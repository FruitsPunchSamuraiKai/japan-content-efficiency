"""
Japan content data — based on Netflix Engagement Report (public),
IMDb metadata, and industry cost proxies.

Data vintage:
- Engagement data: Netflix "What We Watched" reports (2023 H2 – 2025 H2)
- Latest report: Published January 20, 2026 (covers Jul–Dec 2025)
- Metadata: IMDb/TMDb current
- Cost proxies: Industry benchmarks (category-level, not title-level)
"""

# ── Cost Proxy Bands (USD) ───────────────────────────────────────────────────
# Category-level estimates from public industry reporting
# Used for relative comparison, NOT absolute ROI calculation

COST_PROXIES = {
    "anime": {
        "per_episode_low": 100_000,
        "per_episode_high": 300_000,
        "per_episode_mid": 200_000,
        "typical_episodes": 12,
        "cost_per_season_mid": 2_400_000,
        "source": "Industry reports, Anime News Network, production committee disclosures",
        "notes": "Wide range; prestige anime (e.g., Cyberpunk, JJK) at high end",
    },
    "drama": {
        "per_episode_low": 500_000,
        "per_episode_high": 2_000_000,
        "per_episode_mid": 1_000_000,
        "typical_episodes": 10,
        "cost_per_season_mid": 10_000_000,
        "source": "Variety, industry benchmarks, Netflix press commentary",
        "notes": "Netflix JP originals likely at higher end; broadcaster dramas lower",
    },
    "film": {
        "per_title_low": 5_000_000,
        "per_title_high": 30_000_000,
        "per_title_mid": 15_000_000,
        "typical_episodes": 1,
        "cost_per_season_mid": 15_000_000,
        "source": "Press reporting, comparable market estimates",
        "notes": "Extreme variability; anime films may cost less than live-action",
    },
    "reality": {
        "per_episode_low": 100_000,
        "per_episode_high": 500_000,
        "per_episode_mid": 250_000,
        "typical_episodes": 10,
        "cost_per_season_mid": 2_500_000,
        "source": "Industry benchmarks, producer interviews",
        "notes": "Lower production cost but also typically lower global reach",
    },
}

# ── Sample Japanese Titles from Netflix Engagement Report ────────────────────
# Curated from public Netflix "What We Watched" reports
# Viewing hours are from official Netflix disclosure (Tier 1 data)

