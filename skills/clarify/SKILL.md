---
name: clarify
description: "Turn a vague request, voice dump, rough plan, or half-written prompt into a self-contained prompt that a fresh agent can execute. Use when asked to clarify, refine, improve, tighten, or stress-test an agent task. Resolve safe defaults directly and ask one high-leverage question at a time only when the answer would materially change the work."
---

# Clarify

Turn messy intent into an executable prompt without turning clarification into a ceremony.

## Choose a mode

- Refine directly when the goal is clear and missing details have safe defaults.
- Interview when one unresolved choice would materially change behaviour, data, security, compatibility, cost, output, or proof.
- Execute the clarified prompt only when the user explicitly asks to run it or says "just do it."

## Process

1. Read the request and any referenced material.
2. For repository work, inspect discoverable context such as `AGENTS.md`, `CLAUDE.md`, `README.md`, the file tree, and relevant code before asking questions.
3. Extract the goal, current state, inputs, outputs, constraints, scope boundaries, failure behaviour, and success checks.
4. Resolve unambiguous references and project conventions from the available context.
5. Use a sensible assumption when it is cheap to reverse and does not alter the substance of the task.
6. Ask one question when no safe assumption exists. After the answer, check whether another material ambiguity remains.
7. Return a prompt that reads cold. Do not refer to "our discussion" or information outside the prompt.

## Ask useful questions

Ask about decisions such as:

- which input, file, directory, system, or audience is in scope
- what output must exist, where it belongs, and whether it may overwrite anything
- required behaviour for bad input, missing data, network failure, or partial success
- tradeoffs that change product behaviour, security, compatibility, cost, or architecture
- the observable result or check that proves completion

Do not ask about cosmetic choices, conventions the repository answers, details already supplied, or preferences with an obvious low-risk default.

Use this shape:

```text
Question: <one decision>
Recommendation: <answer> because <short reason>.
```

## Write the final prompt

Include only what changes execution:

- goal
- relevant context and current state
- exact inputs and outputs
- in-scope and out-of-scope work
- constraints and safe assumptions
- required failure behaviour
- success criteria and verification

Prefer positive instructions. Resolve contradictions or state which instruction wins. Use numbered steps only when order matters. Add `[NEEDS: <detail>]` only when the missing value cannot be safely assumed and the user has asked you to stop interviewing.

Return:

```text
Final prompt:

<self-contained prompt>

Assumptions: <only material defaults; omit when empty>
Gaps: <only unresolved [NEEDS: ...] items; omit when empty>
```

Do not solve the prompt, explain the rewrite, or offer a menu of next actions unless the user asks.
