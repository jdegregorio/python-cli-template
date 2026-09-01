# {{PROJECT_NAME}}

A small, typed Python command-line project designed for agent-led development.
It uses a `src/` layout, standard-library tests and runtime code, uv packaging,
stable repository scripts, and the language-neutral project knowledge contract.

## Start here

```bash
./scripts/check
./scripts/dev --help
```

## Layout

- `src/{{PROJECT_MODULE}}/`: application package
- `tests/`: standard-library unit tests
- `scripts/dev`, `scripts/test`, `scripts/check`: stable agent and human interface
- `docs/`, `openspec/`, `AGENTS.md`: project knowledge and change workflow
- `.agents/skills/`: committed project-specific skills, when selected

The generated example command is intentionally small. Replace it with the
project's actual behavior, then keep tests and documentation aligned.
