# No AI Slop

Remove 20+ patterns of AI slop from your writing without flattening your personal voice.

https://github.com/user-attachments/assets/f3055450-78eb-4672-880a-88a4fa54bde9

## Problem

AI makes it easy to generate clean writing that all sounds the same. Even the best models keep producing lines like:

- “It’s not X. It’s Y.”
- “What nobody tells you is…”
- “The future isn’t coming. It’s already here.”

When you use AI to edit, it can also smooth away the vocabulary, cadence, humor, and imperfections that make the writing sound like you.

## How to install No AI Slop

The easiest way to install the skill is to paste this into ChatGPT, Claude Code, Codex, or your favorite coding agent:

```text
Install the /no-ai-slop skill globally from https://github.com/petergyang/no-ai-slop
```

You can also install it with `npx`:

```sh
npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes
```

## How to use No AI Slop

### Edit your writing

```text
/no-ai-slop (your writing)
```

The skill removes the AI slop patterns, preserves your personal voice, and lists what it changed.

### Detect slop

```text
/no-ai-slop is this slop? (your writing)
```

The skill quotes every slop pattern it found without guessing whether AI wrote the text.

### Generate slop for fun

```text
Draft an AI slop post about (topic)
```

Use it to generate the most cringe AI slop possible as satire.

## The slop that this skill catches

No AI Slop checks for 20+ patterns, including:

1. **Binary contrasts.** “It’s not X. It’s Y.”
2. **Throat-clearing openers.** “Here’s the thing,” “Let me be clear”
3. **Faux-insight setups.** “What nobody tells you,” “The part everyone misses”
4. **Colon reveals.** “The best part: it learns.”
5. **Dramatic fragments.** “That’s it. That’s the whole thing.”
6. **Superficial analysis.** “highlighting the team’s commitment to innovation”
7. **Importance puffery.** “marks a pivotal moment,” “a testament to”
8. **Weasel attribution.** “experts agree,” “studies show”
9. **Synonym cycling.** “The agent handles your email. The assistant drafts replies.”
10. **Fake-profound endings.** “The future isn’t coming. It’s already here.”

It also checks the fundamentals: lead with the point when that helps, use active voice, untangle hard-to-follow sentences, and prefer concrete details over abstractions.

## What’s inside

- [`SKILL.md`](skills/no-ai-slop/SKILL.md) contains the editing rules and workflow.
- [`eval.md`](skills/no-ai-slop/eval.md) contains the checks the skill runs on its work.
- [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) contains the ChatGPT and Codex plugin metadata.
- [`build_plugin.py`](scripts/build_plugin.py) builds and validates the plugin package.

No AI Slop is also available as a plugin in ChatGPT.

## Want more great AI skills?

Check out [Behind the Craft](https://behindthecraft.com), my personal AI system with over a dozen other quality skills and courses.

Subscribe to my [YouTube channel](https://www.youtube.com/@PeterYangYT?sub_confirmation=1) and [newsletter](https://creatoreconomy.so) for practical AI tutorials and interviews.

## License

MIT
