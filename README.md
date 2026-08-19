# Agent Skills

[![Validate](https://github.com/owainlewis/agent-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/owainlewis/agent-skills/actions/workflows/validate.yml)

Five focused skills for clearer prompts, writing, and teaching.

This library is small by design. Each skill has one job, works across compatible agents, and is written to change behaviour rather than add more prompt noise.

## Install

Browse the collection and choose where to install it:

```sh
npx skills@latest add owainlewis/agent-skills
```

Install one skill directly:

```sh
npx skills@latest add owainlewis/agent-skills --skill teach
```

Add `--global` to install for your user account instead of the current project. The CLI supports Codex, Claude Code, Cursor, and other clients that implement Agent Skills.

Update installed skills with:

```sh
npx skills@latest update
```

## The skills

| Skill | Job | Use it for |
|---|---|---|
| [`deslop`](skills/deslop/SKILL.md) | Remove AI writing patterns without flattening the writer's voice. | Replies, emails, documentation, articles, lessons, scripts, and business writing. |
| [`teach`](skills/teach/SKILL.md) | Turn an AI or technical topic into a tutorial that teaches one usable outcome. | Course lessons, technical articles, video scripts, workshops, newsletters, and standalone guides. |
| [`clarify`](skills/clarify/SKILL.md) | Turn a rough request into a prompt a fresh agent can execute. | Voice dumps, vague plans, incomplete tasks, and prompts that need scope or success criteria. |
| [`compress`](skills/compress/SKILL.md) | Reduce information or instructions to their smallest useful form. | Prompts, specifications, plans, skills, notes, and brain dumps that cost too many tokens. |
| [`explain-visually`](skills/explain-visually/SKILL.md) | Build a responsive HTML explainer around relationships that prose alone makes hard to see. | Architectures, flows, changes, comparisons, state transitions, and technical mental models. |

Invoke a skill using your agent's normal syntax, such as `$teach` in Codex or `/teach` in Claude Code.

## Example prompts

```text
Use $deslop to edit this article without losing my dry tone.

Use $teach to turn these notes into a course lesson on how tool calling works.

Use $clarify to turn this voice dump into a prompt for a coding agent.

Use $compress to cut this specification to the smallest version that preserves every requirement.

Use $explain-visually to show how this request moves through the system.
```

## How they fit together

`clarify` fixes the brief. `teach` creates the tutorial. `explain-visually` handles the parts that need a picture. `deslop` removes AI habits from the prose. `compress` cuts accumulated instruction noise without losing meaning.

You can use one skill alone or compose them. A typical tutorial workflow is `clarify` -> `teach` -> `deslop`, with `explain-visually` when a diagram would genuinely help.

## Design principles

- One skill, one recurring job.
- Plain descriptions that make triggering predictable.
- Instructions that preserve facts, constraints, and user intent.
- Portable Markdown with no required service or framework.
- Examples only when they define behaviour or expose an edge case.
- Automated checks for frontmatter, metadata, links, and repository drift.

## Development

Each skill lives in `skills/<name>/SKILL.md` and follows the [Agent Skills specification](https://agentskills.io/specification). Codex UI metadata lives beside it in `skills/<name>/agents/openai.yaml`.

Run the local checks before committing:

```sh
make validate
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar and contribution workflow.

Software delivery skills such as `spec`, `plan`, `implement`, and `task-to-pr` live in [owainlewis/blueprint](https://github.com/owainlewis/blueprint).

## Credits

`deslop` is adapted from Lauren Tan's [Unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md).

`teach` is informed by Lauren Tan's [Teach](https://github.com/cursor/plugins/blob/main/pstack/skills/teach/SKILL.md), rewritten here for tutorial, course, article, video, and workshop production.

## License

[MIT](LICENSE)
