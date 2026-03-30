"""
Japan Content Investment Efficiency & Export Value Framework
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data.content_data import (
    COST_PROXIES, JAPAN_TITLES,
    build_title_df, build_content_type_summary,
    STRATEGIC_IMPLICATIONS, EXECUTIVE_TAKEAWAY,
)

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Japan Content Investment Efficiency",
    page_icon="🎬",
    layout="wide",
)

st.title("Japan Content Investment Efficiency & Export Value Framework")
st.caption(
    "External-data-based content strategy analytics | "
    "Netflix Engagement Report + public metadata + transparent cost proxies"
)

# ── Data ─────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = build_title_df()
    summary = build_content_type_summary(df)
    return df, summary

df_titles, df_summary = load_data()

TYPE_COLORS = {
    "anime": "#e45756",
    "drama": "#4c78a8",
    "film": "#f58518",
    "reality": "#72b7b2",
}

TYPE_LABELS = {
    "anime": "Anime",
    "drama": "Drama",
    "film": "Film",
    "reality": "Reality / Unscripted",
}

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Summary",
    "Content Type Efficiency",
    "Export Value & Reach",
    "Strategic Implications",
])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1: EXECUTIVE SUMMARY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab1:
    st.header("Executive Summary")
    st.markdown("*Understand Japan content efficiency in 60 seconds*")

    # Find key stats
    most_efficient = df_summary.loc[df_summary["avg_efficiency"].idxmax()]
    highest_export = df_summary.loc[df_summary["avg_export_value"].idxmax()]
    most_domestic = df_summary.loc[df_summary["avg_export_value"].idxmin()]
    highest_viewing = df_summary.loc[df_summary["total_viewing_hours_M"].idxmax()]

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Most Efficient Type",
            TYPE_LABELS[most_efficient["content_type"]],
            f"VEI: {most_efficient['avg_efficiency']:.0f}",
        )
    with col2:
        st.metric(
            "Strongest Export Value",
            TYPE_LABELS[highest_export["content_type"]],
            f"Score: {highest_export['avg_export_value']:.1f}/3",
        )
    with col3:
        st.metric(
            "Most Domestically Concentrated",
            TYPE_LABELS[most_domestic["content_type"]],
            f"Score: {most_domestic['avg_export_value']:.1f}/3",
        )
    with col4:
        st.metric(
            "Titles Analyzed",
            len(df_titles),
            f"across {len(df_summary)} content types",
        )

    st.divider()

    # Content type overview chart
    st.subheader("Content Type Overview")

    fig_overview = px.scatter(
        df_summary,
        x="avg_efficiency",
        y="avg_export_value",
        size="total_viewing_hours_M",
        color="content_type",
        color_discrete_map=TYPE_COLORS,
        text=df_summary["content_type"].map(TYPE_LABELS),
        labels={
            "avg_efficiency": "Viewing Efficiency Index (avg)",
            "avg_export_value": "Export Value (1=Low, 3=High)",
            "total_viewing_hours_M": "Total Viewing Hours (M)",
        },
    )
    fig_overview.update_traces(textposition="top center", textfont_size=12)
    fig_overview.update_layout(
        height=420,
        showlegend=False,
        xaxis=dict(title="Viewing Efficiency Index (higher = more efficient)"),
        yaxis=dict(title="Export Value (higher = more global)", range=[0.5, 3.5]),
    )
    st.plotly_chart(fig_overview, use_container_width=True)
    st.caption(
        "Bubble size = total viewing hours. Viewing Efficiency = viewing hours / "
        "category cost proxy. Export Value scored 1–3 based on global engagement signals."
    )

    st.divider()

    # Takeaway
    st.subheader("Investment Discussion Takeaway")
    st.info(EXECUTIVE_TAKEAWAY)

    st.caption(
        "Data current through December 2025 (Netflix Engagement Report published "
        "January 20, 2026). Cost proxies are category-level industry benchmarks, "
        "not actual Netflix production budgets."
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2: CONTENT TYPE EFFICIENCY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab2:
    st.header("Content Type Efficiency Analysis")
    st.markdown(
        "How much viewing attention does each content type generate relative "
        "to its estimated cost?"
    )

    # Efficiency by content type (bar)
    st.subheader("Average Viewing Efficiency by Content Type")
    df_eff = df_summary.sort_values("avg_efficiency", ascending=True)
    fig_eff = px.bar(
        df_eff,
        x="avg_efficiency",
        y=df_eff["content_type"].map(TYPE_LABELS),
        orientation="h",
        color="content_type",
        color_discrete_map=TYPE_COLORS,
        labels={"avg_efficiency": "Viewing Efficiency Index", "y": ""},
    )
    fig_eff.update_layout(height=300, showlegend=False)
    st.plotly_chart(fig_eff, use_container_width=True)

    # Title-level scatter
    st.subheader("Title-Level Efficiency Matrix")
    st.markdown("Each point is a title. Position shows cost proxy vs viewing hours.")

    fig_titles = px.scatter(
        df_titles,
        x="cost_proxy_per_season_M",
        y="viewing_hours_M",
        color="content_type",
        color_discrete_map=TYPE_COLORS,
        text="title",
        size=[15] * len(df_titles),
        labels={
            "cost_proxy_per_season_M": "Cost Proxy per Season ($M)",
            "viewing_hours_M": "Viewing Hours (M)",
            "content_type": "Content Type",
        },
    )
    fig_titles.update_traces(textposition="top right", textfont_size=9)
    fig_titles.update_layout(
        height=500,
        legend=dict(orientation="h", y=1.1),
    )
    # Add efficiency reference lines
    for eff_line in [10, 25, 50]:
        x_vals = [0, 20]
        y_vals = [0, 20 * eff_line]
        fig_titles.add_trace(go.Scatter(
            x=x_vals, y=y_vals,
            mode="lines",
            line=dict(dash="dot", color="gray", width=1),
            name=f"VEI={eff_line}",
            showlegend=True if eff_line == 25 else False,
        ))
    st.plotly_chart(fig_titles, use_container_width=True)
    st.caption(
        "Dotted lines show constant efficiency levels. Titles above and to the left "
        "are more efficient (more viewing per dollar). Cost proxy is category midpoint, "
        "not title-specific budget."
    )

    # Cost proxy table
    st.subheader("Cost Proxy Reference")
    cost_data = []
    for ctype, proxy in COST_PROXIES.items():
        cost_data.append({
            "Content Type": TYPE_LABELS.get(ctype, ctype),
            "Cost Band (per ep/title)": f"${proxy.get('per_episode_low', proxy.get('per_title_low', 0)):,.0f} – ${proxy.get('per_episode_high', proxy.get('per_title_high', 0)):,.0f}",
            "Midpoint Used": f"${proxy.get('per_episode_mid', proxy.get('per_title_mid', 0)):,.0f}",
            "Typical Season Cost": f"${proxy['cost_per_season_mid']:,.0f}",
            "Source": proxy["source"],
        })
    st.dataframe(pd.DataFrame(cost_data), use_container_width=True, hide_index=True)

    st.caption(
        "These are category-level cost bands from public industry reporting. "
        "Actual Netflix production costs are not publicly available and likely vary "
        "significantly by title."
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3: EXPORT VALUE & REACH
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab3:
    st.header("Export Value & Domestic vs Global Reach")
    st.markdown(
        "Not all valuable content exports equally. This analysis separates "
        "domestic strength from global scalability."
    )

    # Domestic vs Export quadrant
    st.subheader("Content Positioning: Efficiency × Export Value")

    fig_quad = px.scatter(
        df_titles,
        x="viewing_efficiency",
        y="export_value_numeric",
        color="content_type",
        color_discrete_map=TYPE_COLORS,
        text="title",
        labels={
            "viewing_efficiency": "Viewing Efficiency Index",
            "export_value_numeric": "Export Value (1=Low, 3=High)",
        },
    )
    fig_quad.update_traces(textposition="top right", textfont_size=9)

    # Add quadrant lines
    median_eff = df_titles["viewing_efficiency"].median()
    fig_quad.add_hline(y=2, line_dash="dash", line_color="gray", opacity=0.5)
    fig_quad.add_vline(x=median_eff, line_dash="dash", line_color="gray", opacity=0.5)

    # Quadrant labels
    fig_quad.add_annotation(x=median_eff * 2.5, y=2.8, text="Export Engine",
                            showarrow=False, font=dict(color="gray", size=11))
    fig_quad.add_annotation(x=median_eff * 0.3, y=2.8, text="Premium Export",
                            showarrow=False, font=dict(color="gray", size=11))
    fig_quad.add_annotation(x=median_eff * 2.5, y=1.2, text="Efficient Domestic",
                            showarrow=False, font=dict(color="gray", size=11))
    fig_quad.add_annotation(x=median_eff * 0.3, y=1.2, text="Niche / Local",
                            showarrow=False, font=dict(color="gray", size=11))

    fig_quad.update_layout(
        height=500,
        legend=dict(orientation="h", y=1.1),
    )
    st.plotly_chart(fig_quad, use_container_width=True)

    # Export breakdown by type
    st.subheader("Export Signal Distribution by Content Type")

    export_counts = df_titles.groupby(["content_type", "export_signal"]).size().reset_index(name="count")
    export_order = {"high": 3, "moderate": 2, "low": 1}
    export_counts["sort"] = export_counts["export_signal"].map(export_order)
    export_counts = export_counts.sort_values("sort")

    fig_export = px.bar(
        export_counts,
        x=export_counts["content_type"].map(TYPE_LABELS),
        y="count",
        color="export_signal",
        color_discrete_map={"high": "#2ca02c", "moderate": "#f58518", "low": "#d62728"},
        barmode="stack",
        labels={"x": "", "count": "Number of Titles", "export_signal": "Export Signal"},
    )
    fig_export.update_layout(height=350)
    st.plotly_chart(fig_export, use_container_width=True)

    # Comparison table
    st.subheader("Content Type Export Profile")
    export_table = []
    for _, row in df_summary.iterrows():
        ctype = row["content_type"]
        impl = STRATEGIC_IMPLICATIONS[ctype]
        export_table.append({
            "Content Type": TYPE_LABELS[ctype],
            "Avg Export Score": f"{row['avg_export_value']:.1f}/3",
            "Export Assessment": impl["export"],
            "Portfolio Role": row["portfolio_role"],
        })
    st.dataframe(pd.DataFrame(export_table), use_container_width=True, hide_index=True)

    st.divider()
    st.markdown(
        "**Key insight:** Export value and viewing efficiency are correlated but "
        "not identical. Anime scores highest on both dimensions. Drama shows the "
        "widest spread — some titles export well while others are purely domestic. "
        "Content strategy must evaluate titles on both axes, not just one."
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4: STRATEGIC IMPLICATIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab4:
    st.header("Strategic Implications — Investment Discussion Framework")
    st.markdown(
        "How could a strategy or finance team use this framework in a content "
        "investment discussion?"
    )

    # Portfolio discussion grid
    st.subheader("Content Portfolio Discussion Grid")

    grid_data = []
    for ctype, impl in STRATEGIC_IMPLICATIONS.items():
        row = df_summary[df_summary["content_type"] == ctype].iloc[0]
        grid_data.append({
            "Content Type": TYPE_LABELS[ctype],
            "Viewing Efficiency": f"{row['avg_efficiency']:.0f}",
            "Export Value": f"{row['avg_export_value']:.1f}/3",
            "Portfolio Role": row["portfolio_role"],
            "Strategic Implication": impl["investment_implication"][:120] + "...",
        })
    st.dataframe(pd.DataFrame(grid_data), use_container_width=True, hide_index=True)

    # Detailed implications by type
    for ctype in ["anime", "drama", "film", "reality"]:
        impl = STRATEGIC_IMPLICATIONS[ctype]
        st.subheader(f"{TYPE_LABELS[ctype]}")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**Efficiency:** {impl['efficiency']}")
            st.markdown(f"**Export:** {impl['export']}")
        with col_b:
            st.markdown(f"**Role:** {impl['strategic_role']}")
        st.info(impl["investment_implication"])

    # Framework notes
    st.divider()
    st.subheader("Why One Metric Is Not Enough")
    st.markdown("""
