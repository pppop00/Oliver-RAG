from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

import yaml

from .docx_template import (
    GeneratedResumeData,
    apply_generated_data,
    compose_two_col,
    load_template,
    save_document,
)

REQUIRED_POLICY_HEADINGS = [
    "## Skills Prioritization",
    "## One-Page Trim Policy",
    "## Format Guardrails",
    "## Preflight Checklist",
]

MONTH_NAMES = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}


@dataclass
class PolicyDoc:
    doc_version: str
    skills_prioritization: Dict[str, List[str]]
    trim_policy: Dict[str, List[str]]
    format_guardrails: Dict[str, str]
    preflight_checklist: List[str]
    raw_text: str


@dataclass
class PreflightResult:
    passed: bool
    checks: List[Tuple[str, bool, str]]


@dataclass
class GenerationResult:
    output_path: Path
    profile_fallback: bool
    preflight: PreflightResult


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s or "role"


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_resume_generate_skills(path: Path) -> PolicyDoc:
    if not path.exists():
        raise FileNotFoundError(f"missing policy file: {path}")
    text = path.read_text(encoding="utf-8")

    for heading in REQUIRED_POLICY_HEADINGS:
        if heading not in text:
            raise ValueError(f"policy missing required heading: {heading}")

    version_match = re.search(r"^doc_version:\s*([^\n]+)$", text, flags=re.MULTILINE)
    if not version_match:
        raise ValueError("policy missing doc_version")

    must = re.findall(r"^\-\s+([\w\- ]+)$", _section(text, "### Must-Have Keywords"), flags=re.MULTILINE)
    boost = re.findall(r"^\-\s+([\w\- ]+)$", _section(text, "### Boost Keywords"), flags=re.MULTILINE)
    penalty = re.findall(r"^\-\s+([\w\- ]+)$", _section(text, "### Penalty Keywords"), flags=re.MULTILINE)
    checklist = re.findall(r"^\- \[ \] (.+)$", _section(text, "## Preflight Checklist"), flags=re.MULTILINE)

    return PolicyDoc(
        doc_version=version_match.group(1).strip(),
        skills_prioritization={"must": must, "boost": boost, "penalty": penalty},
        trim_policy={"order": ["compress_bullets", "drop_low_score_bullets", "reduce_experience_count"]},
        format_guardrails={
            "font": "preserve",
            "margins": "preserve",
            "line_spacing": "preserve",
            "section_border": "preserve",
            "bullet_style": "preserve",
        },
        preflight_checklist=checklist,
        raw_text=text,
    )


def _section(text: str, heading: str) -> str:
    idx = text.find(heading)
    if idx == -1:
        return ""
    tail = text[idx + len(heading) :]
    next_heading = re.search(r"\n##\s+", tail)
    if next_heading:
        return tail[: next_heading.start()]
    return tail


def validate_preflight(
    policy_doc: PolicyDoc,
    role_slug: str,
    template_path: Path,
    role_profile_path: Path,
    profile_fallback: bool,
) -> PreflightResult:
    checks: List[Tuple[str, bool, str]] = []

    checks.append(("policy_loaded", bool(policy_doc.doc_version), f"doc_version={policy_doc.doc_version}"))
    checks.append(("required_rules", len(policy_doc.skills_prioritization.get("boost", [])) > 0, "skills prioritization present"))
    checks.append(("template_readable", template_path.exists(), str(template_path)))
    checks.append(("role_profile", role_profile_path.exists(), f"path={role_profile_path} fallback={profile_fallback}"))
    checks.append(("budget_computable", True, "template slot budget strategy active"))

    passed = all(item[1] for item in checks)
    return PreflightResult(passed=passed, checks=checks)


def enforce_generation_guard(preflight_result: PreflightResult) -> None:
    if not preflight_result.passed:
        details = "; ".join(f"{name}={ok}" for name, ok, _ in preflight_result.checks)
        raise RuntimeError(f"preflight failed: {details}")


def _month_year(value: str) -> str:
    if not value or value == "present":
        return "Present"
    try:
        year, month = value.split("-")
        return f"{MONTH_NAMES.get(month, month)} {year}"
    except ValueError:
        return value


def _date_range(start: str, end: str) -> str:
    return f"{_month_year(start)} – {_month_year(end)}"


def _metrics_score(text: str) -> int:
    score = 0
    score += len(re.findall(r"\b\d+%", text)) * 3
    score += len(re.findall(r"\bUSD\b", text, flags=re.IGNORECASE)) * 3
    score += len(re.findall(r"\b\d+[MK]?\+?\b", text))
    return score


