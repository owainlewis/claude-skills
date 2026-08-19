---
name: explain-visually
description: "Build a self-contained, responsive HTML page that explains a concept, system, change, or decision with accurate writing and diagrams. Use when asked to visualize, diagram, or explain a repository, architecture, specification, pull request, process, or technical idea as an HTML page."
---

# Explain visually

Build an HTML page that explains a concept with text, examples, and diagrams.

## Understand the source

1. Read the relevant source material.
2. Identify the audience, main point, components, sequence, decisions, tradeoffs, and useful next action.
3. Separate verified facts from assumptions. Do not invent missing behaviour.
4. Choose the relationships that are easier to explain with a visual.

## Shape the explanation

Lead with the answer. Use a small number of sections. Each section should explain one part.

Use concrete titles. Define jargon before using it. Prefer real names, paths, commands, interfaces, states, and observed behaviour to generic labels.

Include a before-and-after, sequence, comparison, hierarchy, or state change only when the source supports it. End with what the reader should do next. Do not repeat the summary.

## Build the artifact

- Create one self-contained HTML file unless the user requests another structure.
- Use semantic HTML, inline CSS, and inline SVG. Avoid runtime dependencies unless the project already provides them or the user asks for them.
- Choose colours, fonts, and layout that fit the subject. Do not reuse the same palette, font pairing, dashboard, or slide template by default.
- Use responsive type and spacing. Let mobile sections grow naturally instead of preserving a desktop aspect ratio.
- Use SVG for flows, relationships, states, and architecture. Use HTML and CSS for comparisons, timelines, cards, and annotated examples.
- Keep labels short and place the explanation beside the visual.
- For three or more components, build the diagram in stages. Redraw the previous state and add one component at a time.
- Add interaction only when it teaches something, such as changing an input, revealing a state, or comparing two cases.
- Make controls keyboard accessible and give meaningful graphics a text equivalent.

Do not add charts, gradients, icons, or motion unless they help explain the source material.

## Verify

Open the artifact in an available real browser or renderer and inspect it at desktop and narrow mobile widths.

Check:

- no clipped, overlapping, or overflowing text
- readable type and diagram labels at each width
- visible focus states and keyboard-operable controls
- sufficient contrast and reduced-motion behaviour where animation exists
- no console errors, missing assets, or failed network requests
- every factual claim is supported by the source

Fix defects before returning the file. If no browser or renderer is available, state that you did not verify the layout.

Return the artifact link and a short note naming the source and widths checked. Do not narrate the build process.
