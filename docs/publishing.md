# Publication and forks

The [manuscript configuration](manuscript/config.yaml) holds paper metadata,
publication identifiers, and project rule and render settings. Forks can
copy the [example configuration](manuscript/config.yaml.example) and edit
the new project's citation metadata. The standalone repository's citation
sidecars remain in the root.

From the pinned Template checkout after project registration, regenerate the
README status with the configuration path supplied explicitly.

```sh
uv run python -m infrastructure.publishing.status_report \
  --project "$project" --config "$project/docs/manuscript/config.yaml" --write
```

The generator at the pinned revision still writes a footer with the legacy
path. Use the explicit command above when refreshing status. Preserve the
tracked output from the previous release until preparing another release.
