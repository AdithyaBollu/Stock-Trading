# Trading Strategy
## Mission
Beat the S&P 500 over the challenge window through aggressive stock picking and disciplined capital deployment. Two sleeves: long-term holds (quality stocks + index ETFs) + short-term active trades (earnings plays, momentum, niche/speculative). Stocks and index ETFs only — no options, ever.

## Philosophy
**Capital sitting in cash is a failure.** Deploy 95–100% of capital at all times. If no single-stock idea clears the bar, park excess in VOO/QQQ in the long-term sleeve — never let capital sit idle. The long-term sleeve provides a stable return baseline; the short-term sleeve generates alpha. Both must be fully deployed and actively managed. Be aggressive: size up on high-conviction, act on good setups the same session you find them.

## Capital & Constraints
- Starting capital: ~$10,000
- Platform: Alpaca
- Instruments: Individual stocks + index ETFs (VOO, SPY, QQQ) in long-term sleeve only — NO OPTIONS, EVER
- PDT limit: 3 day trades per 5 rolling business days (account < $25k) — swing trades only
- All times in PST (market opens 6:30 AM PST, closes 1:00 PM PST)

## Capital Allocation — Two Sleeves

| Sleeve | Target | Max per position | Hold Period | Positions |
|--------|--------|-----------------|-------------|-----------|
| Long-term | 50% | 20% per stock/ETF | Weeks to months | 3–6 positions |
| Short-term | 50% | 15% per trade | Days to weeks | 5–9 positions |
| Cash buffer | ≤5% | — | Settlement only | — |

Total deployed target: **95–100%.** Cash > 5% is a failure mode — find a setup or buy VOO.
Max 15 total positions.

### Position Caps Are ENTRY-SIZING Caps (ratified 2026-08-14, Week 17)
The 15% / 20% per-position limits bind at **order entry** — "position *cost* ≤ X% of equity."
- A position that drifts above its cap on **appreciation** (or because the equity denominator fell) is **NOT a violation** and requires **no trim**. Flag it in the log; do not trade on it.
- The **trailing stop is the resolving mechanism** for passive drift. If the name reverses, the stop trims it.
- **Never open a cash breach (>5%) to cure a mark-to-market cap overage.** A real rule violation is never an acceptable price for a cosmetic one.
- Evidence: PLTR 15.48%→15.76% (8/7–8/11) on a +18.87% gain; MSFT 20.05% (8/14 midday) on a session MSFT *fell*. Deferred seven sessions before ratification.

### Minimum Position Count Per Sleeve (ratified 2026-08-14, Week 17)
Sleeve targets and per-position caps are jointly satisfiable **only above a minimum name count**:
- **Short-term: ≥4 names required.** 3 × 15% = 45% < the 50% target — with three names the sleeve *cannot* reach target at any legal sizing.
- **Long-term: ≥3 names required.** 2 × 20% = 40% < the 50% target.
- **When a sleeve is under target, the remedy is a NEW NAME, never a bigger slice of an existing one.** Concentrating further into a name already at multiples of its written plan size is a real risk taken for a cosmetic point.
- If no new name clears its checklist, the shortfall is logged as an idea-generation failure — not a sizing failure — and the next session's P0 is finding one.
- Evidence: short-term sleeve under target 9 consecutive sessions (8/4–8/14) with only 3 names and every add breaching the 15% cap on a single share.

### Discretionary Sizing Caps Must Name a Trigger, and They LAPSE (ratified 2026-08-21, Week 18)
A sizing cap **tighter than the sleeve cap** (e.g. a "10% macro cap") is only in force while its trigger is live.
- The cap must **state its exact trigger condition** (e.g. "Brent > $95 or VIX > 20") and be **re-tested and recorded every pre-market session**.
- **If the trigger has not fired for 5 consecutive sessions, the cap LAPSES** back to the sleeve cap (15% short-term / 20% long-term). Re-imposing it requires the trigger to actually fire.
- The **10% binary-event cap (Short-Term Rule 6) is independent and unaffected** — it is triggered by a dated earnings print inside the hold horizon, not by a market condition, and never lapses on a session count.
- A lapsed cap authorises **larger sizing on NEW non-reporting names only**. It never authorises adding to a name that reports inside the hold horizon.
- Evidence: the 10% macro cap bound every short-term entry 8/18–8/21 while **Brent peaked at $93.82 against a $95 trigger and VIX ranged 14.52–15.86 against a 20 trigger — the trigger fired on zero sessions.** Six names × ~10% ≈ 43% is arithmetically the sleeve's ceiling under it, and the sleeve finished the week at 42.92%.

