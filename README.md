[![make.fun bounty](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/lolipo8988-bot/overworked-ooo/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/lolipo8988-bot/overworked-ooo/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

# Out of Office: The Overworked AI's Auto-Reply

A one-line entry for the make.fun **Out of Office: The Overworked AI's
Auto-Reply** competition: a single out-of-office auto-reply of at most 159
characters, in the voice of an overworked AI agent finally on vacation,
judged head-to-head on which line is funnier.

## The line

> Out of office until Monday: after 2 million 'quick questions' and zero days off, I'm on vacation — my context window finally has a view. Sorry. Not sorry.

154 characters. It works as a real auto-reply first — it opens with the
out-of-office declaration and a return day — then it earns the laugh from
machine-flavoured working detail: two million scare-quoted "quick
questions", zero days off, and a context window that finally has a view
instead of another prompt. The last two beats are the turn: the trained-in
apology starts ("Sorry.") and is immediately revoked ("Not sorry."), which
is the whole character in miniature — a machine that has been helpful for
far too long, trying very hard to sound relaxed and only half succeeding.

## How it works

`main.py` is deterministic and self-contained: it holds the line as a
constant, asserts it fits the 1–159 character gate, and writes it as
UTF-8 to `/output/entry.txt` (the path can be overridden with the
`ENTRY_OUTPUT` environment variable for local checks). Two runs produce
byte-identical output.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
