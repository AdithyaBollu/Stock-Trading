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

## Week ending 2026-05-15
### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $9,934.98 (Fri 5/8 EOD = Mon 5/11 AM) |
| Ending portfolio | $9,945.20 |
| Week return | +$10.22 (+0.10%) |
| S&P 500 week | ~+0.5% (5/8 close 7,398.93; 5/15 close uncertain in cited data — Yahoo Finance Fri headline noted index sank into close, Mon-Wed run = green through CPI; estimate from triangulated daily closes) |
| Bot vs S&P | ~-0.40% |
| Alpha sleeve deployed | $2,635.94 (26.5% of portfolio) vs 70–75% target |
| Niche sleeve deployed | $0 (0% of portfolio) vs 20–25% target |
| Trades | 1 (W:0 / L:0 / open:3 carryover→ now AAPL/CSCO/GOOGL) vs 15/week limit |
| Win rate | N/A (no closed trades) |
| Best trade | N/A closed; best unrealized GOOGL +7.18% |
| Worst trade | N/A closed; worst unrealized CSCO -0.34% |
| Profit factor | N/A (no closed trades) |
| Phase P&L | -$54.80 (-0.55% vs $10k baseline) |

### Closed Trades
| Ticker | Sleeve | Entry | Exit | P&L | Notes |
| — | — | — | — | — | None closed this week — first zero-realized-loss week since launch |

### Open Positions at Week End
| Ticker | Sleeve | Entry | Close | Unrealized | Stop |
| AAPL | alpha | $284.74 (5/1) | $300.08 | +$46.02 (+5.39%) | $272.88 trail GTC (HWM $303.20) |
| CSCO | alpha | $118.3175 (5/14) | $117.91 | -$3.26 (-0.34%) | $106.956 trail GTC (HWM $118.84) |
| GOOGL | alpha | $369.67 (4/30) | $396.21 | +$53.08 (+7.18%) | $363.33 trail GTC (HWM $403.70) |

### What Worked
- Trail GTCs continued to do all the work: zero manual cuts, zero overrides, AAPL trail auto-advanced multiple times intraweek on fresh HWMs ($300.92→$303.20) and GOOGL trail bumped to $363.33 on Wed's $403.70 HWM print
- First zero-realized-loss week since launch — both legacy winners (GOOGL +7.18%, AAPL +5.39%) carried into Friday close, phase P&L improved from -$87.94 (Mon EOD) to -$54.80 (Fri EOD)
- No-chase discipline held on Mon-Wed: AMD post-blow-off, AMAT pre-print, AMZN tier-2 all rejected — playbook gates intact through CPI (Tue) and CSCO/BABA/AMAT prints
- CPI Tuesday navigated without forcing an entry — sleeve light by design through the binary print, then capital partially redeployed on confirmed beat-and-raise (CSCO) Thursday
- Daytrade count reset to 0/5 rolling for the weekend — full PDT slate available for any defensive cut Mon

### What Didn't Work
- **CSCO fill discipline broke the playbook**: pre-market plan said size at the ~$98-100 pullback target zone with explicit "SKIP if ARM-style sell-the-news fade" gate, but the market-open agent filled at $118.3175 (near the intraday HOD of a +13% gap) — chased the gap rather than waiting for the pullback-on-reclaim structure; closed -0.41% from entry, the only red position into the weekend
- Sleeve under-deployed at 26.5% vs 70-75% target — **fourth consecutive week** below 30%, the pattern is now signal not noise: either no-chase rule is too restrictive on the available tape, OR idea-generation is too narrow
- Niche sleeve still empty (0%) — **fourth consecutive week** without a single 2.5:1 R:R idea clearing the bar; the prior weekly review flagged this as a remediation item but the pre-market routine has not yet been updated with an explicit niche screen
- Underperformed S&P by ~-0.40% on the week — concentration in 3 names with one being a fresh chase entry that's underwater
- May 12 (Tue) EOD snapshot was missed — process gap in daily logging, recovered via Alpaca last_equity baseline on Wed
- AMAT post-print drift Friday was skipped — defensible after the CSCO chase lesson, but raises the question whether playbook gates are now reflexively rejecting alpha-tier post-earnings setups