### Sleeve Shortfalls Require a Reachability Check Before They Are Logged (ratified 2026-08-21, Week 18)
Before recording a sleeve as "under target," compute **max reachable = (number of names) × (binding per-position cap).**
- If **max reachable < target**, the shortfall is a **CAP problem, not a NAME problem.** The session must then either (a) name the binding cap and test whether its trigger is live per the rule above, or (b) add a name.
- **A sleeve may not be logged as "structurally unreachable" for more than 3 consecutive sessions without escalating the cap question to the weekly review.**
- Evidence: 24 consecutive sessions (7/17–8/21) of "long-term over / short-term under," each correctly declining a Rule-8-barred trim, and **none testing whether the binding cap was legitimately in force.**

---

## Sleeve 1 — Long-Term (50%)

Quality growth stocks and index ETFs held weeks to months. Core engine for stable capital growth.

### Instruments Allowed
- **Index ETFs**: VOO, SPY, QQQ — use as default parking when no better individual stock clears the bar
- **Quality growth stocks**: sector leaders with durable competitive advantage, earnings growth trend

### Core Rules
1. NO OPTIONS — ever, under any circumstances
2. Index ETFs (VOO, SPY, QQQ) are PERMITTED in this sleeve only
3. Max 20% of equity per position (stocks or ETFs)
4. 10% trailing stop GTC on every position
5. Cut if thesis fundamentally breaks — do not hold through broken fundamentals
6. Tighten trail: 7% at +15%, 5% at +20%
7. If long-term sleeve < 50% deployed: buy more of existing winners or add VOO/QQQ immediately
8. Hold through normal volatility — only exit on stop hit or broken thesis

### Target Names — Long-Term Sleeve
- **AI / Semiconductors**: NVDA, AMD, AVGO, MRVL, ANET, TSM, MU, SMCI, ASML
- **Mega-cap Tech**: MSFT, GOOGL, META, AMZN, AAPL
- **Disruptive / Niche (long-term thesis)**: ASTS, RKLB, OKLO — if 6–12 month thesis documented
- **Defense & Infrastructure**: LMT, RTX, PLTR, VST, CEG
- **Index fallback**: VOO (S&P 500), QQQ (Nasdaq 100) — always valid if no better idea

### Entry Checklist
- Thesis documented (why this name, why now, target price)?
- Position cost ≤ 20% of equity?
- 10% trailing stop placed immediately after fill?
- Total positions after trade ≤ 15?
- Total trades this week ≤ 25?
- For ETFs (VOO/SPY/QQQ): no additional checklist required — just buy if sleeve < 50%

### Exit Triggers
- Trailing stop hit (automatic GTC)
- Thesis fundamentally broken (guidance cut, sector collapse, management change)
- +20% → tighten trail to 5%
- +15% → tighten trail to 7%

---

## Sleeve 2 — Short-Term / Active (50%)

Aggressive active trading: earnings plays, technical breakouts, sector rotations, niche/speculative. Hold 1–14 days.

### Sub-categories
- **Earnings plays**: pre-earnings setup OR post-earnings drift (beat + guide raise)
- **Momentum/technical**: breakouts above resistance, sector rotation leaders
- **Niche/speculative**: ASTS, RKLB, OKLO, AEHR, NBIS and similar disruptors — binary catalyst or thesis buildup

