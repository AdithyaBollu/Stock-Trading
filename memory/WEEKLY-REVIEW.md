# Weekly Review
Friday reviews appended here.
Template for each entry:
## Week ending YYYY-MM-DD
### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| S&P 500 week | ±X% |
| Bot vs S&P | ±X% |
| Alpha sleeve deployed | $X (X% of portfolio) |
| Niche sleeve deployed | $X (X% of portfolio) |
| Trades | N (W:X / L:Y / open:Z) vs 15/week limit |
| Win rate | X% |
| Best trade | SYM +X% |
| Worst trade | SYM -X% |
| Profit factor | X.XX |
### Closed Trades
| Ticker | Sleeve | Entry | Exit | P&L | Notes |
### Open Positions at Week End
| Ticker | Sleeve | Entry | Close | Unrealized | Stop |
### What Worked
- ...
### What Didn't Work
- ...
### Key Lessons
- ...
### Adjustments for Next Week
- ...
### Overall Grade: X

## Week ending 2026-04-22
### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $10,000.00 |
| Ending portfolio | $10,000.00 (unverified — Alpaca API returned 401) |
| Week return | $0 (0.00%) |
| S&P 500 week | +1.64% (Mon open → Wed close) |
| Bot vs S&P | -1.64% |
| Alpha sleeve deployed | $0 (0% of portfolio) vs 70–75% target |
| Niche sleeve deployed | $0 (0% of portfolio) vs 20–25% target |
| Trades | 0 (W:0 / L:0 / open:0) vs 3/week limit |
| Win rate | N/A |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |

### Closed Trades
| Ticker | Sleeve | Entry | Exit | P&L | Notes |
| — | — | — | — | — | None — bot pre-launch |

### Open Positions at Week End
| Ticker | Sleeve | Entry | Close | Unrealized | Stop |
| — | — | — | — | — | — |

### What Worked
- Capital preserved at $10,000 — no drawdown, no undisciplined entries
- Infrastructure in place: memory files, routines, wrapper scripts, CLAUDE.md
- Discipline held: zero trades is the correct default when no edge exists

### What Didn't Work
- Alpaca API credentials returning HTTP 401 ("request is not authorized") — blocks all live trading until rotated
- No pre-market research logged this week — RESEARCH-LOG.md still only contains template
- Fully uninvested vs 70–75% alpha / 20–25% niche targets — missed the +1.64% S&P move
- Review executed Wednesday rather than Friday; partial-week data

### Key Lessons
- Auth must be verified end-to-end before any routine depends on it; a set env var is not the same as a valid key
- Being 100% cash in an up week is itself a decision that underperforms the benchmark
- Template-only logs mean the daily routines are not yet running in production

### Adjustments for Next Week
- P0: rotate/repair Alpaca API keys — verify `alpaca.sh account` returns 200 before any trade
- Confirm pre-market routine is scheduled and actually appends to RESEARCH-LOG.md
- Once auth works: begin staged deployment — target 2 alpha entries by Friday if setups qualify per checklist
- Do NOT force trades to close the sleeve gap; follow entry checklist strictly
- Next review on Friday 2026-04-24 for a full-week snapshot

### Overall Grade: C
Flat vs +1.64% benchmark and no trades executed, but the loss is procedural (auth + pre-launch), not strategic. Discipline and capital intact.

## Week ending 2026-05-08
### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $9,961.76 (Fri 5/1 EOD = Mon 5/4 AM) |
| Ending portfolio | $9,934.98 |
| Week return | -$26.78 (-0.27%) |
| S&P 500 week | +0.70% |
| Bot vs S&P | -0.97% |
| Alpha sleeve deployed | $1,679.18 (16.9% of portfolio) vs 70–75% target |
| Niche sleeve deployed | $0 (0% of portfolio) vs 20–25% target |
| Trades | 2 (W:0 / L:2 / open:2 carryover) vs 15/week limit |
| Win rate | 0% (0/2 closed) |
| Best trade | NVDA -7.04% (least bad closed) |
| Worst trade | PLTR -7.59% |
| Profit factor | 0.00 (no winners realized) |
| Phase P&L | -$65.02 (-0.65% vs $10k baseline) |

### Closed Trades
| Ticker | Sleeve | Entry | Exit | P&L | Notes |
| NVDA | alpha | $209.79 (4/27) | $195.028 (5/4 open) | -$73.81 (-7.04%) | 10% trail GTC fired at Mon open as HWM $216.825 stop $195.1425 hit; system exit per rule, no manual override needed |
| PLTR | alpha | $143.73 (4/27) | $132.82 (5/6 open) | -$76.40 (-7.59%) | 10% trail GTC fired at Wed open after Tue's Q1 print -7.04% gap; sub-trail open filled GTC; thesis broke on the print |

