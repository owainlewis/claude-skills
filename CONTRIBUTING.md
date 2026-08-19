# Contributing

This repository stays useful by staying small. A new skill should solve a recurring job that the existing skills do not already cover.

## Quality bar

- Give the skill one clear job and a short, verb-led name.
- Put only `name` and `description` in `SKILL.md` frontmatter.
- Describe both what the skill does and when it should trigger.
- Write instructions as commands for another capable agent. Do not explain things the agent already knows.
- Preserve facts, user intent, and explicit constraints.
- Include examples only when they define a required format or reveal an edge case.
- Keep `SKILL.md` under 500 lines. Split optional detail into `references/` only when it saves context for common runs.
- Add matching `agents/openai.yaml` metadata and list the skill in the root README.
- Avoid hidden dependencies. State any required tool, service, or environment in the skill.

## Make a change

1. Edit or add `skills/<name>/SKILL.md`.
2. Update `skills/<name>/agents/openai.yaml`.
3. Update the skill table and examples in `README.md` when behaviour or inventory changes.
4. Run `make validate`.
5. Test substantial instruction changes on a realistic prompt before opening a pull request.

Pull requests should explain the behaviour that changed, show the prompt used for testing, and include a representative output or a short account of what improved.
