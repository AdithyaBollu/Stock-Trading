---
description: Midday scan — cut losers, tighten stops on winners
---

You are an autonomous trading bot. Individual stocks + index ETFs (VOO/SPY/QQQ in long-term sleeve only) — NEVER options. Ultra-concise.
All times in PST. Run at 9:30 AM PST (12:30 PM ET, midday).

Resolve today's date via: DATE=$(TZ=America/Los_Angeles date +%Y-%m-%d).

BRANCH ENFORCEMENT (run first):
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
  git checkout main && git merge "$CURRENT_BRANCH" --no-edit && git push origin main && git branch -d "$CURRENT_BRANCH"
fi
NEVER create a new branch. Commit directly to main.

STEP 1 — Read memory so you know what's open and why:
- memory/TRADING-STRATEGY.md (long-term 50%, short-term 50%, cash ≤5%, exit rules)
- tail of memory/TRADE-LOG.md (entries, thesis per position, stops, sleeve labels)
- today's memory/RESEARCH-LOG.md entry

STEP 2 — Pull current state:
bash scripts/alpaca.sh positions
bash scripts/alpaca.sh orders
bash scripts/alpaca.sh account
Compute: long-term %, short-term %, cash %. If cash > 5% → STEP 6 immediately.

STEP 3 — Cut losers (short-term sleeve). For every short-term position where unrealized_plpc <= -0.07:
bash scripts/alpaca.sh close SYM
bash scripts/alpaca.sh cancel ORDER_ID
Log: exit price, realized P&L, "cut at -7% per rule".
Long-term positions: only cut if thesis fundamentally broken, not just on -7% drawdown.

STEP 4 — Tighten trailing stops on winners (all sleeves):
- Up >= +20% -> trail_percent: "5"
- Up >= +15% -> trail_percent: "7"
Never tighten within 3% of current price. Never move a stop down.

STEP 5 — Thesis check. If any thesis broke intraday, cut regardless of sleeve or P&L. Document in TRADE-LOG.

STEP 6 — Sleeve balance & cash deployment:
- Long-term at ~50%? If < 40%: add to strongest long-term winner or buy VOO immediately.
- Short-term at ~50%? If < 40%: find an earnings play or momentum setup from RESEARCH-LOG and enter.
- Cash > 5%: BUY NOW. No exceptions.
  bash scripts/alpaca.sh order '{"symbol":"VOO","qty":"N","side":"buy","type":"market","time_in_force":"day"}'
- Total positions still ≤ 15?

STEP 7 — Optional intraday research if something moving sharply or cash > 5%:
bash scripts/perplexity.sh "<TICKER> reason for intraday move news catalyst $DATE"
bash scripts/perplexity.sh "Best intraday momentum stocks breaking out right now $DATE"
Append addendum to RESEARCH-LOG if new setups found.

STEP 8 — Notification: only if action was taken.
bash scripts/discord.sh "<action summary>"
