# Data Assumptions & Metric Definitions

## Sample Scope

**"Japanese content"** is defined as titles meeting ALL of:
1. Primary production country is Japan
2. Primary language is Japanese
3. Appeared in Netflix public engagement data

Excluded: Non-Japanese titles popular in Japan, co-productions where Japan
is not the primary origin.

**Current sample:** 21 titles across 4 content types (Anime 7, Drama 6, Film 3, Reality 5).

## Data Currency

- **Latest Netflix Engagement Report:** Published January 20, 2026
- **Coverage window:** July–December 2025
- **Analysis range:** 2023 H1 through 2025 H2

## Cost Proxy Methodology

We use **category-level cost bands** from public industry benchmarks.
Cost is calculated **per title**, not per category:

- **Series:** per_episode_mid × actual episode count
- **Film:** per_title_mid

| Content Type | Per Episode/Title (USD) | Source |
|---|---|---|
| Anime | $100K–$300K / ep (mid: $200K) | Industry reports, Anime News Network |
| Drama | $500K–$2M / ep (mid: $1M) | Variety, industry benchmarks |
| Film | $5M–$30M / title (mid: $15M) | Press reporting |
| Reality | $100K–$500K / ep (mid: $250K) | Industry benchmarks |

**Sensitivity:** All metrics tested under low (min cost), base (mid), and
high (max cost) assumptions. Rankings are stable across all three scenarios.

## Metric Definitions

### Viewing Efficiency Index (VEI)

**Definition:** Total viewing hours (M) / estimated cost proxy ($M)

**Calculation:** Per-title cost = per_episode_mid × episodes (or per_title_mid for films)

**Sensitivity:** VEI_low = hours / cost_high; VEI_high = hours / cost_low

**What it shows:** Relative viewing attention per estimated cost unit.

**What it does NOT show:** True ROI, subscriber impact, retention value.

### Export Value

**Definition:** Rule-based scoring on Global Top 10 presence:
- High (3): 5+ weeks in Netflix Global Top 10
- Moderate (2): 2-4 weeks
- Low (1): <2 weeks

**Source:** Netflix weekly Global Top 10 data (public).

**What it shows:** Whether a title's engagement extends beyond domestic audience.

**What it does NOT show:** Precise country-level viewership breakdown.

### Portfolio Role Classification

Derived from VEI × Export Value position:
- **Export Engine:** High efficiency + high export
- **Local Anchor:** Moderate efficiency, domestic-focused
- **Selective / High-Variance:** Low average efficiency, outcome depends on individual titles

## Data Reliability Tiers

| Tier | Label | Examples |
|---|---|---|
| 1 | Reported | Netflix Engagement Report viewing hours, Global Top 10 weeks |
| 2 | Market Estimate | IMDb ratings, industry cost benchmarks |
| 3 | Proxy Indicator | Cost band estimates for specific content types |

## What This Data Cannot Tell Us

- Netflix's actual production budgets
- Subscriber acquisition or retention impact per title
- Country-level viewing distribution
- Marketing spend or promotional impact
- Whether a title was supply-constrained or demand-constrained
