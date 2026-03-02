from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Dict, List

from docx import Document
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.shared import Inches


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
    if not p.runs:
        p.add_run(text)
        return

    # Keep original run-level formatting by distributing new text across
    # existing runs in proportion to original run lengths.
    original_lengths = [len(r.text) for r in p.runs]
    total_orig = sum(original_lengths)

    if total_orig <= 0:
        for r in p.runs:
            r.text = ""
        p.runs[0].text = text
        return

    n = len(text)
    allocated = []
    used = 0
    for i, orig_len in enumerate(original_lengths):
        if i == len(original_lengths) - 1:
            allocated.append(max(0, n - used))
            break
        share = int(round((orig_len / total_orig) * n))
        # Avoid consuming the entire remainder too early.
        max_allowed = max(0, n - used - (len(original_lengths) - i - 1))
        share = min(max_allowed, max(0, share))
        allocated.append(share)
        used += share

    cursor = 0
    for run, chunk_len in zip(p.runs, allocated):
        run.text = text[cursor : cursor + chunk_len]
        cursor += chunk_len


def _fit(text: str, limit: int) -> str:
    # Keep tab separators for two-column lines.
    if "\t" in text:
        parts = text.split("\t", 1)
        left = _fit(parts[0], max(8, int(limit * 0.62)))
        right = _fit(parts[1], max(6, int(limit * 0.32)))
        return f"{left}\t{right}"

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


def compose_two_col(left: str, right: str, width: int = 112) -> str:
    left_clean = " ".join((left or "").split())
    right_clean = " ".join((right or "").split())
    if not right_clean:
        return left_clean
    # Use tab separator so right column can align by right tab stop.
    return f"{left_clean}\t{right_clean}"


def _set_right_tab_stop(paragraph, pos_inches: float = 7.40) -> None:
    paragraph.paragraph_format.tab_stops.add_tab_stop(Inches(pos_inches), WD_TAB_ALIGNMENT.RIGHT)


def _rewrite_single_run_paragraph(doc: Document, index: int, text: str) -> None:
    p = doc.paragraphs[index]
    first_style = {}
    if p.runs:
        fr = p.runs[0]
        first_style = {
            "bold": fr.bold,
            "italic": fr.italic,
            "underline": fr.underline,
            "font_name": fr.font.name,
            "font_size": fr.font.size,
        }

    # Clear non-format content (runs/hyperlinks/etc.) while preserving paragraph properties.
    p_elm = p._p
    for child in list(p_elm):
        if child.tag.endswith("}pPr"):
            continue
        p_elm.remove(child)

    r = p.add_run(text)
    if first_style:
        r.bold = first_style["bold"]
        r.italic = first_style["italic"]
        r.underline = first_style["underline"]
        if first_style["font_name"]:
            r.font.name = first_style["font_name"]
        if first_style["font_size"]:
            r.font.size = first_style["font_size"]


def apply_generated_data(doc: Document, data: GeneratedResumeData) -> None:
    budgets = extract_budgets(doc)

    _set_paragraph_text(doc, HEADER_LINES["name"], _fit(data.name, budgets.get(0, 40)))
    # Contact line may contain legacy hyperlink nodes in template; rewrite as plain single run.
    # Keep full contact line whenever possible; avoid email truncation.
    _rewrite_single_run_paragraph(doc, HEADER_LINES["contact"], _fit(data.contact, 220))

    for i, idx in enumerate(EDUCATION_LINES):
        text = data.education_lines[i] if i < len(data.education_lines) else ""
        if "\t" in text:
            _set_right_tab_stop(doc.paragraphs[idx])
        _set_paragraph_text(doc, idx, _fit(text, budgets.get(idx, 120)) if text else "")

    for i, idx in enumerate(SKILL_LINES):
        text = data.skill_lines[i] if i < len(data.skill_lines) else ""
        _set_paragraph_text(doc, idx, _fit(text, budgets.get(idx, 130)) if text else "")

    for slot_idx, slot in enumerate(EXPERIENCE_SLOTS):
        if slot_idx < len(data.experiences):
            exp = data.experiences[slot_idx]
            if "\t" in str(exp["header"]):
                _set_right_tab_stop(doc.paragraphs[slot["header"]])
            if "\t" in str(exp["role"]):
                _set_right_tab_stop(doc.paragraphs[slot["role"]])
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

    if "\t" in data.leadership_title:
        _set_right_tab_stop(doc.paragraphs[LEADERSHIP_SLOT["title"]])
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