def _score_experience(exp: dict, role_profile: dict, policy_doc: PolicyDoc) -> float:
    blob = " ".join(
        [
            str(exp.get("title", "")),
            str(exp.get("company", "")),
            " ".join(exp.get("highlights", []) or []),
            " ".join(exp.get("technologies", []) or []),
        ]
    ).lower()

    must = role_profile.get("keywords", {}).get("must", []) or policy_doc.skills_prioritization.get("must", [])
    boost = role_profile.get("keywords", {}).get("boost", []) or policy_doc.skills_prioritization.get("boost", [])
    penalty = role_profile.get("keywords", {}).get("penalty", []) or policy_doc.skills_prioritization.get("penalty", [])

    score = 0.0
    for kw in must:
        if kw.lower() in blob:
            score += 6
    for kw in boost:
        if kw.lower() in blob:
            score += 2
    for kw in penalty:
        if kw.lower() in blob:
            score -= 2

    for h in exp.get("highlights", []) or []:
        score += min(4, _metrics_score(h))

    start = exp.get("start_date", "")
    if re.match(r"^\d{4}-\d{2}$", str(start)):
        year, month = start.split("-")
        score += (int(year) - 2020) * 0.5 + int(month) / 24.0

    return score


def _shorten(text: str, limit: int) -> str:
    cleaned = " ".join(str(text).split())
    if len(cleaned) <= limit:
        return cleaned
    no_paren = re.sub(r"\s*\([^)]*\)", "", cleaned)
    no_paren = " ".join(no_paren.split())
    if len(no_paren) <= limit:
        return no_paren
    if limit <= 3:
        return no_paren[:limit]
    return no_paren[: limit - 3].rstrip() + "..."


def _role_profile(root: Path, role_slug: str) -> Tuple[dict, Path, bool]:
    direct = root / "tools" / "config" / "role_profiles" / f"{role_slug}.yaml"
    if direct.exists():
        return _load_yaml(direct), direct, False
    generic = root / "tools" / "config" / "role_profiles" / "generic.yaml"
    return _load_yaml(generic), generic, True


def _contact_line(personal_info: dict) -> str:
    status_values = list((personal_info.get("status") or {}).values())
    status_text = " | ".join([str(v) for v in status_values if v])
    location = personal_info.get("location") or {}
    city = location.get("city", "")
    state = location.get("state", "")
    loc = f"{city}, {state}".strip(", ")
    phone = personal_info.get("phone", "")
    email = personal_info.get("email", "")

    parts = [p for p in [status_text, loc, f"Cell: {phone}" if phone else "", f"Email: {email}" if email else ""] if p]
    return " | ".join(parts)


def _education_lines(resume: dict) -> List[str]:
    edu = resume.get("education", [])
    lines: List[str] = []
    for item in edu[:2]:
        l1 = compose_two_col(
            str(item.get("institution", "")),
            _date_range(item.get("start_date", ""), item.get("end_date", "")),
            width=112,
        )
        degree = item.get("degree", "")
        major = item.get("major", "")
        minor = item.get("minor", "")
        if minor:
            l2 = f"{degree} in {major}, Minor in {minor}"
        else:
            l2 = f"{degree} in {major}" if degree and major else f"{degree}{major}"
        lines.extend([l1.strip(), l2.strip()])
        honors = item.get("honors", [])
        if honors:
            lines.append("; ".join(honors))
    if len(lines) < 5:
        lines.extend([""] * (5 - len(lines)))
    return lines[:5]


def _skills_lines(resume: dict) -> List[str]:
    skills = resume.get("skills", {})

    def names(bucket: List[dict], limit: int) -> List[str]:
        out = []
        for x in bucket[:limit]:
            n = x.get("name", "")
            if n:
                out.append(n)
        return out

    prog = names(skills.get("programming_languages", []), 5)
    fw = names(skills.get("frameworks_libraries", []), 5)
    tools = names(skills.get("tools_platforms", []), 8)
    domains = names(skills.get("domains", []), 8)

    technical = f"Technical: {', '.join((prog + fw)[:10])}"

    db_items = [x for x in tools if any(k in x.lower() for k in ["sql", "aws", "azure", "oracle", "postgres", "mysql"])]
    if not db_items:
        db_items = tools[:6]
    db_line = f"Database and ETL: {', '.join(db_items[:8])}"

    analytics_items = domains + [x for x in tools if x not in db_items]
    analytics_line = f"Analytics: {', '.join(analytics_items[:8])}"
    analytics_line_2 = f"{', '.join(analytics_items[8:16])}" if len(analytics_items) > 8 else ""

    interests = resume.get("interests", [])
    interest_line = f"Interest: {', '.join(interests)}" if interests else "Interest:"

    return [technical, db_line, analytics_line, analytics_line_2, interest_line]


