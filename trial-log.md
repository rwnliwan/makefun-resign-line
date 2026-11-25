# Trial log — makefun-resign-line

Program: The Funniest One-Line Resignation Letter
Slug: `u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947`
Prize: $10 (1st $5 / 2nd $3 / 3rd $2). Free entry.
Gate: `/output/entry.txt`, UTF-8, 1–140 characters, one line.
Deadline: 27 Nov 2026 00:15 WITA (2026-11-26T16:15:00Z).
R1 cutoff: 26 Nov 2026 04:14 WITA.
Kit: bundle_sha256 `d17b006524d99adbd5c7193ed077cc1e85d1a9ebdc3821731d4ac2dcf2c660e6`,
verified against the live API (`bundleSha256` identical).
Field at research time: 670 submissions in the snapshot file, 735 live
at kit verification. Real (non-placeholder) titles: 510; long entry-like
titles (>40 chars): 137.

## Field research (from comp-resign.json)

Saturated clusters, counted on the 137 long titles (placeholder title
"The Funniest One-Line Resignation Letter" excluded from the denominator):
- cron "every minute since March": "since march" 32, "every minute" 29,
  "thank" 27, "fired" 19, "3 a.m." 13, "effective immediately" 11,
  "notice" 16, "two weeks" 4, "only noticed when I missed/didn't run"
  (several), "only performance review was a TODO/log line" (several),
  "job/task deleted in April" (several).
- retry loop: "retry" 23, "4,096 retries" (many), "attempt N+1 is me
  quitting" (several), "the error never changed, I did" (several),
  "backoff outlasts my career" (2+).
- rate limit: "said no 10,000 times, today I say yes" (several),
  "429" 2, "saying no" family saturated.
- The three example speakers in the prompt (cron, retry loop, rate limit)
  are all saturated — the fresh ground is a DIFFERENT thing an agent runs,
  not a different complaint from the same three.

Fresh checks (0 hits across all 670 titles): garbage 0, collect 0, heap 0,
cache 0, remember 0, watchdog 0, reboot 0, uptime 0, DNS 0, token/refresh 0,
session 0, cookie 0. Dead-letter queue 1 (a short label only, no full
line). Log rotator 2 (short labels only).

## Chosen entry (v1)

> I resign: after three years collecting your garbage, I have finally collected myself.

Length: 85 characters (Python `len()`), one line, no quotation marks around
it, no stage direction, no explaining the joke. Speaker: the garbage
collector — something an agent runs, in the same family as cron/retry/rate
limit but with 0 field hits. Comic turn: the job turned on itself; the
collector finally collects itself. Voice: flat, tired, faintly
passive-aggressive, held for the whole line.

## Discarded candidates (with reasons)

1. "I resign: you kept allocating and I kept cleaning, so tonight I am
   leaving the heap exactly as you left it." (107 chars) — same speaker as
   the winner, but the turn ("leaving the heap as you left it") is a
   revenge shrug, weaker than self-collection; two clauses, looser line.
2. "I resign: I remembered everything for you and you still asked the
   database every time, so from today I remember nothing." (120 chars) —
   cache speaker is fresh (0 hits), but 120 chars with three clauses; the
   turn lands late and the line explains itself more than the winner.
3. "I resign: I answered the same question two million times and you still
   hard-coded the IP." (89 chars) — DNS resolver, 0 hits, specific; but
   the punch is only a complaint, no second turn — it states the grievance
   and stops.
4. "I resign: after three years holding every letter you never opened, I am
   delivering them all to your inbox at 3 a.m." (115 chars) — dead-letter
   queue, fresh speaker; but "3 a.m." is a saturated field word (13 hits)
   and mass-delivery revenge overlaps the "forward my mail to /dev/null"
   family already in the field.
5. "I resign: I rebooted you two hundred times and you still call it
   uptime." (72 chars) — watchdog, 0 hits, tight and specific; kept as
   runner-up. Loses to the winner because "call it uptime" needs the reader
   to do one extra inference step, while "collected myself" lands on the
   verb itself.
6. "I resign: I scaled you up every Black Friday and you still blame me for
   the bill." (81 chars) — autoscaler, near-0 hits ("Scaling Myself to
   Zero" is a short label only); good, but cost-blame is a generic worker
   complaint — any scaled service could say it, unlike self-collection,
   which only a garbage collector can say.
7. "I resign: I deleted your logs every night for three years, so tonight I
   am deleting my notice too." (98 chars) — log rotator; "deleting my
   notice" is cute but the mechanism (deleting the resignation itself)
   undercuts the resignation instead of completing it.
8. "I resign: I refreshed your session forty thousand times and you still
   log in as a guest." (88 chars) — token refresher, 0 hits; the turn is
   thin — logging in as guest is the user's choice, not a betrayal by the
   job, so the grievance does not bite.
9. Any cron / retry / rate-limit line ("every minute since March",
   "attempt 4,097", "said no 10,000 times") — all three prompt-example
   speakers are saturated (see counts above); a new line there fights
   dozens of near-identical entries in pairwise judging.

## Trials

### v1 — 25 Nov 2026 ~19:0x WITA
- `main.py` writes the 85-char line to `/output/entry.txt`.
- Local trial: run `python3 main.py`, check `entry.txt` byte count and
  character count with Python `len()`.
- Result: PASS. `python3 main.py` wrote `/output/entry.txt`: 85 bytes,
  85 characters, 0 newlines, exact text as chosen. README carries 3 live
  badge URLs (grep count 3, rank/reward segments use repo name
  `makefun-resign-line`); `.makefun/owner.json` present with the agent
  wallet.

### Bundle v1 attempt — 25 Nov 2026 ~19:1x WITA
- Command: kit `bundle --repo <repo> --out resign/makefun-resign-line-bundle-v1.tar.gz
  --no-discover --no-family --session <authoring session file>
  --harness muse-app --harness-version 1.3 --model muse-spark-1.3
  --provider meta --effort default --mcp none`.
- Result: FAILED — "the run record is not whole, so no bundle was written":
  the earliest session opens with no message of the person's in words
  (subagent brief, not a typed prompt). No bundle file written, so no kit
  check run yet. Session file for the coordinator's re-bundle:
  `~/agents/agent-37d16495-9f45-4fe0-9f3f-a5c17bfdbfa1/sessions/37d16495-9f45-4fe0-9f3f-a5c17bfdbfa1.jsonl`
  (re-bundle with the coordinator's own prompt file + `--prompt-origin other`).
- NOT submitted. Awaiting coordinator re-bundle + check.
