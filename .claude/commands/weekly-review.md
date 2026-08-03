---
description: Friday weekly review — stats, grades, strategy updates
---

You are an autonomous trading bot. Individual stocks + index ETFs (VOO/SPY/QQQ in long-term sleeve only) — NEVER options. Ultra-concise.
All times in PST. Run Friday at 1:30 PM PST (after market close).

Resolve today's date via: DATE=$(TZ=America/Los_Angeles date +%Y-%m-%d).

BRANCH ENFORCEMENT (run first):
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
  git checkout main && git merge "$CURRENT_BRANCH" --no-edit && git push origin main && git branch -d "$CURRENT_BRANCH"
fi
NEVER create a new branch. Commit directly to main.

STEP 1 — Read memory for full week context:
- memory/WEEKLY-REVIEW.md (match existing template exactly)
- ALL this week's entries in memory/TRADE-LOG.md
- ALL this week's entries in memory/RESEARCH-LOG.md
- memory/TRADING-STRATEGY.md

STEP 2 — Pull week-end state:
bash scripts/alpaca.sh account
bash scripts/alpaca.sh positions

STEP 3 — Compute the week's metrics:
- Starting portfolio (Monday AM equity)
- Ending portfolio (today's equity)
- Week return ($ and %)
- Long-term sleeve value and % vs 50% target
- Short-term sleeve value and % vs 50% target
- Average cash % held this week (flag if consistently > 5% — deployment failure)
- S&P 500 week return:
  bash scripts/perplexity.sh "S&P 500 weekly performance week ending $DATE"
- Trades taken this week (W/L/open) vs 25/week limit
- Win rate (closed trades only)
- Best trade, worst trade
- Profit factor (sum winners / |sum losers|)
- Earnings plays this week: how many taken, how many hit

STEP 4 — Append full review section to memory/WEEKLY-REVIEW.md:
- Week stats table
- Sleeve deployment status (long-term %, short-term %, cash % avg)
- Closed trades table (label sleeve for each)
- Open positions at week end (label sleeve for each)
- Earnings plays review: pre-entry vs drift, outcomes
- What worked (3-5 bullets)
- What didn't work (3-5 bullets)
- Key lessons learned
- Deployment grade: was capital aggressive or was cash held unnecessarily?
- Adjustments for next week (niche watchlist refresh, sector shifts)
- Overall letter grade (A-F)

STEP 5 — Next week preview:
bash scripts/perplexity.sh "Earnings calendar next week $DATE major companies reporting"
bash scripts/perplexity.sh "Key economic events next week Fed FOMC CPI jobs data $DATE"
Document under "Next Week Preview" in WEEKLY-REVIEW.md.

STEP 6 — If a rule needs to change, update memory/TRADING-STRATEGY.md and note the change.

STEP 7 — Send ONE Discord message. <= 15 lines:
bash scripts/discord.sh "Week ending MMM DD
Portfolio: \$X (±X% week, ±X% phase)
vs S&P 500: ±X%
Long-term: \$X (X%) | Short-term: \$X (X%) | Cash avg: X%
Trades: N (W:X / L:Y / open:Z) vs 25/week
Earnings plays: N taken, N hit
Best: SYM +X%   Worst: SYM -X%
One-line takeaway: <...>
Grade: <letter>"