def _prepare_experience_blocks(resume: dict, role_profile: dict, policy_doc: PolicyDoc) -> List[Dict[str, List[str] | str]]:
    experiences = list(resume.get("experience", []))
    scored = [
        (exp, _score_experience(exp, role_profile=role_profile, policy_doc=policy_doc))
        for exp in experiences
        if str(exp.get("employment_type", "")).lower() != "leadership"
    ]
    scored.sort(key=lambda x: x[1], reverse=True)

    caps = role_profile.get("bullet_caps_per_experience", [4, 5, 5, 4])
    exp_count = int(role_profile.get("section_caps", {}).get("experience_count", 4))

    selected = [exp for exp, _ in scored[:exp_count]]
    blocks = []
    for idx, exp in enumerate(selected):
        cap = caps[idx] if idx < len(caps) else 4
        highlights = exp.get("highlights", []) or []
        highlights_sorted = sorted(highlights, key=_metrics_score, reverse=True)
        bullets = [_shorten(h, 130) for h in highlights_sorted[:cap]]

        header = compose_two_col(str(exp.get("company", "")), str(exp.get("location", "")), width=112).strip()
        role = compose_two_col(
            str(exp.get("title", "")),
            _date_range(exp.get("start_date", ""), exp.get("end_date", "")),
            width=112,
        ).strip()
        blocks.append({"header": header, "role": role, "bullets": bullets})

    # Hard one-page fallback: reduce experiences if too many long bullets.
    total_chars = sum(len(b) for block in blocks for b in block["bullets"])
    if total_chars > 2300 and len(blocks) > 3:
        blocks = blocks[:3]

    return blocks


def _leadership_block(resume: dict) -> Tuple[str, List[str]]:
    leadership_entries = [e for e in resume.get("experience", []) if str(e.get("employment_type", "")).lower() == "leadership"]
    if not leadership_entries:
        return "", []
    entry = leadership_entries[0]
    left = f"{entry.get('title', '')} - {entry.get('company', '')}"
    right = _date_range(entry.get("start_date", ""), entry.get("end_date", ""))
    title = compose_two_col(left, right, width=112)
    bullets = [_shorten(x, 150) for x in (entry.get("highlights", []) or [])[:2]]
    return title, bullets


def _next_output_path(output_dir: Path, role_slug: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    date_stamp = date.today().strftime("%Y%m%d")
    role_part = role_slug.replace("-", "_").title()
    base = f"{date_stamp}_Oliver_Hong_Resume_{role_part}"
    first = output_dir / f"{base}.docx"
    if not first.exists():
        return first

    seq = 2
    while True:
        candidate = output_dir / f"{base}_{seq:02d}.docx"
        if not candidate.exists():
            return candidate
        seq += 1


def generate_role_resume(root: Path, role: str) -> GenerationResult:
    role_slug = _slugify(role)

    policy_path = root / "RESUME_GENERATE_SKILLS.md"
    policy_doc = load_resume_generate_skills(policy_path)

    template_path = root / "Oliver Hong Resume 2026.docx"
    profile, profile_path, profile_fallback = _role_profile(root, role_slug)
    preflight = validate_preflight(
        policy_doc=policy_doc,
        role_slug=role_slug,
        template_path=template_path,
        role_profile_path=profile_path,
        profile_fallback=profile_fallback,
    )
    enforce_generation_guard(preflight)

    print("pre_read=ok")
    if profile_fallback:
        print("profile_fallback=true")

    resume = _load_yaml(root / "oliver-knowledge-base" / "structured-data" / "resume.yaml")
    doc = load_template(template_path)

    personal_info = resume.get("personal_info", {})
    raw_name = str(personal_info.get("name", "Oliver Hong"))
    name = re.sub(r"\s*\([^)]*\)", "", raw_name).strip() or "Oliver Hong"
    contact = _contact_line(personal_info)

    education_lines = _education_lines(resume)
    skill_lines = _skills_lines(resume)
    experiences = _prepare_experience_blocks(resume, profile, policy_doc)
    leadership_title, leadership_bullets = _leadership_block(resume)

    generated = GeneratedResumeData(
        name=name,
        contact=contact,
        education_lines=education_lines,
        skill_lines=skill_lines,
        experiences=experiences,
        leadership_title=leadership_title,
        leadership_bullets=leadership_bullets,
    )

    apply_generated_data(doc, generated)

    out_path = _next_output_path(root / "resume-output", role_slug)
    save_document(doc, out_path)

    return GenerationResult(output_path=out_path, profile_fallback=profile_fallback, preflight=preflight)