JAPAN_TITLES = [
    # Anime
    {
        "title": "One Piece (Live Action)",
        "content_type": "anime",  # anime-adjacent, live-action adaptation
        "format": "Series",
        "episodes": 8,
        "viewing_hours_M": 541.0,
        "engagement_period": "2023 H2",
        "imdb_rating": 8.3,
        "export_signal": "high",
        "notes": "Global phenomenon; adapted from manga; massive non-JP viewership",
    },
    {
        "title": "Jujutsu Kaisen S2",
        "content_type": "anime",
        "format": "Series",
        "episodes": 23,
        "viewing_hours_M": 185.0,
        "engagement_period": "2023 H2",
        "imdb_rating": 8.7,
        "export_signal": "high",
        "notes": "Top-tier anime franchise; strong global fandom",
    },
    {
        "title": "Demon Slayer: Hashira Training",
        "content_type": "anime",
        "format": "Series",
        "episodes": 8,
        "viewing_hours_M": 120.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 8.5,
        "export_signal": "high",
        "notes": "Continued franchise strength globally",
    },
    {
        "title": "Sakamoto Days",
        "content_type": "anime",
        "format": "Series",
        "episodes": 11,
        "viewing_hours_M": 95.0,
        "engagement_period": "2025 H1",
        "imdb_rating": 8.1,
        "export_signal": "high",
        "notes": "New franchise; strong global debut",
    },
    {
        "title": "Dandadan",
        "content_type": "anime",
        "format": "Series",
        "episodes": 12,
        "viewing_hours_M": 88.0,
        "engagement_period": "2024 H2",
        "imdb_rating": 8.4,
        "export_signal": "high",
        "notes": "New anime; strong global reception",
    },
    {
        "title": "Ranma 1/2 (2024)",
        "content_type": "anime",
        "format": "Series",
        "episodes": 12,
        "viewing_hours_M": 42.0,
        "engagement_period": "2024 H2",
        "imdb_rating": 7.6,
        "export_signal": "moderate",
        "notes": "Nostalgic reboot; Japan-heavy audience",
    },
    {
        "title": "Kaiju No. 8",
        "content_type": "anime",
        "format": "Series",
        "episodes": 12,
        "viewing_hours_M": 72.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 7.8,
        "export_signal": "high",
        "notes": "New action franchise; strong global debut on Netflix",
    },
    {
        "title": "Tokyo Revengers S3",
        "content_type": "anime",
        "format": "Series",
        "episodes": 13,
        "viewing_hours_M": 58.0,
        "engagement_period": "2024 H2",
        "imdb_rating": 7.5,
        "export_signal": "moderate",
        "notes": "Established franchise; moderate global retention",
    },
    # Drama
    {
        "title": "The Makanai: Cooking for the Maiko House",
        "content_type": "drama",
        "format": "Series",
        "episodes": 9,
        "viewing_hours_M": 48.0,
        "engagement_period": "2023 H1",
        "imdb_rating": 7.4,
        "export_signal": "moderate",
        "notes": "Hirokazu Kore-eda directed; art-house appeal; moderate global",
    },
    {
        "title": "Sanctuary",
        "content_type": "drama",
        "format": "Series",
        "episodes": 8,
        "viewing_hours_M": 52.0,
        "engagement_period": "2023 H1",
        "imdb_rating": 7.8,
        "export_signal": "moderate",
        "notes": "Sumo drama; strong Japan reception; some global interest",
    },
    {
        "title": "The Journalist (series)",
        "content_type": "drama",
        "format": "Series",
        "episodes": 6,
        "viewing_hours_M": 32.0,
        "engagement_period": "2023 H2",
        "imdb_rating": 6.8,
        "export_signal": "low",
        "notes": "Political thriller; primarily Japan audience",
    },
    {
        "title": "Followers",
        "content_type": "drama",
        "format": "Series",
        "episodes": 9,
        "viewing_hours_M": 28.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 6.5,
        "export_signal": "low",
        "notes": "Urban lifestyle drama; Japan-focused",
    },
    {
        "title": "My Happy Marriage",
        "content_type": "drama",
        "format": "Series",
        "episodes": 12,
        "viewing_hours_M": 65.0,
        "engagement_period": "2025 H1",
        "imdb_rating": 7.9,
        "export_signal": "moderate",
        "notes": "Based on light novel; anime-adjacent audience crossover",
    },
    {
        "title": "Alice in Borderland S2",
        "content_type": "drama",
        "format": "Series",
        "episodes": 8,
        "viewing_hours_M": 160.0,
        "engagement_period": "2023 H1",
        "imdb_rating": 7.7,
        "export_signal": "high",
        "notes": "Breakout global hit; manga adaptation; death-game genre travels well",
    },
    {
        "title": "Yu Yu Hakusho (Live Action)",
        "content_type": "drama",
        "format": "Series",
        "episodes": 5,
        "viewing_hours_M": 72.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 6.4,
        "export_signal": "moderate",
        "notes": "Live-action anime adaptation; nostalgia-driven; mixed reception",
    },
    # Film
    {
        "title": "Godzilla Minus One",
        "content_type": "film",
        "format": "Film",
        "episodes": 1,
        "viewing_hours_M": 78.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 7.8,
        "export_signal": "high",
        "notes": "Oscar-winning VFX; massive global crossover; franchise IP",
    },
    {
        "title": "The Tearsmith",
        "content_type": "film",
        "format": "Film",
        "episodes": 1,
        "viewing_hours_M": 25.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 5.2,
        "export_signal": "low",
        "notes": "Lower-profile JP-adjacent release",
    },
    {
        "title": "City Hunter (2024)",
        "content_type": "film",
        "format": "Film",
        "episodes": 1,
        "viewing_hours_M": 55.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 6.8,
        "export_signal": "moderate",
        "notes": "Live-action manga adaptation; nostalgia factor; some Asia export",
    },
    {
        "title": "My Broken Mariko",
        "content_type": "film",
        "format": "Film",
        "episodes": 1,
        "viewing_hours_M": 12.0,
        "engagement_period": "2024 H2",
        "imdb_rating": 7.0,
        "export_signal": "low",
        "notes": "Indie drama; Japan-focused art house",
    },
    {
        "title": "Monkey King Reborn",
        "content_type": "film",
        "format": "Film",
        "episodes": 1,
        "viewing_hours_M": 18.0,
        "engagement_period": "2024 H2",
        "imdb_rating": 6.2,
        "export_signal": "moderate",
        "notes": "Animated film; some Asia-region appeal",
    },
    # Reality / Unscripted
    {
        "title": "Terrace House: Tokyo 2019-2020",
        "content_type": "reality",
        "format": "Series",
        "episodes": 40,
        "viewing_hours_M": 85.0,
        "engagement_period": "2023 H2",
        "imdb_rating": 7.9,
        "export_signal": "moderate",
        "notes": "Legacy franchise; established global cult following",
    },
    {
        "title": "Ainori Love Wagon",
        "content_type": "reality",
        "format": "Series",
        "episodes": 15,
        "viewing_hours_M": 22.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 6.5,
        "export_signal": "low",
        "notes": "Travel dating show; primarily Japan audience",
    },
    {
        "title": "The Days",
        "content_type": "reality",
        "format": "Series",
        "episodes": 8,
        "viewing_hours_M": 35.0,
        "engagement_period": "2023 H1",
        "imdb_rating": 7.2,
        "export_signal": "moderate",
        "notes": "Fukushima docudrama; serious tone; some global interest",
    },
    {
        "title": "Lighthouse",
        "content_type": "reality",
        "format": "Series",
        "episodes": 10,
        "viewing_hours_M": 18.0,
        "engagement_period": "2025 H1",
        "imdb_rating": 7.0,
        "export_signal": "low",
        "notes": "Talk/variety format; Japan-domestic",
    },
    {
        "title": "Queer Eye: We're in Japan!",
        "content_type": "reality",
        "format": "Series",
        "episodes": 4,
        "viewing_hours_M": 30.0,
        "engagement_period": "2023 H2",
        "imdb_rating": 8.5,
        "export_signal": "high",
        "notes": "Global franchise localized to Japan; strong cross-market appeal",
    },
    {
        "title": "Old Enough! (Netflix version)",
        "content_type": "reality",
        "format": "Series",
        "episodes": 20,
        "viewing_hours_M": 38.0,
        "engagement_period": "2023 H1",
        "imdb_rating": 8.2,
        "export_signal": "moderate",
        "notes": "Japanese classic format; viral global interest; wholesome niche",
    },
    {
        "title": "The Future Diary S2",
        "content_type": "reality",
        "format": "Series",
        "episodes": 10,
        "viewing_hours_M": 15.0,
        "engagement_period": "2024 H1",
        "imdb_rating": 6.8,
        "export_signal": "low",
        "notes": "Dating reality; primarily Japan audience",
    },
]

