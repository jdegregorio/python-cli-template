# python-cli-template

The small Python CLI overlay used by `musterctl` project templates. It is
applied after the language-neutral `agent-project-template` layer.

The materialized overlay is isolated in `template/`; catalogs should use that
directory as `source_path` and pin an immutable commit.

```bash
./scripts/check
```
