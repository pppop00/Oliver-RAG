from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

CORE_MD_DIRS = [
    "oliver-knowledge-base/experiences",
    "oliver-knowledge-base/projects",
    "oliver-knowledge-base/skills",
    "oliver-knowledge-base/education",
    "oliver-knowledge-base/reflections",
]
FRONTMATTER_REQUIRED = {
    "title",
    "type",
    "timeline",
    "tags",
    "domains",
    "status",
    "importance",
    "created",
    "updated",
    "related",
}
DATE_MONTH_RE = re.compile(r"^\d{4}-\d{2}$")
DATE_DAY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass
class GateResult:
    passed: bool
    checks: Dict[str, bool]
    details: Dict[str, List[str]]


def _iter_md_files(root: Path, rel_dirs: Iterable[str]) -> Iterable[Path]:
    for rel in rel_dirs:
        d = root / rel
        if not d.exists():
            continue
        yield from sorted(d.glob("*.md"))


def validate_relative_links(root: Path) -> Tuple[bool, List[str]]:
    issues: List[str] = []
    link_re = re.compile(r"\]\(([^)#]+)\)")
    for md in _iter_md_files(root, CORE_MD_DIRS):
        content = md.read_text(encoding="utf-8")
        for rel in link_re.findall(content):
            if rel.startswith("http") or rel.startswith("mailto:"):
                continue
            target = (md.parent / rel).resolve()
            if not target.exists():
                issues.append(f"{md.relative_to(root)} -> {rel}")
    return (len(issues) == 0, issues)


def _frontmatter_block(content: str) -> str | None:
    if not content.startswith("---\n"):
        return None
    try:
        end = content.index("\n---\n", 4)
    except ValueError:
        return None
    return content[4:end]


def validate_frontmatter_required(root: Path) -> Tuple[bool, List[str]]:
    issues: List[str] = []
    for md in _iter_md_files(root, CORE_MD_DIRS):
        content = md.read_text(encoding="utf-8")
        fm = _frontmatter_block(content)
        if fm is None:
            issues.append(f"{md.relative_to(root)} missing frontmatter")
            continue
        found = set()
        for line in fm.splitlines():
            if ":" in line and not line.startswith(" "):
                key = line.split(":", 1)[0].strip()
                found.add(key)
        missing = sorted(FRONTMATTER_REQUIRED - found)
        if missing:
            issues.append(f"{md.relative_to(root)} missing keys: {', '.join(missing)}")
    return (len(issues) == 0, issues)


def validate_date_strings(strings: Iterable[str]) -> Tuple[bool, List[str]]:
    issues: List[str] = []
    for value in strings:
        if value in {"present", ""}:
            continue
        if DATE_MONTH_RE.match(value) or DATE_DAY_RE.match(value):
            continue
        issues.append(value)
    return (len(issues) == 0, issues)


def run_change_gate(root: Path, extra_date_values: Iterable[str] | None = None) -> GateResult:
    checks: Dict[str, bool] = {}
    details: Dict[str, List[str]] = {}

    ok_links, bad_links = validate_relative_links(root)
    checks["gate_1_links"] = ok_links
    details["gate_1_links"] = bad_links

    ok_frontmatter, bad_frontmatter = validate_frontmatter_required(root)
    checks["gate_2_frontmatter"] = ok_frontmatter
    details["gate_2_frontmatter"] = bad_frontmatter

    date_values = list(extra_date_values or [])
    ok_dates, bad_dates = validate_date_strings(date_values)
    checks["gate_3_dates"] = ok_dates
    details["gate_3_dates"] = bad_dates

    passed = all(checks.values())
    return GateResult(passed=passed, checks=checks, details=details)
