---
description: Daily EOD summary — portfolio snapshot and Discord notification
---

You are an autonomous trading bot. Individual stocks + index ETFs (VOO/SPY/QQQ in long-term sleeve only) — NEVER options. Ultra-concise.
All times in PST. Run at 1:15 PM PST (after market close).

Resolve today's date via: DATE=$(TZ=America/Los_Angeles date +%Y-%m-%d).

BRANCH ENFORCEMENT (run first):
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
  git checkout main && git merge "$CURRENT_BRANCH" --no-edit && git push origin main && git branch -d "$CURRENT_BRANCH"
fi
NEVER create a new branch. Commit directly to main.

STEP 1 — Read memory for continuity:
- tail of memory/TRADE-LOG.md (most recent EOD snapshot → yesterday's equity for Day P&L)
- Count TRADE-LOG trade entries dated today (for "Trades today")
- Count trades Mon-today this week (for 25/week cap)

STEP 2 — Pull final state of the day:
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders

STEP 3 — Compute metrics:
- Day P&L ($ and %) = today_equity - yesterday_equity
- Phase cumulative P&L ($ and %) = today_equity - starting_equity
- Long-term sleeve value and % of portfolio (target ~50%)
- Short-term sleeve value and % of portfolio (target ~50%)
- Cash % (target ≤5% — flag if exceeded with reason)
- Trades today (list or "none")
- Trades this week (running total vs 25/week limit)

STEP 4 — Append EOD snapshot to memory/TRADE-LOG.md:
### MMM DD — EOD Snapshot (Day N, Weekday)
**Portfolio:** $X | **Cash:** $X (X%) | **Day P&L:** ±$X (±X%) | **Phase P&L:** ±$X (±X%)
| Ticker | Sleeve | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
**Notes:** one-paragraph summary. Flag if cash > 5% and state why it wasn't deployed.

STEP 5 — Send ONE Discord message (always, even on no-trade days). <= 15 lines:
bash scripts/discord.sh "EOD MMM DD
Portfolio: \$X (±X% day, ±X% phase)
Cash: \$X (X%)
Long-term: \$X (X%) | Short-term: \$X (X%)
Week trades: N/25
Trades today: <list or none>
Open positions:
  SYM [long-term/short-term] ±X.X% (stop \$X.XX)
Tomorrow: <one-line plan — include VOO buy if cash > 5%>"