### Key Lessons
- **Post-earnings drift entries on alpha-tier names still require the pullback-on-reclaim gate** — CSCO is the lesson: a +13% gap with no pullback is the same chase pattern that AMD has presented for 3 weeks; the size-down-to-event-week cap is necessary but not sufficient — entry timing must wait for structure or the entry is forfeit
- The 10% trailing stop and -7% manual cut continue to be the system's strongest component — zero manual cuts needed in 5 days across 3 positions while both legacy winners extended drift
- **Sleeve under-deployment is now a 4-week structural pattern**, not transient: the no-chase rule is correct but the sleeve gap (~50pts below the 70-75% target every week) needs a deliberate counter-policy — either widen the eligible-setup definition OR accept that this strategy is fundamentally a "wait for A+" approach that will spend long stretches in cash
- **Niche sleeve dormancy is now critical**: 4 weeks of zero niche, two prior review cycles flagged it as a remediation priority, and the pre-market routine still has no formal niche screen. This is a process gap, not a market-availability gap
- Phase P&L recovered ~$33 this week without any closed wins — proves the legacy book (GOOGL Q1 PEAD + AAPL Q2 PEAD) is doing the work; protecting these drifts via trail is the highest-value action right now

### Adjustments for Next Week
- KEEP: 10% trail GTC, -7% manual cut, no-chase pullback-on-reclaim gate, lastday_price verification, position sizing caps, daily EOD snapshot discipline (close the Tue gap)
- TIGHTEN: For post-earnings drift entries, market-open agent must verify (a) gap-up-then-pullback structure is present in the first 15 min, AND (b) fill price is within $1 of the research plan's pullback target zone, OR explicitly downgrade the entry to "watchlist only" — CSCO Thu was a chase that the gate should have caught
- ADD (mandatory next week): pre-market routine must produce an explicit niche-sleeve candidate list each session — FDA calendar, small-cap breakout scan, mid-cap post-earnings drift screen — even if every candidate is "skip", the screen must run. Four weeks of empty niche without a documented screen is procedurally indefensible
- HOLD AAPL/CSCO/GOOGL into Mon — GOOGL **Google I/O 5/19-20** is the dominant near-term catalyst; do NOT pre-emptively trim, do NOT add (already 8% from entry, +15% trail-tighten trigger requires close ≥$425.12)
- CSCO close-watch: -7% manual cut line is $110.04; below that on volume = manual cut. Above $118 reclaim = thesis confirming
- Re-arm AMD watchlist for Mon-Tue only on a clean Day 5+ pullback structure (not the chaotic chase tape that has dominated 3 weeks)
- Re-evaluate sleeve deployment policy if Week 5 is again below 30% despite Google I/O catalyst — that would be 5 straight weeks of structural under-deployment and the strategy tuning case becomes urgent

### Overall Grade: C+
Week return +0.10% vs S&P ~+0.5% (-0.40% relative), 0 closed trades, 1 questionable entry (CSCO chase, now -0.34%). But: first zero-realized-loss week since launch, phase P&L recovered ~$33, both legacy PEAD winners extended their drift (GOOGL +7.18%, AAPL +5.39%), trail GTCs auto-managed every position, no manual overrides, no panic. Discipline B+ (CSCO fill is the demerit), P&L C, trend B. Slight upgrade from last week's C — the system is producing on the held book, but the entry-side discipline slipped on CSCO and the 4-week sleeve under-deployment + 4-week empty niche sleeve pattern is now urgent. If Week 5 (with Google I/O catalyst arriving) doesn't see either (a) sleeve deployment crossing 40% on a clean setup, or (b) a niche sleeve entry from an explicit screen, the strategy tuning conversation moves to mandatory.
