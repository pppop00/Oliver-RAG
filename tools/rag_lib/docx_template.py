from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from docx import Document


EXPERIENCE_SLOTS = [
    {"header": 18, "role": 19, "bullets": [20, 21, 22, 23], "spacer": 24},
    {"header": 25, "role": 26, "bullets": [27, 28, 29, 30, 31]},
    {"header": 32, "role": 33, "bullets": [34, 35, 36, 37, 38]},
    {"header": 39, "role": 40, "bullets": [41, 42, 43, 44]},
    {"header": 45, "role": 46, "bullets": [47, 48]},
]
LEADERSHIP_SLOT = {"title": 51, "bullets": [52, 53]}
EDUCATION_LINES = [4, 5, 6, 7, 8]
SKILL_LINES = [11, 12, 13, 14, 15]
HEADER_LINES = {"name": 0, "contact": 1}


@dataclass
class GeneratedResumeData:
    name: str
    contact: str
    education_lines: List[str]
    skill_lines: List[str]
    experiences: List[Dict[str, List[str] | str]]
    leadership_title: str
    leadership_bullets: List[str]


def load_template(template_path: Path) -> Document:
    return Document(str(template_path))


def extract_budgets(doc: Document) -> Dict[int, int]:
    budgets: Dict[int, int] = {}
    for idx, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        if text:
            budgets[idx] = max(24, len(text))
    return budgets


def _set_paragraph_text(doc: Document, index: int, text: str) -> None:
    p = doc.paragraphs[index]
    p.text = text


def _fit(text: str, limit: int) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= limit:
        return cleaned
    # First pass: drop parenthetical info.
    import re

    shrunk = re.sub(r"\s*\([^)]*\)", "", cleaned)
    shrunk = " ".join(shrunk.split())
    if len(shrunk) <= limit:
        return shrunk
    # Hard trim.
    if limit <= 3:
        return shrunk[:limit]
    return shrunk[: limit - 3].rstrip() + "..."


def apply_generated_data(doc: Document, data: GeneratedResumeData) -> None:
    budgets = extract_budgets(doc)

    _set_paragraph_text(doc, HEADER_LINES["name"], _fit(data.name, budgets.get(0, 40)))
    _set_paragraph_text(doc, HEADER_LINES["contact"], _fit(data.contact, budgets.get(1, 160)))

    for i, idx in enumerate(EDUCATION_LINES):
        text = data.education_lines[i] if i < len(data.education_lines) else ""
        _set_paragraph_text(doc, idx, _fit(text, budgets.get(idx, 120)) if text else "")

    for i, idx in enumerate(SKILL_LINES):
        text = data.skill_lines[i] if i < len(data.skill_lines) else ""
        _set_paragraph_text(doc, idx, _fit(text, budgets.get(idx, 130)) if text else "")

    for slot_idx, slot in enumerate(EXPERIENCE_SLOTS):
        if slot_idx < len(data.experiences):
            exp = data.experiences[slot_idx]
            _set_paragraph_text(doc, slot["header"], _fit(str(exp["header"]), budgets.get(slot["header"], 130)))
            _set_paragraph_text(doc, slot["role"], _fit(str(exp["role"]), budgets.get(slot["role"], 130)))
            bullets = list(exp["bullets"])
            for i, para_idx in enumerate(slot["bullets"]):
                txt = bullets[i] if i < len(bullets) else ""
                _set_paragraph_text(doc, para_idx, _fit(txt, budgets.get(para_idx, 130)) if txt else "")
        else:
            _set_paragraph_text(doc, slot["header"], "")
            _set_paragraph_text(doc, slot["role"], "")
            for para_idx in slot["bullets"]:
                _set_paragraph_text(doc, para_idx, "")

    _set_paragraph_text(
        doc,
        LEADERSHIP_SLOT["title"],
        _fit(data.leadership_title, budgets.get(LEADERSHIP_SLOT["title"], 140)) if data.leadership_title else "",
    )
    for i, para_idx in enumerate(LEADERSHIP_SLOT["bullets"]):
        txt = data.leadership_bullets[i] if i < len(data.leadership_bullets) else ""
        _set_paragraph_text(doc, para_idx, _fit(txt, budgets.get(para_idx, 150)) if txt else "")


def save_document(doc: Document, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))
