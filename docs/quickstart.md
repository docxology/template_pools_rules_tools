# Run the integration and render the manuscript

## Standalone smoke check

Install Python 3.11 or newer and uv. Run the following at this repository's
root. Use a disposable checkout for regeneration because scripts write into
`output/`, which includes tracked publication artifacts.

```sh
uv sync --locked --extra dev
uv run python scripts/01_validate_sources.py
uv run python scripts/02_run_integration.py
uv run python scripts/03_generate_manuscript.py
uv run python scripts/04_validate_strong_rules.py
```

The standalone checkout exercises the readers' missing-resource behavior.
The integration uses bundled `_template_resources/<layer>/templates/` if
present, then looks for the shared layer in a Template checkout. A bare clone
does not carry the shared resources. Its smoke run logs missing inputs and
emits the results for that environment. Use the complete Template checkout
below to reproduce the full resource counts and run the coverage gate.

## Full integration and render

Install Python 3.15, uv, jq, GNU `timeout` or `gtimeout`, Pandoc 3.14,
pandoc-crossref v0.3.26b, and XeLaTeX with the
[Template TeX packages](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/README.md#L565-L574).
Set `POOLS_CHECKOUT` to the absolute path of this checkout. From its parent,
create and initialize the pinned runner.

```sh
git clone https://github.com/docxology/template.git pools-template-runner
cd pools-template-runner
git checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
uv sync --locked --python 3.15
project=projects/working/template_pools_rules_tools
mkdir -p projects/working
git -C "$POOLS_CHECKOUT" worktree add --detach "$PWD/$project" HEAD
mv "$project/output" "$(mktemp -d)/published-output"

uv run pytest "$project/tests" --cov="$project/src" --cov-fail-under=90
for script in "$project"/scripts/0[1-5]_*.py; do
  uv run python "$script" || exit $?
done
uv run python scripts/pipeline/stage_03_render.py --project working/template_pools_rules_tools
uv run python scripts/pipeline/stage_04_validate.py --project working/template_pools_rules_tools
```

Run the analysis scripts in order. The figure script writes to the checkout's
manuscript figure directory and mirrors the regenerated images and registry
into `output/figures/`. Stage 03 calls the hydration hook automatically.
Stage 04 validates the fresh outputs. See the
[artifact inventory](resource_contracts.md#outputs) for the result paths.

From the standalone project directory, use Lychee for an offline Markdown link
check and let Git check patch whitespace:

```sh
lychee --offline README.md STANDALONE.md AGENTS.md 'docs/**/*.md'
git diff --check
```