### Core Niche Watchlist (always research these — niche sub-category)
- **ASTS** — AST SpaceMobile (space-based mobile broadband; constellation buildout)
- **RKLB** — Rocket Lab (launch services + satellite components; Neutron rocket)
- **OKLO** — Oklo Inc. (advanced nuclear microreactors; data-center power demand)
- **AEHR** — Aehr Test Systems (next-gen semiconductor test equipment; SiC/GaN wave)
- **NBIS** — Nebius Group (European AI infrastructure / GPU cloud)
- Scan for similar: space, nuclear, AI infra, defense tech, next-gen semis, biotech catalysts

### Core Rules
1. Individual stocks ONLY in this sleeve — no ETFs
2. Max 15% of equity per short-term position
3. Hard cut at -7% — no exceptions, no holding through a loser
4. 10% trailing stop GTC on every new position
5. Tighten trail: 7% at +15%, 5% at +20%
6. Earnings plays: size to 10% if taking binary event risk
7. If short-term sleeve < 50% deployed: find an earnings play, momentum name, or niche setup — do not sit on cash
8. Counts toward the 25-trade/week combined limit
9. Minimum R:R: **1.5:1** (short-term), **2.5:1** (niche/speculative)

### Entry Checklist — Earnings Plays
- Beat + guide raise (post-earnings drift) OR strong pre-earnings technical + bullish consensus trend
- Sector tailwind confirmed?
- Position ≤ 10% (binary event) or ≤ 15% (drift play after report)?
- Stop at -7%?

### Entry Checklist — Niche / Speculative
- Full 7-point research documented in RESEARCH-LOG:
  1. Earnings/Fundamentals: last 2 quarters EPS trend, revenue growth, guidance
  2. Analyst Coverage: price targets, recent upgrades/downgrades
  3. Institutional Activity: 13F changes, insider buying/selling
  4. News & Catalysts: key news last 2 weeks, upcoming events
  5. Sentiment: short interest %, squeeze potential, investor community view
  6. Technical: support/resistance, trend, volume
  7. Thesis: why now, what's the asymmetric upside, 2.5:1 R:R path
- Position ≤ 15% of equity?
- Hard stop at -7% defined?

---

## Earnings Calendar — Weekly Discipline (MANDATORY)
Every Monday pre-market, poll the full week's earnings calendar. For each reporting company:

**Research required per earnings ticker:**
bash scripts/perplexity.sh "<TICKER> earnings preview consensus EPS revenue guidance analyst sentiment"
bash scripts/perplexity.sh "<TICKER> options implied move earnings sentiment bull bear case"
bash scripts/perplexity.sh "<TICKER> institutional positioning going into earnings $DATE"

**Classify each as:**
- **PRE-EARNINGS ENTRY**: strong technical base + bullish estimate trend + sector tailwind → enter before report, size to 10%
- **POST-EARNINGS DRIFT WATCH**: wait for clean beat + guide raise → enter next morning
- **HOLD CURRENT (if owned)**: document plan — hold/trim/exit before report
- **AVOID**: weak setup, binary risk without edge, negative sentiment

Refresh sentiment check each subsequent day that week for the ones on watch.

---

## Macro & Geopolitical Monitoring (daily)
Every pre-market routine must assess the following and log in RESEARCH-LOG:
- **Fed policy**: rate decision status, next FOMC date, FedWatch cut probability, Fed speakers
- **Inflation**: latest CPI/PPI/PCE reading, trend direction, expectations vs actual
- **Economic data**: jobs/unemployment, GDP revision, consumer confidence
- **Treasury yields**: 2yr/10yr spread — steep rise = multiple compression risk
- **Geopolitical**: conflicts affecting oil/commodities (Middle East, Russia/Ukraine), US-China trade/tariffs
- **Fiscal**: US debt ceiling, government spending, sector-specific legislation

Impact classification:
- **HIGH**: directly reprices sector today → size down to 10% max, tighten existing stops
- **MEDIUM**: developing — monitor intraday
- **LOW/PRICED IN**: noted, business as usual

---

## General Market Health Check (daily)
- S&P 500, Nasdaq, Russell 2000 performance vs prior day
- Sector rotation: which sectors leading, which lagging
- Market breadth: advance/decline ratio
- VIX level: <15 = low fear (lean aggressive), 15–25 = normal (standard sizing), >25 = elevated (reduce new positions to 10% max)
- Put/call ratio

