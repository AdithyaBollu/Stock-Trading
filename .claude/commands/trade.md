---
description: Manual trade helper with strategy-rule validation. Usage — /trade SYMBOL SHARES buy|sell
---

Execute a manual trade with full rule validation. Refuse if any rule fails.
All times in PST (market: 6:30 AM – 1:00 PM PST). No ETFs — individual stocks only.

Args: SYMBOL SHARES SIDE (buy or sell). SLEEVE (alpha/niche). If missing, ask.

1. Pull state: account, positions, quote SYMBOL (capture ask price P).
2. For BUY — Alpha sleeve, validate:
   - Total positions after fill <= 8
   - Trades this week (alpha + niche combined) + 1 <= 15
   - SHARES * P <= 15% of equity
   - SHARES * P <= available cash
   - daytrade_count < 3
   - Catalyst documented (ask for thesis if not in today's RESEARCH-LOG)
   If any fail, STOP and print the failed checks.
3. For BUY — Niche sleeve, validate:
   - Total positions after fill <= 8
   - Trades this week (alpha + niche combined) + 1 <= 15
   - SHARES * P <= 10% of equity
   - SHARES * P <= available cash
   - daytrade_count < 3
   - 3:1 R:R thesis documented (ask if missing)
   - Only 1 niche position open at a time (warn if adding second)
   If any fail, STOP and print the failed checks.
4. For SELL, confirm position exists with right qty. No other checks.
5. Print order JSON + validation results, ask "execute? (y/n)".
6. On confirm:
   bash scripts/alpaca.sh order '{"symbol":"SYM","qty":"N","side":"buy|sell","type":"market","time_in_force":"day"}'
7. For BUYs, immediately place 10% trailing stop GTC:
   bash scripts/alpaca.sh order '{"symbol":"SYM","qty":"N","side":"sell","type":"trailing_stop","trail_percent":"10","time_in_force":"gtc"}'
8. Log to memory/TRADE-LOG.md with: sleeve (alpha/niche), full thesis, entry, stop, target, R:R.
9. bash scripts/discord.sh with trade details including sleeve label.