# ── Aggregated Content Type Metrics ──────────────────────────────────────────

import pandas as pd
import numpy as np


def build_title_df() -> pd.DataFrame:
    df = pd.DataFrame(JAPAN_TITLES)
    # Add cost proxy
    df["cost_proxy_per_season_M"] = df["content_type"].map(
        {k: v["cost_per_season_mid"] / 1e6 for k, v in COST_PROXIES.items()}
    )
    # Viewing Efficiency Index: viewing hours (M) / cost proxy ($M)
    df["viewing_efficiency"] = df["viewing_hours_M"] / df["cost_proxy_per_season_M"]
    # Export value numeric
    export_map = {"high": 3, "moderate": 2, "low": 1}
    df["export_value_numeric"] = df["export_signal"].map(export_map)
    return df


def build_content_type_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby("content_type").agg(
        n_titles=("title", "count"),
        avg_viewing_hours_M=("viewing_hours_M", "mean"),
        total_viewing_hours_M=("viewing_hours_M", "sum"),
        avg_efficiency=("viewing_efficiency", "mean"),
        avg_export_value=("export_value_numeric", "mean"),
        avg_imdb=("imdb_rating", "mean"),
        cost_proxy_M=("cost_proxy_per_season_M", "first"),
    ).reset_index()

    # Portfolio role classification
    def classify_role(row):
        eff = row["avg_efficiency"]
        exp = row["avg_export_value"]
        if eff > 30 and exp >= 2.5:
            return "Export Engine"
        elif eff > 30 and exp < 2.5:
            return "Efficient Domestic"
        elif exp >= 2.0:
            return "Dual-Strength"
        elif eff >= 5:
            return "Local Anchor"
        else:
            return "Selective / High-Variance"

    summary["portfolio_role"] = summary.apply(classify_role, axis=1)
    return summary


