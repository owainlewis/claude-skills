# Repository instructions

This repository contains five portable Agent Skills.

When changing a skill:

- Read the whole skill before editing it.
- Preserve its single job and remove instructions that do not change agent behaviour.
- Keep frontmatter to `name` and `description`; put trigger conditions in the description.
- Use imperative language in the body.
- Keep facts, constraints, failure behaviour, and verification intact.
- Update `agents/openai.yaml` and `README.md` when the public description or inventory changes.
- Run `make validate` before reporting completion.

Do not add generated files, per-skill READMEs, changelogs, or dependencies without a concrete need.