Content investment cannot be evaluated by viewing hours alone, or by cost efficiency
alone, or by export value alone. Each metric answers a different question:

- **Viewing Efficiency** answers: "How much attention does this generate per dollar?"
- **Export Value** answers: "Does this content travel beyond Japan?"
- **Portfolio Role** answers: "What strategic function does this serve in the slate?"

A title like Terrace House may score low on export value and moderate on efficiency,
but it fills a specific domestic catalog function that no anime blockbuster can replace.
Conversely, investing only in high-efficiency anime would leave the Japan domestic slate
thin on variety and drama — risking subscriber retention among audiences who value those formats.

**The framework's value is in structuring the discussion, not in producing a single ranking.**
    """)

    st.divider()
    st.caption(
        "Data current through December 2025. Cost proxies are category-level estimates. "
        "This framework is designed for investment discussion, not financial decision automation. "
        "Internal data would significantly improve precision (see README §8)."
    )

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### About This Framework")
    st.markdown(
        "**Japan Content Investment Efficiency**\n\n"
        "Evaluates Japanese content across four types using:\n"
        "1. Viewing efficiency (hours / cost proxy)\n"
        "2. Export value (global vs domestic signal)\n"
        "3. Portfolio role classification\n\n"
        "Built to demonstrate content strategy analytics "
        "capability for investment discussion."
    )
    st.markdown("---")
    st.markdown("### Data Currency")
    st.markdown(
        "- **Netflix Engagement Report:** Through Dec 2025\n"
        "- **Published:** January 20, 2026\n"
        "- **Metadata:** IMDb/TMDb current\n"
        "- **Cost proxies:** Industry benchmarks"
    )
    st.markdown("---")
    st.markdown("### Key Principle")
    st.markdown(
        "This is NOT an ROI model. It is a **framework for structuring "
        "content investment discussions** using transparent external data "
        "and clearly labeled assumptions."
    )
    st.markdown("---")
    st.markdown("### Limitations")
    st.markdown(
        "- No actual production budgets\n"
        "- Category-level cost proxies only\n"
        "- Export value is proxy-based\n"
        "- Japan titles only (MVP)\n"
        "- See README §7"
    )
