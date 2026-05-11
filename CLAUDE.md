# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Claude Code / Codex skill (not a runnable application). It provides a structured PM dialogue protocol that guides users through requirements elicitation and outputs PRD documents. The skill is invoked when users mention product requirements, PRD, or related trigger words.

## Architecture

- `SKILL.md` — The core prompt: role definition, 5-phase workflow, challenge logic, material handling rules. This is what gets loaded into the LLM context when the skill triggers.
- `commands/product-manager.md` — Thin entry point with frontmatter (name, description, trigger words) that `<include>`s SKILL.md.
- `references/question-bank.md` — Dynamic question routing tables for each phase. SKILL.md references this at runtime.
- `references/prd-template.md` — Full PRD output template with fill rules. Used in Phase 4.
- `scripts/parse_document.py` — Parses .docx/.xlsx/.pptx to markdown (stdout). Uses python-docx, openpyxl, python-pptx.
- `scripts/transcribe_media.py` — Transcribes audio/video via faster-whisper. Outputs timestamped markdown to stdout.

## Plugin Entry Points

```
.claude-plugin/plugin.json   → Claude Code
.codex-plugin/plugin.json    → Codex (OpenAI CLI)
```

Both reference `./commands/product-manager.md` as the command entry.

## Running Scripts

```bash
# Document parsing (docx/xlsx/pptx)
python3 scripts/parse_document.py <file_path>

# Audio/video transcription (requires ffmpeg installed)
python3 scripts/transcribe_media.py <file_path> [--model small]
```

Dependencies: `pip install -r scripts/requirements.txt`

## Key Design Decisions

- All content is in Chinese — the skill targets Chinese-speaking business users.
- The skill uses a single-question-per-turn protocol with progress labels like `[阶段名称 Q2/4]`.
- Each phase is capped at 3-6 questions max; the entire guided flow should not exceed ~20 questions.
- PM challenge logic has explicit "accept boundaries" (compliance, verified data, org constraints) — never challenge those.
- PRD generation marks AI-inferred acceptance criteria with `[AI推导，待确认]` and missing info with `[待补充]`.
- `{skill_dir}` in SKILL.md refers to this repository's root path at runtime.
