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
