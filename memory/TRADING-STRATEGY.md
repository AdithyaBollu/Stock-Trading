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

### Position caps are ENTRY ceilings (added 2026-08-07, Week 16)
Every "max % per position" figure is measured **at fill**, against equity at that moment. A position that drifts above its cap on **appreciation** is compliant and requires **no trim** — the +15%/+20% trail-tighten ladder is the mechanism that resolves it. Only a *new buy* that would breach the cap is blocked.
- Rationale: PLTR drifted to 15.48% vs the 15% short-term cap on a +15.91% gain (Week 16). The rulebook was silent; the alternative reading mandates cutting the best position in the book to satisfy a ratio.

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

## Deployment Rules (Hard)
- Cash > 5%: BUY. Find a setup immediately. If no single stock clears, buy VOO in long-term sleeve.
- Long-term sleeve < 50%: add to existing long-term winners or buy VOO/QQQ
- Short-term sleeve < 50%: find an earnings play, momentum name, or niche setup
- Under-deployment is a failure mode every single time it occurs.

### NO SELF-INVENTED GATES (added 2026-08-07, Week 16)
Any gate, filter, or test used to **block** an entry must cite a specific line in this file. If it cannot be cited, **it does not exist** and must not be applied.
- Any spread test must be computed from **regular-hours consolidated quotes**. Pre-market IEX odd-lot quotes are not tradeable quotes and must never gate a decision.
- Rationale: 39 consecutive sessions at 100% cash (Weeks 12–16) were caused by three invented gates — a "spread <1%" test built on pre-market odd-lot data (read GOOGL at 10.6% vs a real ~0.08% spread), a "chase-gate", and a "pilot rule". None appeared in this file. All retired 2026-08-04.

### Cash-breach remediation is SAME-SESSION (added 2026-08-07, Week 16)
If an exit or stop-out pushes cash above 5% **after** the midday scan, the proceeds are redeployed **before the close of that same session** — short-term replacement first, VOO in the long-term sleeve as the mandated fallback. The EOD routine owns this check.
- Rationale: Week 16 had two breaches (Wed 16.91% held for three hours, Thu 25.67% at the open). Neither was a judgment failure — no routine was scheduled between the fill and the bell.
