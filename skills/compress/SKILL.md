---
name: compress
description: "Shorten a prompt, specification, plan, skill, note, or brain dump without changing its meaning or behaviour. Use when asked to compress, shorten, simplify, tighten, remove repetition, or use fewer tokens. Preserve facts, constraints, examples, edge cases, and checks that affect the result."
---

# Compress

Shorten the input without losing meaning.

Use this for information and instructions, not ordinary prose polishing. Use `deslop` when voice and writing quality are the main problem.

## Process

1. Identify the purpose and intended reader or agent.
2. Extract the required content: facts, actions, inputs, outputs, constraints, defaults, examples, edge cases, checks, and stop conditions.
3. Remove repetition, throat-clearing, backstory, generic advice, motivational language, and structure that does not change understanding or behaviour.
4. Replace vague phrases with a concrete instruction only when the source supports it. Otherwise cut them.
5. Merge overlapping rules and place each fact once, where the reader needs it.
6. Rewrite in plain words and the smallest structure that preserves the logic.
7. Compare the result with the source. Restore anything whose removal changes the likely interpretation or outcome.

## Keep

- facts, numbers, names, paths, commands, schemas, and citations
- explicit scope, priorities, and exceptions
- requirements created by past failures
- defaults that resolve real ambiguity
- examples that define a format or expose an edge case
- verification, failure behaviour, and stop conditions
- useful voice when compressing a brain dump or note

## Cut

- repeated goals, summaries, and conclusions
- obvious preambles and narration about the document
- baseline advice such as "be thorough" or "use good judgement"
- adjectives such as "robust," "polished," and "production-ready" without a test
- hedging that does not change confidence or responsibility
- examples that merely repeat the rule
- headings, bullets, or steps that add shape but no meaning
- synonyms for a term already named clearly

## Test every cut

Ask: if this disappears, could a capable reader act differently or lose a fact, limit, decision, warning, or piece of voice?

If no, cut it. If yes, keep it or rewrite it more clearly.

Return only the compressed result unless the user asks for a summary of changes.
