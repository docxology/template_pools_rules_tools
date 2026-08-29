# docs/AGENTS.md — template_pools_rules_tools

Agent-facing notes for this repository's `docs/` directory.

## Layout

- `README.md` — human entry point: what the repo is, directory map, run/test
  commands (copied from root `README.md` and `AGENTS.md`).
- This file — agent conventions for maintaining `docs/`.

## Key modules (from root AGENTS.md)

- `src/type_defs.py` — all TypedDict definitions; edit there first.
- `src/fonds_reader.py` — reads `fonds/templates/template_bibliography`,
  `template_contacts`, `template_datasets`.
- `src/rules_applier.py` — loads `rules/templates/template_project_rules` and
  `template_manuscript_rules`.
- `src/strong_rule_evaluator.py` — semantic evaluation of strong rule YAML.
- `src/tools_invoker.py` — discovers `tools/templates/template_code_executor`
  and other tool manifests.
- `src/integration.py` — orchestrates all three into a combined demo result.

## Conventions observed in this repo

- Manuscript follows the shared template standard: `manuscript/config.yaml` is
  the live metadata source; `config.yaml.example` is the fork template.
- `{{TOKEN}}` placeholders in manuscript markdown are render-time variables,
  not defects; ground truth for integration and figure counts lives in
  `output/data/manuscript_variables.json` (root AGENTS.md).
- Resilience policy: `src/` functions return empty collections and log warnings
  when resource directories are absent; tests skip via `pytest.mark.skipif`.
- Decision memory: root `README.md` links the monorepo
  `docs/rules/memory_and_decision_records.md` guidance (resolves inside a full
  template checkout only).
- Docs changes should be committed path-scoped to `docs` (and `manuscript`
  when applicable), never mixed with code changes.

## Scope rules for agents

- DOCS + MANUSCRIPT CONTENT ONLY: do not modify `src/`, `tests/`, `scripts/`,
  or build configs when working in `docs/`.
- Never fabricate numbers: measured counts belong to generated docs at the
  monorepo level (`docs/_generated/COUNTS.md`), not hand-written prose here.