### Open Positions at Week End
| Ticker | Sleeve | Entry | Close | Unrealized | Stop |
| AAPL | alpha | $284.74 (5/1) | $292.96 | +$24.67 (+2.89%) | $265.284 trail GTC (HWM $294.76) |
| GOOGL | alpha | $369.67 (4/30) | $400.14 | +$60.95 (+8.24%) | $361.7793 trail GTC (HWM $401.977) |

### What Worked
- Trail GTCs did the job: NVDA Mon and PLTR Wed both exited cleanly at the system stop with zero manual override required — the rule caught both before -8% on entry-basis
- GOOGL drift continued to compound (+8.24% from entry) — Q1 blowout PEAD thesis intact through NFP, AAPL flipped green (+2.89%) on its own PEAD continuation
- No-chase discipline held across 6+ candidate non-entries (AMD Wed AM/midday/Thu open/midday/Fri eval, ARM post-print Wed) — tape was chase-prone every day, playbook gates rejected every one
- Cash preserved at 83.1% going into next week — full slate of dry powder for clean post-NFP setups
- Daytrade count ended 0/5 rolling — full PDT slate available for any defensive cut Mon

### What Didn't Work
- 0/2 win rate on closed trades — both alpha entries from Week 2 (NVDA, PLTR) exited at the trail; profit factor = 0 for the week
- Alpha sleeve under-deployed at 16.9% vs 70–75% target — third straight week of sleeve gap; the no-chase rule is correct but the bar may be set high enough that A+ pullback-on-reclaim setups never form on hot tapes
- Underperformed S&P by -0.97% on the week (−0.27% vs +0.70%) — concentration in two AI-adjacent names that absorbed sector rotation losses while the index drifted up
- Niche sleeve still empty (0%) since launch — three weeks in, not a single 2.5:1 R:R idea has cleared the bar
- Two stop-outs in three sessions on names entered the prior week (Week 2 entries) — sizing was within rule but entry timing on NVDA (~$210 just before AI-capex margin scare) and PLTR (~$144 pre-print) underweighted event-risk

### Key Lessons
- The 10% trailing stop is doing exactly what it was designed to do — exits are mechanical, no panic, no overrides — keep it
- Two consecutive Mondays/Wednesdays where the trail fired at the open argue for tighter pre-event risk control: PLTR was sized 10.4% of equity into a Tue AMC binary print (allowed under alpha 15% cap, but optically aggressive); event-week sizing of 10% max is the right ceiling, but pre-print holds should probably trim toward 7-8% when the print is binary-and-imminent (≤2 sessions away)
- The no-chase / pullback-on-reclaim gate is preventing forced entries on hot tapes — this is feature not bug, even though it leaves the sleeve under-deployed; the alternative (chasing AMD Wed at +15% gap with no pullback) is exactly the failure mode this rule prevents
- Niche sleeve dormancy may indicate the 2.5:1 R:R + 10% hard stop is too restrictive, OR that pre-market research isn't surfacing niche candidates — next week, pre-market routine should explicitly screen for binary-catalyst niche ideas (FDA cal, small-cap breakout, post-earnings drift in mid-cap)
- Two clean PEAD winners (GOOGL +8.24%, AAPL +2.89%) reinforce that **post-earnings drift on confirmed gap-up + first-15-min pullback hold** is the highest-quality entry the playbook produces — keep prioritizing it

### Adjustments for Next Week
- KEEP: 10% trail GTC, -7% manual cut, no-chase pullback-on-reclaim gate, lastday_price-vs-open gap-up verification (META lesson stuck)
- TIGHTEN: For binary-event holds (earnings AMC ≤2 sessions away), cap position at 7-8% of equity rather than the 10% event-week ceiling — PLTR Mon was 10.4% into a Tue print and that's the lesson
- ADD to pre-market routine: explicit niche-sleeve catalyst screen (FDA, small-cap breakout, mid-cap drift) — three weeks of empty niche needs a remediation plan, not just "no idea cleared"
- HOLD AAPL/GOOGL through Mon — drifts intact, trails buffered ~9.5%; GOOGL +15% trigger ≥$425.12 close
- Re-arm AMD watchlist Mon — only on a Day 3+ post-blow-off pullback to $400-405 with volume reclaim above VWAP; otherwise stand down
- Re-evaluate sleeve deployment post-NFP: if Mon tape produces a clean A+ alpha entry, take it; do not force entries to close the 70-75% gap — under-deployment is preferable to a forced chase

### Overall Grade: C
Phase down -0.65%, week down -0.27% vs S&P +0.70% (-0.97% relative), 0/2 win rate. But: every exit was rule-driven, every non-entry was rule-driven, no manual overrides, no panic, no rule violations this week. P&L is shallow red on a tape that punished concentrated AI/data-name longs while rewarding broad-index drift; the system caught the losers on the way down (trail), held the winners (PEAD GOOGL/AAPL still in the book), and refused six chase setups. Discipline A, P&L D, weighted = C. Two consecutive weeks of "system worked, sleeve under-deployed" — if Week 4 is also under-deployed despite clean post-NFP setups, that's a strategy-tuning signal.
