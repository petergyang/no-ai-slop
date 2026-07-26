# No AI Slop plugin submission

## Positioning

No AI Slop removes 20+ patterns that make AI-assisted writing sound generic without flattening the writer's voice.

Peter uses it during the middle 50% of his writing process to improve spelling, grammar, and clarity. He writes the first draft himself and does the final line-by-line pass himself.

## Proof

- 2.7K+ GitHub stars as of July 26, 2026
- 611,392 X impressions
- 5,234 likes
- 10,519 saves
- 13,704 link clicks

Sources:

- https://github.com/petergyang/no-ai-slop
- https://x.com/petergyang/status/2079943830024188105
- https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns

## Starter prompts

1. Edit this draft without flattening my voice.
2. Flag the AI-slop patterns without rewriting.
3. Make this clearer and more direct while preserving my tone.

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

Initial skills-only release. Includes edit and detect modes, voice-preserving instructions, self-checking evals, and no external server or authentication.
