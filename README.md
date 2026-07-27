# No AI slop

This open-source skill removes 20+ patterns of AI slop from your writing without flattening your personal voice. It can also detect slop without guessing whether AI wrote the text.

More than 2,700 people have starred it on [GitHub](https://github.com/petergyang/no-ai-slop). The [launch post on X](https://x.com/petergyang/status/2079943830024188105) reached 611K impressions, 10K+ saves, and 13K+ link clicks.

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

I use it during the middle 50% of my writing process to improve spelling, grammar, and clarity. I write or dictate the first draft myself, use AI to edit, then do the final line-by-line pass myself. [Read the full 25/50/25 process.](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns)

## Install

Paste this into Claude Code, Codex, or your favorite AI harness:

"Install this skill globally: [https://github.com/petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)"

The repository also contains a skills-only plugin package for ChatGPT and Codex. Tagged releases attach a validated plugin ZIP, and the plugin is available in the public ChatGPT directory.

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
3. `.codex-plugin/plugin.json`: Metadata for the ChatGPT and Codex plugin.
4. `scripts/build_plugin.py`: Builds and validates the plugin ZIP from the canonical skill files.

## Who made this

This is one skill from my personal AI operating system. The full library, including my courses and workflows, lives at [Behind the Craft](https://behindthecraft.com).

## License

MIT
