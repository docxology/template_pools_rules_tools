# tests/ — template_pools_rules_tools

Project tests (90% coverage floor on `src/`, configured in `pyproject.toml`;
see the [verification guide](../docs/quickstart.md) for the shared-resource setup). Real fixtures under `fonds/`,
`rules/`, and `tools/` template trees — no mocks.

## Running

```bash
# From this repository root (monorepo: prefix with
# projects/templates/template_pools_rules_tools/ and run from the monorepo root)
uv run pytest tests/ --cov=src --cov-fail-under=90
```

## Files

The suite currently contains eleven test modules:

`test_coverage_extras.py`, `test_figures.py`, `test_fonds_reader.py`,
`test_generate_figures_script.py`, `test_integration.py`,
`test_manuscript_variables.py`, `test_property_based.py`,
`test_resource_schema.py`, `test_rules_applier.py`,
`test_strong_rule_evaluator.py`, and `test_tools_invoker.py`.

## See also

- [`../AGENTS.md`](../AGENTS.md)
- [Reference](../docs/reference/tests.md)
