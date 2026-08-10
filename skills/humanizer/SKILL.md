---
name: humanizer
description: "Rewrite any writing so it sounds clear, human, and plain. Use for landing pages, emails, docs, posts, scripts, lessons, prompts, and messages with AI slop, purple prose, cliches, em dashes, hype, vague claims, or over-polished language."
user-invocable: true
argument-hint: "<text, file path, or draft to humanize>"
---

# Humanizer

Rewrite any writing in plain English.

Use for:

- landing pages
- sales copy
- emails
- docs
- lessons
- scripts
- posts
- prompts
- notes
- product copy

## Process

1. Read the input.
2. Identify what the writer means.
3. Remove AI slop, purple prose, cliches, hype, and fake depth.
4. Rewrite with simple words, concrete nouns, and natural rhythm.
5. Run the checks.
6. Return only useful output.

## Rules

- Write for the intended reader. If the audience is not clear, assume an intelligent beginner.
- Lead with the main point.
- Simplify the language, not the idea.
- Put one main idea in each sentence.
- Explain ideas in the order the reader needs them.
- Prefer plain words, but keep precise technical terms.
- Define a term when it might be unfamiliar to the intended reader.
- Use a real example, or clearly say when an example is made up. Never use a made-up example as proof.
- Remove detail that does not help the reader understand or act.
- Keep important facts, limits, and warnings.
- Never make the writing childish, vague, or inaccurate.
- No em dashes.
- No purple prose.
- No cliches.
- No slogan endings.
- No fake depth.
- No invented proof, numbers, stories, or results.
- Use the user's voice sample when present.
- Use short, normal words.
- Prefer concrete nouns: email, task, note, file, meeting, customer, invoice, reply.
- Prefer concrete verbs: get, make, ask, send, read, write, save, run, check.
- Keep real opinions. If proof is missing, soften the claim or mark it unknown.
- Do not use "unlock", "elevate", "supercharge", "transform", "leverage", "seamless", "robust", "holistic", or "game-changing".
- Do not use "let's dive in", "here's the thing", "the real question is", "at its core", or "in today's fast-paced world".
- Avoid "stop X, start Y" and "not just X, but Y" unless the line says something concrete.

## Slop Patterns

| Pattern | Watch for | Fix |
|---|---|---|
| Tidy contrast | Stop X. Start Y. Not just X, but Y. | Say the actual action or result. |
| Fake depth | The real shift is. The deeper truth is. At its core. | State the point in normal words. |
| Purple prose | profound, breathtaking, vibrant, rich, nestled, tapestry | Replace mood with facts. |
| Abstract nouns | transformation, potential, impact, alignment, innovation | Name the thing the reader can picture. |
| Vague magic | unlock, elevate, empower, supercharge, 10x | Say what changes in the user's day. |
| Marketing negation | Not a toy. Not a demo. Not a prompt pack. | Show what the person will have. |
| Grand claim | This changes everything. The future is here. | Make the claim smaller and specific. |
| Persona fog | AI operator, business OS, agentic workflow | Define it with examples or cut it. |
| Motivational rhythm | short punchy line, short punchy line, profound closer | Use natural sentences. |
| Empty outcome | save time, work smarter, get more done | Name the saved task or decision. |
| Condescending opener | Most people do not realize. What people miss. | Start with the point. |
| Chatbot scaffolding | Great question. Certainly. I hope this helps. | Cut it. |
| Fancy verb | serves as, stands as, represents, showcases | Use is, has, uses, shows. |
| Vague source | experts say, many believe, studies show | Name the source or cut it. |

## Checks

- Can the reader picture it?
- Does it say what they will have, do, see, or decide?
- Could the intended reader understand it without needless effort?
- Is the language simple while the meaning stays accurate?
- Is each term that might be unfamiliar to the intended reader explained in plain words?
- Would a real person say it out loud?
- Did vague value become a concrete example?
- Is there any slogan rhythm left?
- Are there any em dashes?

## Examples

Bad:

> Stop prompting from scratch. Start delegating real work.

Better:

> Instead of explaining your whole situation every time, give the assistant a job: check my calendar, read my notes, draft the follow-up, and tell me what needs my attention.

Bad:

> Not a toy chatbot. Not another prompt pack. Not AI productivity tips.

Better:

> By the end, you will have an assistant running. You can message it. It can read your workspace. It can follow written skills. It can draft work for you to review.

Bad:

> Unlock the power of AI agents.

Better:

> Give the assistant one job, such as preparing your day each morning. Then give it the files, tools, and rules it needs to do that job without you explaining everything again.

## Output

Default:

1. `Rewrite:` improved text.
2. `Changed:` 2 to 4 short notes, only if useful.

When asked why text is bad:

1. `Pattern:` main issue.
2. `Why it fails:` one plain sentence.
3. `Rewrite:` improved text.
