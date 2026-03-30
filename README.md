# Japan Content Investment Efficiency & Export Value Framework

*Part of a two-project analytical series. The companion project
([APAC Streaming Competitive Intelligence](../apac-streaming-ci/README.md))
maps the competitive environment; this project provides a framework for
content investment discussion within that environment.*

## 1. Problem

Content investment discussions require evaluating not just how much a title is
watched, but how efficiently it generates viewing relative to cost, and whether
its value is primarily domestic or globally exportable. These questions matter
most when understood in the context of each market's competitive structure —
which is why this project is designed as a companion to the APAC competitive
intelligence analysis. With Netflix's public Engagement Report data, we can
build a transparent discussion framework even without internal financial data.

## 2. Scope

- **Market:** Japan only
- **Sample:** 21 titles, all Japan-produced and Japanese-language
- **Inclusion criteria:** Primary production country Japan, primary language Japanese, appeared in Netflix public engagement data
- **Content types:** Anime (7), Drama (6), Film (3), Reality/Unscripted (5)
- **Metrics:** Viewing efficiency, export value, portfolio role
- **NOT in scope:** Exact ROI, title-level budgets, subscriber impact, non-Japanese titles

## 3. Data Sources

| Source | What It Provides | Vintage |
|---|---|---|
| Netflix Engagement Report | Title-level viewing hours | Through Dec 2025 (published Jan 20, 2026) |
| IMDb / TMDb | Genre, format, episode count, ratings | Current |
| Industry cost benchmarks | Category-level production cost bands | Public estimates |
| Netflix Top 10 site | Weekly ranking data | Ongoing |

**Data currency:** Analysis is current through December 2025. The latest Netflix
Engagement Report used was published January 20, 2026, covering July–December 2025.

## 4. Approach

Three analytical lenses, not one simplistic metric:
1. **Viewing Efficiency** — viewing hours / estimated cost (per-episode × episode count, not flat category). Tested under low, base, and high cost assumptions.
2. **Export Value** — rule-based scoring on weeks in Netflix Global Top 10: High (5+), Moderate (2-4), Low (<2). Not manual judgment.
3. **Portfolio Role** — strategic classification derived from efficiency × export value position

## 5. Key Findings

- Anime appears strongest on both viewing efficiency and export value (rankings hold under all cost scenarios)
- Japanese drama serves a local anchor function; export depends heavily on title selection
- Film shows high variability — franchise IP exports well, original films stay domestic
- Reality/unscripted fills domestic catalog needs at low cost but has limited global reach

## 6. Deliverables

- 4-tab Streamlit dashboard
- Transparent metric definitions with documented assumptions
- Content type efficiency comparison
- Export vs. domestic value framework
- Strategic implications for investment discussion

## 7. Limitations

- No actual production budgets — cost proxies are category-level bands
- Viewing hours ≠ subscriber value (retention impact unknown)
- Export value is proxied, not directly measured
- Netflix Engagement Report covers ~99% of viewing but aggregation methodology is Netflix's
- Framework is for structured discussion, not financial decision automation

## 8. How This Would Improve with Internal Data

With internal Netflix data:
- Actual title-level costs → real efficiency calculation
- Retention/acquisition attribution → subscriber value
- Country-level viewing breakdown → precise export measurement
- Marketing spend → full investment picture
- Completion rates → engagement quality beyond hours

## 9. Connection to Companion Project

This project provides the **content investment framework** — how to compare
content types on efficiency, export value, and portfolio role for slate planning.

The companion project, *APAC Streaming Competitive Intelligence*, provides
the market context: what competitive pressures exist in Japan and Korea, and
why APAC markets require locally adjusted analysis frameworks.

Together: **competitive landscape → content investment framework → strategic implications.**
