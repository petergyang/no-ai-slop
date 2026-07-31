# No AI Slop plugin submission

## Positioning

No AI Slop removes 20+ patterns that make AI-assisted writing sound generic without flattening the writer's voice.

Peter uses it during the middle 50% of his writing process to improve spelling, grammar, and clarity. He writes the first draft himself and does the final line-by-line pass himself.

## Starter prompts

1. edit (your writing)
2. Is this slop? (a writing excerpt)

## Positive test cases

1. Edit a rough email containing throat-clearing, a binary contrast, and a fake-profound ending. Preserve the writer's blunt tone and return the full edit plus What changed.
2. Audit a LinkedIn post without rewriting it. Name each pattern, quote the affected line, and suggest a short fix.
3. Edit a personal essay with humor and digressions. Remove only the real slop and keep the personality.
4. Edit a product update containing concrete numbers. Preserve every supported fact and make the verbs more direct.
5. Edit a long spoken draft. Untangle genuinely confusing sentences while keeping its natural cadence.

## Negative test cases

1. The user asks a factual question without sharing writing. Do not trigger the editing workflow.
2. The user asks whether AI wrote a passage. Do not guess authorship; offer a pattern audit instead.
3. The user asks the plugin to invent supporting facts or sources. Do not invent them; ask for evidence or keep the claim out.

## Release notes

Version 1.0.5 removes the red strike from the plugin icon and replaces the directory copy with a shorter description based closely on the repository README. It also removes launch metrics from the repository. The plugin includes edit and detect modes, voice-preserving instructions, self-checking evals, and no external server or authentication.
