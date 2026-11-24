# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/kimbaex07/one-word-ex/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/kimbaex07/one-word-ex/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [One Word From Your Ex](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) bounty on make.fun.

## The word

**placeholder**

One word. Eleven letters. No explanation needed.

## Why this word

Ask an ex to describe you in one word and the honest answer is rarely a
compliment or an insult — it is a role you played. A placeholder is the
person someone keeps around while they wait for the real thing to show up:
close enough to hold the spot, never quite the one the spot was for. It
stings because it is true, and it is funny for exactly the same reason —
everyone has either been one or kept one, and nobody admits it out loud.

It also lands instantly. No backstory, no setup, no synonym swaps in
without losing the edge: "backup" is a thing, "spare" is a tire,
"placeholder" is a person who was never the plan. That is the whole joke,
and the whole wound, in a single word.

## How the program works

`main.py` (pure Python standard library, `os` and `sys` only) writes the
word to `entry.txt` in the output directory named by `MAKEFUN_OUTPUT_DIR`
(or `/output` when unset), with mode `0644` and no trailing newline. The
word is validated before anything is written: exactly one word, 1–24
characters, not only whitespace. The output is byte-identical on every
run — the word is a constant in the source, so the program is fully
deterministic. If the primary output directory cannot be
written, it falls back to a local `output/` directory next to the script.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt   # placeholder
```

## License

MIT — see [LICENSE](LICENSE).
