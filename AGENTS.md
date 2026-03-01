# AGENTS.md

## Mandatory Entry Rule

Before any read/write work in this repository, you must read:

- `./SKILLS.md`

This is the master governance document for all RAG changes.

For role-based resume generation, you must also read:

- `./RESUME_GENERATE_SKILLS.md`

## Required Workflow

If the task involves any of the following:

- new or updated resume
- new resource/source document
- new external links (LinkedIn/GitHub/Website/Portfolio)
- schema change
- retrieval/RAG pipeline or indexing change

you must follow the SOP and Gates in `SKILLS.md`.

If the task is `generate-role-resume`, you must run preflight checks defined in
`RESUME_GENERATE_SKILLS.md` first. Generation is not allowed without a valid pre-read.

## Conflict Handling

If `SKILLS.md` conflicts with repository reality:

1. Update `SKILLS.md` first.
2. Then implement the requested data/document change.

## Completion Gate

Do not end a task until the `Change Gate` checks in `SKILLS.md` are satisfied.
