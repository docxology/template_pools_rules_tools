# docs/ — template_pools_rules_tools

Human entry point for this repository's documentation. The repo's own README.md
remains the primary overview; this directory collects stable how-to and
reference material.

## What this repo is

`template_pools_rules_tools` — "Pools, Rules, and Tools: A Template-Integrated
Resource Architecture". A meta-project exemplar demonstrating integration of
three top-level resource directories (`fonds/`, `rules/`, `tools/`) and four
public tool exemplars. See the root `README.md` for the full purpose and
structure map.

## Repository layout (top level)

| Path | Role |
|---|---|
| `src/` | Project business logic (TypedDicts, fonds/rules/tools readers, integration) |
| `scripts/` | Thin orchestrators importing from `src/` |
| `tests/` | Project test suite |
| `manuscript/` | Manuscript sections, `config.yaml`, references, figures |
| `output/` | Reproducibility bundle (tracked, like every other public exemplar) |
| `data/` | Project data, incl. `claim_ledger.yaml` |
| `docs/` | This documentation directory |

## Running

This exemplar runs from this repository root standalone, or via the template
monorepo from the monorepo root (prefix paths with
`projects/templates/template_pools_rules_tools/`). Project scripts:

```bash
uv run python scripts/01_validate_sources.py
uv run python scripts/02_run_integration.py
uv run python scripts/03_generate_manuscript.py
uv run python scripts/04_validate_strong_rules.py
```

`scripts/05_generate_figures.py` and `scripts/z_generate_manuscript_variables.py`
import the monorepo `infrastructure/` package and only run inside a full template
checkout.

Forks: copy `manuscript/config.yaml.example` to `manuscript/config.yaml`.

## Testing

Project pytest config lives in `pyproject.toml` (`testpaths = ["tests"]`,
`pythonpath = [".", "src"]`). From this repository root:

```bash
uv run pytest tests/ --cov=src --cov-fail-under=90
```

The 90% floor needs the `fonds/`, `rules/`, and `tools/` trees: a standalone
copy that ships only `src/` reaches ~65% and fails the resource-dependent
strong-rule and receipt tests, so run without `--cov` there.

## Documentation maintenance

Docs here are hand-maintained, short, and evidence-based: every factual claim
traces to a repo file (README, AGENTS.md, config, source headers). Cross
references to monorepo-level guides (`docs/`, `infrastructure/` at the template
root) resolve only inside a full template checkout, not in this standalone
checkout.