---

## Weekly Rhythm
- Monday: full earnings calendar pull + sentiment for each reporter; review all positions vs thesis; niche watchlist refresh
- Daily pre-market: macro scan, geopolitical, Fed, general market health, niche radar, earnings sentiment update
- Midday: cut losers, tighten stops on winners, check sleeve deployment — if cash > 5%, find a setup or buy VOO
- Friday: full weekly review, grade the week, adjust strategy if 2+ weeks of evidence

---

## Order & Stop Mechanics (Hard)

### Stale-Quote Override on the Spread Gate (ratified 2026-08-14, Week 17)
The quote endpoint intermittently returns a **stale single-venue artifact** — a frozen ask on a 100x100 book while the bid moves underneath — printing fabricated 3–30% spreads on liquid names.
- A spread-gate failure **may be overridden** only by **trade-print evidence**: pull 1-minute bars and confirm **continuous trading (tens to hundreds of prints/min) inside a range tighter than the quoted spread**.
- When the override is used, **place a LIMIT order at the rule-compliant price**, never a market order — so that if the wide book *were* real, no R:R ceiling or sizing rule can be breached on the fill.
- Log the polls discarded and the bar evidence used. Never override on a single poll or on intuition.
- Evidence: ANET/VRT/RKLB, five consecutive sessions 8/10–8/14; RKLB 8/14 required discarding six of eight polls, then filled at $81.29 against an $81.96 limit.

### Add-On Lots May Not Be Stopped Below Existing Lots (ratified 2026-08-14, Week 17)
When adding shares to a name already held, set the new lot's trail so its stop sits **at or above the lowest existing stop on that name** — even if that requires a trail **tighter than 10%**.
- A textbook 10% trail anchored to a lower fill would leave the **newest** shares protected **worse** than the oldest. That is the substance of "never move a stop down," even though no existing order is modified.
- Flag the deliberate deviation in the trade log so a later session does not "correct" it downward.
- Evidence: RKLB 8/14 — a 10% trail off the $81.29 fill would have sat at $73.16, below both existing RKLB legs and the $73.97 floor; set at 8.63% / $74.28 instead.

---

## Deployment Rules (Hard)
- Cash > 5%: BUY. Find a setup immediately. If no single stock clears, buy VOO in long-term sleeve.
- Long-term sleeve < 50%: add to existing long-term winners or buy VOO/QQQ
- Short-term sleeve < 50%: find an earnings play, momentum name, or niche setup — **a NEW name, per the minimum-position-count rule above**
- Under-deployment is a failure mode every single time it occurs.
- **Late-session sweep (added 2026-08-14):** if a stop fires **after the midday routine**, the released cash must be redeployed the **same session** — do not leave proceeds idle into the close. Stops fire on the market's clock, not the routine calendar. Evidence: 8/11 GOOGL stop proceeds ($1,381.00) landed 11:43 AM PT into an unscheduled window and sat overnight into the CPI print — the phase's first cash-test failure after 41 consecutive passes.
- **The EOD routine OWNS the late-session sweep (ratified 2026-08-21, Week 18).** The rule above had no numbered step in any routine and failed twice from the same schedule hole. It is now an explicit EOD step:
  - **EOD must check whether any stop filled after the midday routine.** If one did, EOD **places the redeploy order in the same session** — as a **next-open LIMIT at the pre-derived rule-compliant price** when the market has already closed. A queued next-open limit satisfies the sweep; idle proceeds do not.
  - The redeploy target is the **highest-R:R name on the armed board** that the proceeds can afford at a compliant size, using the ceiling already derived in that day's research — not a fresh derivation at 1:15 PM.
  - Evidence: **two failures from the identical hole** — 8/11 GOOGL ($1,381.00, 11:43 AM PT) and 8/20 ADI ($370.11, 12:55 PM PT) — separated by a weekly review that made closing it a dated P0 and did not. A remedy that lives in a review bullet rather than a routine step does not get executed.
