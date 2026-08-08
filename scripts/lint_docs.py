#!/usr/bin/env python3
"""Check the skill's own docs against the rules the skill enforces.

A style checker that breaks its own rules is the one kind of bug that costs it
credibility, and it is cheap to catch. This lints README.md, SKILL.md, and
eval.md for the subset of rules that can be checked mechanically, plus the
cross-reference integrity between SKILL.md and eval.md.

It deliberately does not try to evaluate editing quality -- that needs a model,
and `eval.md` is the checklist for it. This only catches the mechanical misses.

Usage: python scripts/lint_docs.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "no-ai-slop" / "SKILL.md"
EVAL = ROOT / "skills" / "no-ai-slop" / "eval.md"
README = ROOT / "README.md"
DOCS = (README, SKILL, EVAL)

# Short copy gets no em dashes; longer drafts tolerate 1-2 (SKILL.md).
EM_DASH_BUDGET = {README.name: 0, SKILL.name: 2, EVAL.name: 2}


def _lines(path: Path, skip_frontmatter: bool = False) -> list[tuple[int, str]]:
    """Numbered lines, optionally without the YAML frontmatter block.

    Frontmatter keys are `key: Value` by construction, so they trip the
    colon rule without being prose.
    """
    raw = path.read_text(encoding="utf-8").splitlines()
    out = list(enumerate(raw, 1))
    if skip_frontmatter and raw and raw[0].strip() == "---":
        end = next((i for i, l in enumerate(raw[1:], 1) if l.strip() == "---"), 0)
        out = out[end + 1:]
    return out


def _banned_words() -> list[str]:
    m = re.search(r"Banned outright:\s*(.+?)\.\s*$",
                  SKILL.read_text(encoding="utf-8"), re.M)
    if not m:
        raise SystemExit("lint: could not find the banned-word list in SKILL.md")
    return [w.strip() for w in m.group(1).split(",") if w.strip()]


def check_colon_case(fail) -> None:
    """SKILL.md: prefer sentence case after a colon unless grammar requires otherwise."""
    ok_after = re.compile(r"^(I|AI|GitHub|ChatGPT|Claude|Codex|MIT|SKILL)\b")
    # A colon may introduce a direct question or quotation; that is grammar,
    # not the "colon reveal" pattern the skill targets.
    introduces_speech = re.compile(
        r"\b(question|questions|ask|asks|prompt|quote|quotes|example|examples)\s*$", re.I)
    for path in DOCS:
        for n, line in _lines(path, skip_frontmatter=True):
            if line.lstrip().startswith(("http", "|", "```", "-  ")):
                continue
            for m in re.finditer(r":\s+([A-Z][a-z]+)", line):
                word = m.group(1)
                if ok_after.match(word):
                    continue
                if introduces_speech.search(line[:m.start()]):
                    continue
                # a proper noun or a title is fine; a plain word starting a
                # clause is the pattern the skill says to fix
                fail(f"{path.name}:{n}: capitalised '{word}' after a colon "
                     f"(SKILL.md prefers sentence case)")


def check_em_dashes(fail) -> None:
    for path in DOCS:
        count = path.read_text(encoding="utf-8").count("—")
        budget = EM_DASH_BUDGET[path.name]
        if count > budget:
            fail(f"{path.name}: {count} em dashes, budget is {budget}")


def check_banned_words(fail) -> None:
    """Banned words must not appear outside the list that defines them."""
    banned = _banned_words()
    for path in DOCS:
        for n, line in _lines(path):
            if "Banned outright:" in line:
                continue
            for word in banned:
                if re.search(rf"\b{re.escape(word)}\b", line, re.I):
                    fail(f"{path.name}:{n}: banned word '{word}'")


def check_pattern_coverage(fail) -> None:
    """Every bolded pattern in SKILL.md should be reachable from eval.md.

    Catches the drift where a rule is added or renamed in one file only.
    """
    skill_text = SKILL.read_text(encoding="utf-8")
    section = skill_text.split("## Patterns to cut", 1)[-1].split("## Workflow", 1)[0]
    patterns = re.findall(r"^\*\*(.+?)\.\*\*", section, re.M)
    eval_text = EVAL.read_text(encoding="utf-8").lower()
    for pat in patterns:
        # match on the distinctive head noun, so light rewording does not trip it
        key = pat.lower().split()[0].rstrip(",")
        if key not in eval_text:
            fail(f"eval.md: no check covers SKILL.md pattern '{pat}'")
    if not patterns:
        fail("SKILL.md: no bolded patterns found; has the format changed?")


def main() -> int:
    failures: list[str] = []
    fail = failures.append
    for check in (check_colon_case, check_em_dashes,
                  check_banned_words, check_pattern_coverage):
        check(fail)
    if failures:
        print("Docs do not satisfy the skill's own rules:\n", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"lint_docs: {len(DOCS)} docs satisfy the skill's own rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
