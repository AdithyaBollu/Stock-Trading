# Trading Strategy
## Mission
Beat the S&P 500 over the challenge window through stock picking alone. Two sleeves: high-conviction alpha stocks + niche/asymmetric picks. Stocks only — no options, no ETFs, ever.

## Philosophy
Concentrate in 6-10 high-conviction individual stocks across two sleeves. Alpha sleeve is the core engine; niche sleeve captures asymmetric upside. Lean aggressive — deploy capital when a thesis clears the bar. Patience still trumps random activity, but "HOLD" is not a default dodge when real setups exist.

## Capital & Constraints
- Starting capital: ~$10,000
- Platform: Alpaca
- Instruments: Individual stocks ONLY — no options, no ETFs, ever
- PDT limit: 3 day trades per 5 rolling business days (account < $25k)
- All times in PST (market opens 6:30 AM PST, closes 1:00 PM PST)

## Capital Allocation — Two Sleeves

| Sleeve | Target | Max per position | Positions |
|--------|--------|-----------------|-----------|
| Alpha stocks | 70–75% | 15% per stock | 5–6 positions |
| Niche/speculative | 20–25% | 10% per pick | 2–4 positions |
| Cash buffer | 5–10% | — | For adds and opportunities |

Total deployed target: 90–95%. Max 10 total positions.

## Sleeve 1 — Alpha Stocks (70–75%)

High-conviction, catalyst-driven positions in sector-momentum names or high-quality mean-reversion setups. Hold weeks to months.

### Core Rules
1. NO OPTIONS, NO ETFs — ever
2. Max 15% of equity per alpha position
3. Max 15 new trades per week (alpha + niche combined)
4. 10% trailing stop GTC on every position (place immediately after fill)
5. Cut losers at -7% manually — do not wait for the stop
6. Tighten trail: 7% at +15%, 5% at +20%
7. Never move stop within 3% of current price; never move a stop down
8. Follow sector momentum OR take contrarian mean-reversion in oversold leaders with a documented catalyst
9. Event-risk weeks (FOMC, mega-cap earnings) do NOT auto-veto entries — size down to 10% max per position that week and proceed if R:R clears the bar
10. Default bias: if a setup clears the checklist, TAKE IT. Only HOLD when nothing clears the checklist — not as a reflex.

### Sector Themes (2025–2026) — prioritized
- **AI / Semiconductors (core focus)** — NVDA, AMD, AVGO, MRVL, ANET, INTC, TSM, MU, QCOM, ARM, SMCI, ASML, KLAC, LRCX, AMAT
- **Mega-cap Tech** — MSFT, GOOGL, META, AMZN, AAPL (earnings-driven entries OK)
- **Defense & Aerospace** — LMT, RTX, NOC, PLTR
- **Healthcare Innovation** — biotech catalysts, GLP-1 plays (LLY, NVO)
- **Energy** — LNG, natural gas infrastructure, selective clean energy
- **Infrastructure & Industrials** — CAT, DE, PWR, VST, CEG (data-center power)

### Entry Checklist
- Clear catalyst documented in today's RESEARCH-LOG?
- Sector in momentum OR defensible mean-reversion thesis?
- Position cost ≤ 15% of equity (≤ 10% during event-risk weeks)?
- Stop defined 10% below entry?
- Target ≥ **1.2:1 R:R** (lowered from 1.5:1)?
- Total trades this week ≤ 15?
- Total positions after trade ≤ 10?

### Exit Triggers
- Trailing stop hit (automatic GTC)
- -7% intraday — cut manually
- Thesis broken intraday → cut immediately regardless of P&L
- +20% → cancel old stop, place 5% trail
- +15% → cancel old stop, place 7% trail

## Sleeve 2 — Niche / Speculative (20–25%)

Asymmetric, high-conviction plays — binary catalysts, sector dislocations, small-cap breakouts, earnings setups.

### Rules
1. Max 10% of equity per niche position
2. Max 2–4 niche positions open simultaneously
3. Require minimum **2.5:1 R:R** (lowered from 3:1) thesis documented before entry
4. Hard stop at -10%, no exceptions, no extensions
5. Counts toward the 15-trade/week combined limit
6. Examples: FDA catalyst, earnings surprise setup, macro dislocation, small-cap breakout, post-earnings drift

### Entry Checklist
- Asymmetric thesis written out (2.5:1 R:R minimum)?
- Position cost ≤ 10% of equity?
- Hard stop at -10% defined?
- Total trades this week ≤ 15?

## Earnings Focus (new)
Every pre-market routine must surface companies reporting earnings this week and evaluate each as a potential entry/exit:
- **Pre-earnings entry:** only if clear fundamental/technical setup + catalyst thesis. Size down to 10% max. Count toward weekly limit.
- **Post-earnings entry (drift play):** preferred — enter morning after a clean beat + guide-raise with sector tailwind. Niche sleeve eligible.
- **Currently-held ticker reporting:** document pre-earnings plan (hold/trim/stop adjust) in RESEARCH-LOG the day before.

## Weekly Rhythm
- Monday: review all positions against thesis; assess adds; log this week's earnings calendar
- Daily: track stops, thesis health, sector momentum, earnings calendar
- Friday: full weekly review — grade the week, adjust strategy if 2+ weeks of evidence
- Ongoing: tighten stops on winners per the schedule above

## Deployment & Niche Activation Policy (added 2026-05-22, Week 5 review)
Five consecutive weeks ran at ~17–27% deployed vs the 70–75% alpha target with an empty niche sleeve. The held book worked every week, but the cash drag was the primary driver of benchmark underperformance in up-weeks (-1.06% relative the week this was written). The no-chase gate is correct and stays; the fix is broadening *how* capital gets deployed, not lowering the quality bar.

### Counter-policy 1 — Core-winner add path
- A proven in-book alpha winner (currently green from entry, thesis intact, drift extending) OR a mega-cap sector leader in a confirmed uptrend may be added **without requiring a fresh earnings catalyst**.
- Entry trigger: a normal 3–5% pullback to a **rising 20-DMA** with a **volume reclaim** off that level.
- Sizing: ≤10% of equity per add; combined position must still respect the 15% per-alpha-position cap.
- Still no-chase gated: never buy within 3% of the session HOD; never add into a vertical/extended move with no pullback structure.
- Counts toward the 15-trade/week limit.
- Purpose: lift sleeve deployment toward target on quality names already validated, rather than waiting only for the rare A+ post-earnings drift.

### Counter-policy 2 — Mandatory niche screen
- The pre-market routine MUST produce an explicit niche-candidate list **every session**: FDA calendar, small-cap breakout scan, mid-cap post-earnings drift.
- At least one screened candidate must be logged with a take/skip reason — "no idea cleared" is only acceptable output AFTER the screen has demonstrably run.
- Niche entries still require the 2.5:1 R:R thesis + -10% hard stop + ≤10% sizing.

### Deployment floor (soft target, not a forced-trade mandate)
- Target lifting alpha deployment toward 40%+ on the first qualifying core-add or A+ setup. This is a bias to act on quality, NOT a license to chase to hit a number — under-deployment is still preferable to a forced bad entry. The floor exists to counter the proven 5-week ceiling, not to override the no-chase gate.