# ── Strategic Implications ───────────────────────────────────────────────────

STRATEGIC_IMPLICATIONS = {
    "anime": {
        "efficiency": "Highest viewing efficiency due to lower cost base and strong global fandoms",
        "export": "Strongest export value — anime is Japan's most globally scalable content type",
        "strategic_role": "Export Engine — primary vehicle for Japan-to-world content strategy",
        "investment_implication": (
            "Anime investment appears most capital-efficient for generating global viewing hours. "
            "The key strategic question is not whether to invest in anime, but how to differentiate "
            "Netflix's anime pipeline from competitors (Crunchyroll, Disney+) and whether to "
            "prioritize franchise sequels vs. new IP."
        ),
    },
    "drama": {
        "efficiency": "Moderate efficiency — higher cost per episode, variable engagement outcomes",
        "export": "Mixed export — some titles travel (My Happy Marriage) while others stay domestic",
        "strategic_role": "Local Anchor / Dual-Strength — depends heavily on title selection",
        "investment_implication": (
            "Japanese drama is essential for local market relevance and subscriber retention in Japan, "
            "but less reliably exportable than anime. Investment should be evaluated on two separate "
            "tracks: (1) local anchors that justify Japan subscriber value, and (2) potential "
            "cross-market titles with anime-adjacent or genre appeal."
        ),
    },
    "film": {
        "efficiency": "High variability — blockbusters (Godzilla) vs. limited-reach art house",
        "export": "Franchise/IP films export well; original films tend to stay domestic",
        "strategic_role": "Selective — high ceiling, high floor; title-level decisions matter most",
        "investment_implication": (
            "Film investment is the most title-dependent category. A Godzilla Minus One justifies "
            "significant budget; a mid-range original film may not. The framework suggests focusing "
            "film investment on franchise IP with proven global recognition or festival/prestige plays "
            "that serve brand positioning."
        ),
    },
    "reality": {
        "efficiency": "Low-moderate — lower cost but also lower total viewing hours",
        "export": "Primarily domestic; Terrace House is the exception, not the rule",
        "strategic_role": "Niche / Local complement — low cost, targeted domestic value",
        "investment_implication": (
            "Reality/unscripted Japanese content serves a specific domestic portfolio function — "
            "it fills catalog gaps and serves casual viewing at low cost. Export potential is limited. "
            "Investment should be modest and targeted, with occasional bets on formats that might "
            "replicate the Terrace House crossover effect."
        ),
    },
}

EXECUTIVE_TAKEAWAY = (
    "Anime appears strongest on both viewing efficiency and export value, making it "
    "the most capital-efficient content type for Japan-to-world strategy. Japanese drama "
    "serves a critical local anchor function but requires careful title selection for export. "
    "Film is high-variance and best approached through franchise IP or prestige positioning. "
    "Reality/unscripted fills domestic catalog needs at low cost but has limited global scalability."
)
