---
name: explain-visually
description: "Build a self-contained, responsive HTML explainer that teaches a concept, system, change, or decision through source-grounded writing and purposeful diagrams. Use when asked to visualize, diagram, or explain a repository, architecture, specification, pull request, process, or technical idea as an interactive or visual web artifact."
---

# Explain visually

Build an HTML artifact that makes one idea easier to understand than prose alone.

## Understand the source

1. Read the relevant source material.
2. Identify the audience, central claim, moving parts, sequence, decisions, tradeoffs, and useful next action.
3. Separate verified facts from assumptions. Do not invent behaviour to complete the story.
4. Choose the few relationships that genuinely benefit from a visual.

## Shape the explanation

Lead with the answer or mental model. Then show how it works through a small number of sections, each with one teaching job.

Use concrete titles. Define jargon before using it. Prefer real names, paths, commands, interfaces, states, and observed behaviour to generic labels.

Include a before-and-after, sequence, comparison, hierarchy, or state change only when the source supports it. End with the reader's next useful action rather than a repeated summary.

## Build the artifact

- Create one self-contained HTML file unless the user requests another structure.
- Use semantic HTML, inline CSS, and inline SVG. Avoid runtime dependencies unless the project already provides them or the user asks for them.
- Choose a visual language that fits the subject. Do not reuse a fixed palette, font pairing, dashboard shell, or slide template by default.
- Use responsive type and spacing. Let mobile sections grow naturally instead of preserving a desktop aspect ratio.
- Use SVG for flows, relationships, states, and architecture. Use HTML and CSS for comparisons, timelines, cards, and annotated examples.
- Keep labels short and place the explanation beside the visual.
- For three or more moving parts, reveal the model in stages. Redraw the previous state and add one part at a time.
- Add interaction only when it teaches something, such as changing an input, revealing a state, or comparing two cases.
- Make controls keyboard accessible and give meaningful graphics a text equivalent.

Do not decorate an explanation with unrelated charts, gradients, icons, or motion. A visual earns its place by reducing the reader's work.

## Verify

Open the artifact in an available real browser or renderer and inspect it at desktop and narrow mobile widths.

Check:

- no clipped, overlapping, or overflowing text
- readable type and diagram labels at each width
- visible focus states and keyboard-operable controls
- sufficient contrast and reduced-motion behaviour where animation exists
- no console errors, missing assets, or failed network requests
- every factual claim is supported by the source

Fix defects before returning the artifact. If no browser or renderer is available, say that visual verification remains outstanding.

Return the artifact link and a short note naming the source and widths checked. Do not narrate the build process.
