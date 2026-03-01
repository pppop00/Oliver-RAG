# RESUME_GENERATE_SKILLS.md

doc_version: 1.0
owner: Oliver Hong
last_updated: 2026-03-01

## Purpose

This document is the mandatory pre-read policy for role-based one-page resume generation.
Any workflow that runs `generate-role-resume` must read and validate this file first.

## Inputs

- role
- `oliver-knowledge-base/structured-data/resume.yaml`
- `oliver-knowledge-base/experiences/*.md`
- `oliver-knowledge-base/structured-data/skills-matrix.yaml`
- `Oliver Hong Resume 2026.docx`

## Skills Prioritization

### Must-Have Keywords

- investment banking
- lbo
- valuation
- due diligence
- deal
- financial modeling
- irr
- monte carlo

### Boost Keywords

- private equity
- portfolio
- aum
- term sheet
- risk analytics
- compliance
- power bi
- sql

### Penalty Keywords

- unrelated personal reflection
- generic objective statement

### Role-Specific Top Skill Buckets

1. Financial modeling and transaction analytics
2. Risk and compliance analytics
3. SQL and ETL support for audit-ready data
4. BI and executive reporting

## Content Selection Rules

- Select at most 4 professional experiences for role resumes.
- Keep 1 leadership entry if space allows.
- Each selected experience has a bullet cap based on template slots.
- Prioritize bullets that include measurable business impact:
  - `%`
  - `USD`
  - `AUM`
  - deal count

## One-Page Trim Policy

Trim order:

1. Compress long bullet sentences while preserving Action + Metric + Outcome.
2. Drop lowest-scored bullet lines.
3. Reduce total selected experiences from 4 to 3 if still over budget.

Do not remove:

- Education section
- Most recent core experience

## Format Guardrails

The generator must preserve template formatting from `Oliver Hong Resume 2026.docx`:

- font family
- page margins
- line spacing
- section border style
- bullet/numbering style

## Output Convention

- Filename (finance-friendly): `YYYYMMDD_Oliver_Hong_Resume_<RoleTitle>.docx`
- Same-day duplicates: append sequence suffix `_02`, `_03`, ...
- Directory: `/Users/pppop/Desktop/Projects/Oliver RAG/resume-output/`

## Preflight Checklist

- [ ] Role profile exists, or fallback profile is loaded.
- [ ] Skill prioritization rules are available.
- [ ] One-page budget is computable from template slots.
- [ ] Template file exists and is readable.
- [ ] `pre_read=ok` is logged before generation starts.

## Failure and Fallback

- If this file is missing: fail fast and exit.
- If required sections are missing: fail fast and exit.
- If role profile is missing: fallback to generic profile and log `profile_fallback=true`.
- If one-page trimming cannot converge: stop generation and return actionable error.
