# Resource and output contracts

## Inputs

| Layer | Contract | Reader |
| --- | --- | --- |
| Fonds | `fonds.yaml` declares a bibliography, contacts, or dataset pool. CSV or JSON records are normalized for aggregation. | [Fonds reader](../src/fonds_reader.py) |
| Rules | `rules.yaml` indexes soft guidance and strong requirements. Semantic checks evaluate real project paths, headings, and bibliography. | [Rule reader](../src/rules_applier.py) and [strong-rule evaluator](../src/strong_rule_evaluator.py) |
| Tools | `tools.yaml` declares input, output, and entrypoint files. The library reports discovery and path validation. | [Tool reader](../src/tools_invoker.py) |

Project readers treat the shared trees as read-only. A missing resource logs a
warning and yields an empty or missing result, so the combined summary can report
partial availability. Inspect the statuses as well as the CLI exit codes.
The strong-rule CLI treats missing conventional IMRaD headings as advisory for
this architecture manuscript. It still evaluates the current bibliography and
other applicable constraints.

## Outputs

| Path | Contents |
| --- | --- |
| `output/data/manuscript_variables.json` | Values derived from the current integration run |
| `output/figures/` | Eight registered content figures and the cover graphic |
| `output/manuscript/` | Generated copy with token substitutions for rendering |
| `output/pdf/` | Combined paper and PDF intermediates |
| `output/web/index.html` | Combined HTML |
| `output/slides/` | Section slide decks when enabled |
| `output/reports/` | Validation, figure and other output evidence, and render provenance |

`output/` is also the home of the tracked publication snapshot. The
[authored manuscript](manuscript/README.md) remains the source for edits.
