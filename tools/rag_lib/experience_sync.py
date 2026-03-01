from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List

import yaml

from .validators import run_change_gate


@dataclass
class SyncResult:
    experience_file: Path
    updated_files: List[Path]
    gate_passed: bool
    gate_details: Dict[str, List[str]]


REQUIRED_FIELDS = {
    "title",
    "company",
    "location",
    "employment_type",
    "start_date",
    "end_date",
    "highlights",
    "technologies",
    "domains",
    "tags",
    "importance",
}


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s or "item"


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _dump_yaml(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def _today_day() -> str:
    return date.today().strftime("%Y-%m-%d")


def _today_month() -> str:
    return date.today().strftime("%Y-%m")


def _validate_payload(payload: dict) -> None:
    missing = sorted(REQUIRED_FIELDS - set(payload.keys()))
    if missing:
        raise ValueError(f"payload missing fields: {', '.join(missing)}")
    if not isinstance(payload.get("highlights"), list) or not payload["highlights"]:
        raise ValueError("payload.highlights must be a non-empty list")


def _experience_markdown(payload: dict, rel_resume: str = "../structured-data/resume.yaml") -> str:
    created = _today_day()
    tags = payload.get("tags", [])
    domains = payload.get("domains", [])
    related = payload.get("related", [])
    if not related:
        related = ["../skills/python-for-data-and-ml.md"]

    lines = [
        "---",
        f'title: "{payload["title"]} @ {payload["company"]}"',
        'type: "experience"',
        "timeline:",
        f'  start: "{payload["start_date"]}"',
        f'  end: "{payload["end_date"]}"',
        '  period: "grad_and_career"',
        f"tags: {tags}",
        f"domains: {domains}",
        'status: "ongoing"' if payload["end_date"] == "present" else 'status: "completed"',
        f'importance: {int(payload["importance"])}',
        f"created: {created}",
        f"updated: {created}",
        "related:",
    ]
    for r in related:
        lines.append(f'  - "{r}"')
    lines.extend(
        [
            "---",
            "",
            "## Summary",
            payload.get("summary", "Core role focused on measurable business impact and analytics execution."),
            "",
            "## Basic Information",
            f'- Company: {payload["company"]}',
            f'- Role: {payload["title"]}',
            f'- Location: {payload["location"]}',
            f'- Timeline: {payload["start_date"]} to {payload["end_date"]}',
            "",
            "## Quantified Outcomes",
        ]
    )
    for h in payload["highlights"]:
        lines.append(f"- {h}")
    lines.extend(["", "## Technologies", f"- {', '.join(payload.get('technologies', []))}", "", "## Related Structured Data", f"- [resume.yaml]({rel_resume})"])
    return "\n".join(lines) + "\n"


def sync_experience(root: Path, payload_path: Path) -> SyncResult:
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    _validate_payload(payload)

    kb = root / "oliver-knowledge-base"
    structured = kb / "structured-data"

    exp_slug = f"{_slugify(payload['company'])}-{_slugify(payload['title'])}"
    exp_file = kb / "experiences" / f"{exp_slug}.md"
    exp_file.write_text(_experience_markdown(payload), encoding="utf-8")

    updated_files = [exp_file]

    resume_path = structured / "resume.yaml"
    resume = _load_yaml(resume_path)
    experience = resume.get("experience", [])

    new_item = {
        "title": payload["title"],
        "company": payload["company"],
        "location": payload["location"],
        "employment_type": payload["employment_type"],
        "start_date": payload["start_date"],
        "end_date": payload["end_date"],
        "highlights": payload["highlights"],
        "technologies": payload["technologies"],
        "markdown_link": f"../experiences/{exp_file.name}",
    }

    replaced = False
    for i, item in enumerate(experience):
        if item.get("title") == new_item["title"] and item.get("company") == new_item["company"] and item.get("start_date") == new_item["start_date"]:
            experience[i] = new_item
            replaced = True
            break
    if not replaced:
        experience.append(new_item)

    def exp_key(item: dict):
        s = item.get("start_date", "0000-00")
        return s

    experience = sorted(experience, key=exp_key, reverse=True)
    resume["experience"] = experience
    resume["last_updated"] = _today_day()
    resume["version"] = str(resume.get("version", "1.0"))
    _dump_yaml(resume_path, resume)
    updated_files.append(resume_path)

    timeline_path = structured / "timeline.yaml"
    timeline = _load_yaml(timeline_path)
    entries = timeline.get("timeline", [])
    entries.append(
        {
            "date": payload["start_date"],
            "event": f"Started {payload['title']} at {payload['company']}",
            "category": "experience",
            "importance": int(payload["importance"]),
            "link": f"../experiences/{exp_file.name}",
        }
    )
    if payload["end_date"] != "present":
        entries.append(
            {
                "date": payload["end_date"],
                "event": f"Completed {payload['title']} at {payload['company']}",
                "category": "experience",
                "importance": max(1, int(payload["importance"]) - 1),
                "link": f"../experiences/{exp_file.name}",
            }
        )
    timeline["timeline"] = sorted(entries, key=lambda x: x.get("date", "0000-00"))
    timeline.setdefault("metadata", {})["last_updated"] = _today_day()
    _dump_yaml(timeline_path, timeline)
    updated_files.append(timeline_path)

    skills_path = structured / "skills-matrix.yaml"
    skills_matrix = _load_yaml(skills_path)
    skills_root = skills_matrix.get("skills", {})
    payload_tech = [str(t) for t in payload.get("technologies", [])]
    evidence_line = f"{payload['company']}: {payload['title']}"

    for _, bucket in skills_root.items():
        if not isinstance(bucket, list):
            continue
        for skill in bucket:
            name = str(skill.get("name", ""))
            if any(name.lower() in t.lower() or t.lower() in name.lower() for t in payload_tech):
                skill["last_used"] = _today_month()
                ev = skill.get("evidence")
                if not isinstance(ev, list):
                    ev = []
                if evidence_line not in ev:
                    ev.append(evidence_line)
                skill["evidence"] = ev
    skills_matrix.setdefault("metadata", {})["last_updated"] = _today_day()
    _dump_yaml(skills_path, skills_matrix)
    updated_files.append(skills_path)

    queries_path = structured / "test-queries.yaml"
    queries = _load_yaml(queries_path)
    test_cases = queries.get("test_cases", [])
    query_obj = {
        "query": f"What impact did Oliver deliver as {payload['title']} at {payload['company']}?",
        "expected_docs": [f"../experiences/{exp_file.name}"],
        "expected_facts": payload["highlights"][:2],
    }
    test_cases.append(query_obj)
    queries["test_cases"] = test_cases
    queries.setdefault("metadata", {})["last_updated"] = _today_day()
    _dump_yaml(queries_path, queries)
    updated_files.append(queries_path)

    date_values = [payload.get("start_date", ""), payload.get("end_date", "")]
    gate = run_change_gate(root, extra_date_values=date_values)

    return SyncResult(
        experience_file=exp_file,
        updated_files=updated_files,
        gate_passed=gate.passed,
        gate_details=gate.details,
    )
