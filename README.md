# No AI slop

This skill removes 40+ patterns of AI slop from your writing and it can also help you detect slop as well.

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
| Anaphora | "Every tree, every field, every sign..." |
| Transformation pivots | "X becomes Y" / "X is turning into Y" |
| Parallel declarative stacks | Reorderable `[noun] [verb] [noun]` assertion grids |
| Abstract framing | "The problem was X." / "The key insight is..." |
| Forced optimism endings | "Despite these challenges, the future remains bright." |
| Hedging clusters | "arguably... in many ways... to some extent..." |

It also catches label sentences, stacked tail clauses, mixed-vehicle metaphors, noun-inventory subjects, point-announcing lead-ins, harder-question escalations, forced triads, comma-list overload, nominalization stacks, repetition disguised as development, automatic moral lessons, sanitized story arcs, generic specificity, chatbot tells, and unproved superlatives. See [SKILL.md](SKILL.md) for the full list.

It also enforces the fundamentals that make writing good: Lead with the point when it helps, use active voice, untangle hard-to-follow sentences, and prefer concrete numbers over abstractions.

## Install

Paste this into Claude Code, Codex, or your favorite AI harness:

"Install this skill globally: [https://github.com/petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)"

## Use

**1. Edit a draft.** Paste it and invoke the skill:

```
/no-ai-slop

[your draft]
```

You get back the edited draft plus a short What changed section. The skill makes the minimum effective edit, then checks its own work against [eval.md](eval.md).

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

This is one skill from my personal AI operating system. The full library, including my courses and workflows, lives at [Behind the Craft](https://behindthecraft.com).

## License

MIT
