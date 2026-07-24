# No AI slop

This skill removes 20+ patterns of AI slop from your writing and it can also help you detect slop as well.

## What it catches

The patterns it detects include:

| Pattern | Smells like |
|---------|-------------|
| Binary contrasts | "It's not X. It's Y." |
| Throat-clearing openers | "Here's the thing..." |
| Faux-insight setups | "What nobody tells you..." |
| Colon reveals | "The best part: it learns." |
| Superficial analysis | "...highlighting the team's commitment" |
| Importance puffery | "marks a pivotal moment" |
| Weasel attribution | "experts agree," "studies show" |
| Fake-strong verbs | "serves as a centralized hub" |
| Synonym cycling | the agent, then the assistant, then the tool |
| Negative listing | "Not a X. Not a Y. A Z." |
| Dramatic fragmentation | "That's it. That's the whole thing." |

It also enforces the fundamentals that make writing good: Lead with the point when it helps, use active voice, untangle hard-to-follow sentences, and prefer concrete numbers over abstractions.

## Install

Install a reviewed, immutable revision rather than the moving default branch. Paste this into Claude Code, Codex, or your favorite AI harness:

"Install this skill globally from [commit 61c21c351da4dcb40946a11fead978f2078a2c65](https://github.com/angelcontreras/no-ai-bs/tree/61c21c351da4dcb40946a11fead978f2078a2c65)."

## Use

**1. Edit a draft.** Paste it and invoke the skill:

```
/no-ai-slop

[your draft]
```

You get back the edited draft plus a short What changed section. The skill makes the minimum effective edit, then checks its own work against [eval.md](eval.md).

For legal, medical, financial, security, compliance, contractual, or public-policy content, it preserves facts, qualifications, citations, obligations, dates, numbers, and procedures. It flags substantive changes for approval. You can also ask for a suggestion-only review.

**2. Detect slop.** Ask whether a piece reads as AI:

```
/no-ai-slop is this AI slop?

[the text]
```

You get every pattern it found each with the quoted line.

## Files

1. `SKILL.md`: The editing rules and workflow.
2. `eval.md`: Pass/fail checks the skill runs on its own edits.

## Who made this

This fork is maintained at [angelcontreras/no-ai-bs](https://github.com/angelcontreras/no-ai-bs). It is derived from work by Peter Yang; the original MIT copyright notice remains in [LICENSE](LICENSE).

## License

MIT
