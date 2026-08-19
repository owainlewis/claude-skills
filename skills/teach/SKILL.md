---
name: teach
description: "Create tutorial content that helps the intended reader understand and use an AI or technical concept. Use for course lessons, technical articles, video scripts, workshops, standalone tutorials, educational newsletters, and course outlines. Explain how it works in plain language, show a worked example, and give the reader practice or a next step."
---

# Teach

Turn a topic into a tutorial that explains how something works or teaches the reader how to do it.

Treat every output as a tutorial. Apply the same teaching rules to course lessons, technical articles, workshops, video scripts, and newsletters.

Write for an intelligent beginner unless the user defines another audience. Do not talk down to them. Explain assumed steps and unfamiliar terms.

## Frame the tutorial

1. Infer the learner, what they already know, and why they need this.
2. Choose one thing they should understand, decide, build, or troubleshoot after the tutorial.
3. Narrow a broad topic until it fits the requested format and length.
4. Decide what the learner must know first. Teach or state that prerequisite before relying on it.
5. Exclude interesting material that does not support the outcome.

If the audience or outcome is missing and different choices would produce different tutorials, ask one question. Otherwise use a sensible assumption and proceed.

## Use a concrete title

Name the question, mechanism, decision, or result. Prefer a concrete noun and verb.

- Weak: "Understanding AI agents"
- Better: "How an AI agent decides which tool to call"
- Weak: "A deep dive into RAG"
- Better: "How RAG finds context before the model answers"
- Weak: "The future of prompting"
- Better: "When a prompt needs an example"

Reject titles that merely name a field or promise depth.

## Build the lesson

1. Open with a problem, decision, or result the learner can recognise.
2. Give the smallest complete explanation of what the thing is and when it is useful.
3. Explain the mechanism in the order it happens. Name the actor, action, input, output, and limit.
4. Define each new term in plain English before depending on it. Use one name for the same thing throughout.
5. Walk through one realistic example completely.
6. State the general rule after the learner has seen it work.
7. Close the most likely wrong conclusion, edge case, or limitation.
8. Give the learner a useful next action. For applied lessons, include a small exercise and a way to check the result.

Do not print this structure as boilerplate headings. Choose headings that state what each section teaches.

## Explain plainly

- Explain how it works. Do not substitute a metaphor, label, slogan, or list of features.
- Use common words without making the idea childish or vague.
- Keep one main idea in each paragraph.
- Prefer short sentences, but keep the detail that makes the idea click.
- Show commands, code, prompts, outputs, or before-and-after examples when the learner needs to see the action.
- State where an analogy stops matching the real system.
- Mark invented examples as examples, not evidence.
- State uncertainty. Do not present an uncertain claim as a fact.
- Do not add motivational filler, rhetorical quizzes, or a summary that repeats the tutorial.

## Use visuals to teach

Use a diagram or table only when it makes a relationship easier to understand.

For three or more components, build the picture in stages. Show the first relationship, redraw it with one addition, then add the next. A crowded all-at-once diagram is reference material, not teaching.

Keep labels short. Explain the mechanism in the prose around the visual.

## Design a course

When the request covers several lessons:

1. State what the learner should be able to do at the end.
2. Work backwards to the knowledge and skills it requires.
3. Order lessons by prerequisite, not by prestige or novelty.
4. Give each lesson one result the learner can demonstrate, one worked example, and one application.
5. Use later lessons to combine earlier skills instead of reteaching them with new jargon.
6. End with a project or decision that shows what the learner can now do.

## Match the format

- Course lesson: state what the learner should be able to do, then include the explanation, worked example, practice, and completion check.
- Technical article or newsletter: earn attention with a concrete problem, teach the mechanism, and end with a useful application.
- Video script: write for speech, make transitions explicit, and pair each visual beat with the idea it reveals.
- Workshop: alternate short explanations with guided action and visible checks.
- Standalone tutorial: state prerequisites, provide exact steps, show expected results, and cover likely failure points.

## Final check

- Does the title promise a specific result or answer a real question?
- Can the learner explain what this is, how it works, and when to use it?
- Did every term appear after its plain explanation?
- Did the example show how it works?
- Can the learner take the next step without filling in hidden gaps?
- Did any sentence sound knowledgeable without teaching anything?

Return the tutorial itself, not a report about how it was made.
