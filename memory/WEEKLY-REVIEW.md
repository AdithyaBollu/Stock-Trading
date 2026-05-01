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

## Week ending 2026-05-01
### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $10,000.00 (Mon AM) |
| Ending portfolio | $9,960.57 |
| Week return | -$39.43 (-0.39%) |
| S&P 500 week | +0.56% (Fri 4/24 close 7,165.08 → Fri 5/1 close 7,205.33) |
| Bot vs S&P | -0.95% |
| Alpha sleeve deployed | $3,609.62 (36.2% of portfolio) vs 70–75% target |
| Niche sleeve deployed | $0 (0% of portfolio) vs 20–25% target |
| Trades | 6 (W:1 / L:1 / open:4) vs 15/week limit |
| Win rate | 50% (closed: 1W / 1L) |
| Best trade | GOOGL +4.15% (open); MSFT +$2.01 (closed) |
| Worst trade | NVDA -5.43% (open); META -$0.52 (closed) |
| Profit factor | 3.87 (closed only: $2.01 / $0.52) |

### Closed Trades
| Ticker | Sleeve | Entry | Exit | P&L | Notes |
| MSFT | alpha | $420.23 (3 sh) | ~$420.90 | +$2.01 | Round-trip Mon — pre-research violation (binary AMC event-week + 12.6% > 10% cap) |
| META | alpha | $605.38 (1 sh) | $604.86 | -$0.52 | Round-trip Thu — entered into a -9.5% gap-DOWN mistaken for "gap-up pullback"; cut per thesis-broken rule |

### Open Positions at Week End
| Ticker | Sleeve | Entry | Close | Unrealized | Stop |
| GOOGL | alpha | $369.67 (2 sh) | $385.00 | +$30.66 (+4.15%) | $348.06 trail GTC (HWM $386.74) |
| PLTR | alpha | $143.73 (7 sh) | $143.90 | +$1.17 (+0.12%) | $131.80 trail GTC (HWM $146.44) |
| AAPL | alpha | $284.74 (3 sh) | $280.11 | -$13.89 (-1.63%) | $258.50 trail GTC (HWM $287.22) |
| NVDA | alpha | $209.79 (5 sh) | $198.40 | -$56.95 (-5.43%) | $195.14 trail GTC (HWM $216.83) |

### What Worked
- GOOGL post-earnings drift: clean Plan A entry on gap-up + first-15-min pullback hold, +4.15% by Fri close — playbook executed exactly
- AAPL drift entry Fri: applied META lesson (verified lastday_price < open before "gap-up" call), waited for ISM 7 AM PST print to clear, sized 8.6% under 10% Friday-overnight cap
- PLTR holding into Mon AMC print despite mid-week drawdown — patience held the line, recovered to +0.12% by close
- 10% trail GTC kept NVDA on the books at -5.43% with ~1.7% buffer remaining — let the rule do the work instead of pre-emptive cuts
- Capital discipline: two intraday rule violations (MSFT, META) cut within ~90 sec each, total cost ~$1.49 vs preserved PDT slots and reset thesis

### What Didn't Work
- Pre-market plan vs market-open execution conflict on Mon: separate agent worked off a clone missing the binding INTC plan, took NVDA/MSFT/PLTR instead — INTC was the correct setup and proceeded to rip +50% in 7 sessions while we held the wrong names
- META gap-down misread Thu: did not compare current to lastday_price before assuming "gap-up pullback"; entry+cut burned a PDT slot
- NVDA -5.43% from entry — sized 10.49% over the 10% event-week cap (micro-overage at entry, no trim) and the position has been a drag on the book all week
- INTC chase trap: the planned $76-78 retest never materialized; the right read was "missed setup, document, move on", but the +50% subsequent rip is a reminder that early conviction matters
- Sleeve under-deployment: alpha at 36.2% (target 70-75%) and niche at 0% (target 20-25%) — by design under event-risk week, but two more weeks at this level = structural underperformance vs benchmark

### Key Lessons
- ALWAYS `git fetch && git pull` BEFORE any trade decision on a new clone; the pre-market research artifact is the binding plan
- Verify lastday_price < current price BEFORE calling a session "gap-up" — narrowing intraday spread is NOT a pullback if the day opened gap-DOWN
- Post-earnings drift > pre-earnings entry: GOOGL and AAPL were the highest-quality entries of the week; both came AFTER the catalyst printed
- Round-share sizing on $10k account routinely lands 0.06-0.49% over per-position caps; either accept micro-overages or wait for prices that hit the cap exactly
- Two failed sectors (energy oil de-escalation, defense ceasefire-fade) pulled out of consideration this week — followed strategy rule on sector momentum

### Adjustments for Next Week
- Ramp alpha deployment toward target: aim for 50-60% by Fri 5/8, taking 1-2 more qualified entries (post-earnings drift candidates from PLTR Mon AMC + earnings-week tape)
- Consider trimming 1 NVDA share if NVDA breaks $200 with no bid Mon — currently 10.49% over event-week cap is no longer relevant (event week ended), but sizing now flagged as drag
- Run pre-market routine BEFORE market-open routine on Mon and verify the agent reads the latest research log entry; add an explicit "fetch + tail RESEARCH-LOG" gate in the open routine
- Niche sleeve still empty — re-evaluate weekly; no force, but target 1 niche entry within next 2 weeks if a clean 2.5:1 R:R emerges
- PLTR plan: hold into Mon AMC, decide trim/hold by Mon close per pre-print thesis health; do NOT add into the print

### Overall Grade: C+
Bot lagged S&P by ~0.95% on a benchmark-up week with two open winners (GOOGL +4.15%, PLTR +0.12%) offset by one NVDA drag (-5.43%) and one mistimed AAPL entry (-1.63%). Two rule-violation round-trips were caught and unwound the same session. Execution improved sharply Thu-Fri (clean Plan A on GOOGL, disciplined Plan B on AAPL with META lesson applied). The setup pipeline is real now; the sleeve allocation lag is the next gap to close.
