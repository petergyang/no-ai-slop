# Contributing

Keep changes small and easy to review.

Good changes usually do one of these:

- Clarify an existing rule in `skills/no-ai-slop/SKILL.md` without changing its behavior.
- Add a missing example for a pattern already in `skills/no-ai-slop/SKILL.md`.
- Add a new pattern with a clear smell, a plain fix, and a short before/after example.
- Update `skills/no-ai-slop/eval.md` when the skill behavior changes.

Before opening a PR, check:

- Does the change preserve the writer's voice instead of making every draft sound polished?
- Does it avoid guessing whether AI wrote something?
- Does detect mode still return pattern evidence, not a rewrite or score?
- Does the README stay short enough for new users to understand quickly?
- Does the PR avoid unrelated cleanup?

If you add a pattern, include the smallest useful example. One sharp example beats a long list.
