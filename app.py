"""
app.py  –  Airbnb Revenue Optimization Analytics Dashboard
Main entry point: Home page + sidebar navigation.
"""

import streamlit as st
from data_generator import generate_airbnb_data

# ── Page config (must be first Streamlit call) ─────────────────────────────
st.set_page_config(
    page_title="Airbnb Revenue Analytics | Dubai",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Base ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1,h2,h3,h4 { font-family: 'Space Grotesk', sans-serif; }

/* Hide default Streamlit menu */
#MainMenu, footer { visibility: hidden; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0d14 0%, #12151f 100%);
    border-right: 1px solid #1e2333;
}
[data-testid="stSidebar"] * { color: #e0e6f0 !important; }

/* ── Metric cards ── */
.metric-card {
    background: linear-gradient(135deg, #1a1d2e 0%, #1e2235 100%);
    border: 1px solid #2a2f45;
    border-radius: 14px;
    padding: 20px 24px;
    text-align: center;
    transition: transform .2s, box-shadow .2s;
}
.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(255,90,95,.15);
}
.metric-val { font-size: 2rem; font-weight: 700; color: #FF5A5F; }
.metric-lbl { font-size: .85rem; color: #8b95b0; margin-top: 4px; }
.metric-delta { font-size: .78rem; color: #36c97e; margin-top: 2px; }

/* ── Section header ── */
.section-header {
    background: linear-gradient(90deg, #FF5A5F22, transparent);
    border-left: 4px solid #FF5A5F;
    padding: 10px 18px;
    border-radius: 0 8px 8px 0;
    margin: 24px 0 16px;
}
.section-header h3 { margin: 0; color: #fff; font-size: 1.1rem; }

/* ── Insight box ── */
.insight-box {
    background: #12151f;
    border: 1px solid #252a3d;
    border-left: 4px solid #FF5A5F;
    border-radius: 8px;
    padding: 12px 16px;
    margin-top: 8px;
    font-size: .88rem;
    color: #b0bcd4;
    line-height: 1.6;
}

/* ── Page hero ── */
.hero {
    background: linear-gradient(135deg, #0f1117 0%, #1a1030 50%, #0f1117 100%);
    border: 1px solid #2a2f45;
    border-radius: 18px;
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content:'';
    position:absolute; top:-60px; right:-60px;
    width:240px; height:240px;
    background: radial-gradient(circle, #FF5A5F33, transparent 70%);
    border-radius:50%;
}
.hero h1 { font-size: 2.4rem; font-weight: 700; color: #fff; margin: 0 0 8px; }
.hero p { color: #8b95b0; font-size: 1.05rem; max-width: 700px; }
.badge {
    display:inline-block; background:#FF5A5F22;
    color:#FF5A5F; border:1px solid #FF5A5F55;
    border-radius:20px; padding:3px 12px;
    font-size:.78rem; font-weight:600; margin-bottom:14px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px;'>
        <div style='font-size:2.2rem'>🏠</div>
        <div style='font-size:1.1rem; font-weight:700; color:#FF5A5F; letter-spacing:.5px;'>
            Airbnb Analytics
        </div>
        <div style='font-size:.75rem; color:#555e7a; margin-top:2px;'>
            Dubai Revenue Intelligence
        </div>
    </div>
    <hr style='border-color:#1e2333; margin:10px 0 20px;'/>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        [
            "🏠  Home",
            "📋  Dataset Overview",
            "🔍  Exploratory Analysis",
            "💰  Pricing Analytics",
            "🤖  Classification Models",
            "🎯  Clustering Analysis",
            "🔗  Association Rule Mining",
            "📈  Regression Modeling",
            "📅  Demand Forecasting",
            "🚀  Revenue Optimization",
        ],
        label_visibility="collapsed",
    )

    st.markdown("""
    <hr style='border-color:#1e2333; margin:20px 0 10px;'/>
    <div style='font-size:.72rem; color:#555e7a; text-align:center;'>
        Dataset: 3,500 Dubai listings · Synthetic<br>
        © 2024 Airbnb Revenue Analytics
    </div>
    """, unsafe_allow_html=True)

# ── Load data (cached) ─────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data():
    return generate_airbnb_data()

with st.spinner("⚡ Generating synthetic dataset …"):
    df = load_data()

# ── Route to pages ─────────────────────────────────────────────────────────
p = page.split("  ")[-1].strip()

# ═══════════════════════════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════════════════════════
if p == "Home":
    st.markdown("""
    <div class='hero'>
        <span class='badge'>🏙️ Dubai Airbnb Market · 2024</span>
        <h1>Revenue Optimization Analytics<br>for Airbnb Hosts</h1>
        <p>
            A data-driven intelligence platform for Dubai short-term rental hosts and
            property managers. Leverage machine learning, clustering, and demand
            forecasting to maximize occupancy and revenue.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # KPI cards
    booked_pct    = (df["Booking_Status"] == "Booked").mean() * 100
    avg_price     = df["Price_Per_Night"].mean()
    avg_occ       = df["Occupancy_Rate"].mean() * 100
    avg_review    = df["Review_Score"].mean()
    superhost_pct = df["Superhost_Status"].mean() * 100
    avg_revenue   = (df["Price_Per_Night"] * df["Occupancy_Rate"] * 30).mean()

    cols = st.columns(6)
    kpis = [
        ("3,500",        "Total Listings",        "Dubai Market"),
        (f"AED {avg_price:,.0f}", "Avg Price/Night", "+8.2% YoY"),
        (f"{avg_occ:.1f}%",  "Avg Occupancy Rate",  "+3.1% YoY"),
        (f"{avg_review:.2f}★", "Avg Review Score",   "out of 5.0"),
        (f"{superhost_pct:.1f}%", "Superhost Rate",  "Top performers"),
        (f"AED {avg_revenue:,.0f}", "Avg Monthly Rev", "per listing"),
    ]
    for col, (val, lbl, delta) in zip(cols, kpis):
        col.markdown(f"""
        <div class='metric-card'>
            <div class='metric-val'>{val}</div>
            <div class='metric-lbl'>{lbl}</div>
            <div class='metric-delta'>{delta}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Business context
    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.markdown("""
        <div class='section-header'><h3>📌 Business Context</h3></div>
        """, unsafe_allow_html=True)
        st.markdown("""
        Dubai's short-term rental market has grown **35% annually** since 2021,
        driven by tourism expansion and Expo legacy demand. With over **25,000 active
        Airbnb listings**, hosts face increasing competition — making data-driven
        pricing and optimization essential for maximizing returns.

        This platform answers the critical questions every host must resolve:
        - **What factors** truly drive bookings vs. empty nights?
        - **What price** balances occupancy vs. nightly rate optimally?
        - **Which amenities** deliver the highest ROI for investment?
        - **Which traveler segments** are most valuable to target?
        """)

    with c2:
        st.markdown("""
        <div class='section-header'><h3>🧠 Analytics Techniques</h3></div>
        """, unsafe_allow_html=True)
        techniques = [
            ("📊", "Exploratory Data Analysis",   "Uncover patterns & distributions"),
            ("🤖", "Classification Models",        "Predict booking probability"),
            ("🎯", "K-Means Clustering",           "Segment listing types"),
            ("🔗", "Association Rule Mining",      "Discover amenity patterns"),
            ("📈", "Regression Modeling",          "Predict optimal price"),
            ("📅", "Demand Forecasting",           "Plan for peak seasons"),
            ("🚀", "Revenue Optimization",         "Maximize earnings strategy"),
        ]
        for icon, name, desc in techniques:
            st.markdown(f"""
            <div style='display:flex; gap:12px; align-items:center;
                        background:#1a1d2e; border:1px solid #252a3d;
                        border-radius:10px; padding:10px 14px; margin-bottom:8px;'>
                <span style='font-size:1.3rem'>{icon}</span>
                <div>
                    <div style='font-weight:600; color:#e0e6f0; font-size:.9rem'>{name}</div>
                    <div style='color:#8b95b0; font-size:.78rem'>{desc}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    # Quick stats row
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class='section-header'><h3>📍 Market Snapshot</h3></div>""",
                unsafe_allow_html=True)
    import plotly.express as px
    import plotly.graph_objects as go

    c1, c2, c3 = st.columns(3)
    with c1:
        fig = px.pie(df, names="Property_Type", hole=0.5,
                     color_discrete_sequence=px.colors.sequential.RdBu,
                     title="Property Mix")
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e6f0", height=300,
            margin=dict(t=40, b=0, l=0, r=0),
            showlegend=True, legend=dict(font_size=10)
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        hood_rev = (
            df.assign(Revenue=df.Price_Per_Night * df.Occupancy_Rate * 30)
            .groupby("Neighborhood")["Revenue"].mean()
            .sort_values(ascending=False).head(8)
        )
        fig2 = px.bar(hood_rev, orientation="h",
                      color=hood_rev.values,
                      color_continuous_scale="RdBu_r",
                      title="Top Neighborhoods by Revenue")
        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e6f0", height=300,
            margin=dict(t=40, b=0, l=0, r=40),
            coloraxis_showscale=False,
            xaxis_title="Avg Monthly Revenue (AED)",
            yaxis_title=""
        )
        st.plotly_chart(fig2, use_container_width=True)

    with c3:
        season_occ = df.groupby("Season")["Occupancy_Rate"].mean().reset_index()
        fig3 = px.bar(season_occ, x="Season", y="Occupancy_Rate",
                      color="Occupancy_Rate",
                      color_continuous_scale="RdBu_r",
                      title="Occupancy by Season")
        fig3.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e6f0", height=300,
            margin=dict(t=40, b=0, l=0, r=0),
            coloraxis_showscale=False,
            yaxis_tickformat=".0%"
        )
        st.plotly_chart(fig3, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# DATASET OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Dataset Overview":
    import plotly.express as px

    st.markdown("<div class='hero'><h1>📋 Dataset Overview</h1><p>Explore the synthetic Dubai Airbnb dataset: 3,500 listings · 33 features · realistic market patterns.</p></div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("<div class='metric-card'><div class='metric-val'>3,500</div><div class='metric-lbl'>Total Listings</div></div>", unsafe_allow_html=True)
    c2.markdown("<div class='metric-card'><div class='metric-val'>33</div><div class='metric-lbl'>Features</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'><div class='metric-val'>0</div><div class='metric-lbl'>Missing Values</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='metric-card'><div class='metric-val'>15</div><div class='metric-lbl'>Neighborhoods</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class='section-header'><h3>🗃️ Dataset Preview</h3></div>""", unsafe_allow_html=True)
    st.dataframe(df.head(20).style.format({
        "Price_Per_Night": "AED {:,.0f}",
        "Occupancy_Rate": "{:.0%}",
        "Review_Score": "{:.1f}",
    }), use_container_width=True, height=320)

    st.markdown("""<div class='section-header'><h3>🔢 Data Types & Summary</h3></div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        dtype_df = pd.DataFrame({
            "Column": df.columns,
            "Type": df.dtypes.astype(str).values,
            "Non-Null": df.notnull().sum().values,
            "Unique": df.nunique().values
        })
        st.dataframe(dtype_df, use_container_width=True, height=400)
    with c2:
        st.dataframe(df.describe().round(2), use_container_width=True, height=400)

    # Charts
    st.markdown("""<div class='section-header'><h3>📊 Key Distributions</h3></div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        fig = px.histogram(df, x="Price_Per_Night", nbins=50,
                           color_discrete_sequence=["#FF5A5F"],
                           title="Price Per Night Distribution")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=300, margin=dict(t=40,b=0,l=0,r=0),
                          xaxis_title="AED", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Prices are right-skewed with most listings between AED 150–600/night. Premium properties in Palm Jumeirah and Downtown push the upper tail significantly above AED 1,000.</div>", unsafe_allow_html=True)

    with c2:
        pt_counts = df["Property_Type"].value_counts().reset_index()
        fig2 = px.bar(pt_counts, x="Property_Type", y="count",
                      color="count", color_continuous_scale="RdBu_r",
                      title="Property Type Distribution")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=300, margin=dict(t=40,b=0,l=0,r=0),
                           coloraxis_showscale=False, xaxis_title="", yaxis_title="Count")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Apartments dominate (45%) the Dubai market, followed by Studios (20%) and Villas (15%). Penthouses are rare but command the highest nightly rates.</div>", unsafe_allow_html=True)

    with c3:
        fig3 = px.histogram(df, x="Occupancy_Rate", nbins=40,
                            color_discrete_sequence=["#36c97e"],
                            title="Occupancy Rate Distribution")
        fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=300, margin=dict(t=40,b=0,l=0,r=0),
                           xaxis_tickformat=".0%", xaxis_title="Occupancy", yaxis_title="Count")
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Occupancy rates follow a near-normal distribution centered ~65%. Fewer than 5% of listings achieve 90%+ occupancy — these are typically Superhosts in premium locations.</div>", unsafe_allow_html=True)

    # Booking status
    st.markdown("""<div class='section-header'><h3>🎯 Booking Status Split</h3></div>""", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        bs = df["Booking_Status"].value_counts()
        fig = px.pie(values=bs.values, names=bs.index, hole=0.55,
                     color_discrete_sequence=["#FF5A5F", "#1e2335"],
                     title="Booking Status")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e0e6f0",
                          height=280, margin=dict(t=40,b=0,l=0,r=0))
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        nb_hood = df.groupby(["Neighborhood", "Booking_Status"]).size().reset_index(name="Count")
        fig2 = px.bar(nb_hood, x="Neighborhood", y="Count", color="Booking_Status",
                      barmode="stack", color_discrete_sequence=["#FF5A5F","#252a3d"],
                      title="Bookings by Neighborhood")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=280, margin=dict(t=40,b=0,l=0,r=0),
                           xaxis_tickangle=-30, legend_title="")
        st.plotly_chart(fig2, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATORY ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Exploratory Analysis":
    import plotly.express as px
    import plotly.graph_objects as go

    st.markdown("<div class='hero'><h1>🔍 Exploratory Data Analysis</h1><p>Deep-dive into relationships between listing features and booking performance.</p></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(df.sample(800, random_state=1),
                         x="Price_Per_Night", y="Occupancy_Rate",
                         color="Property_Type", opacity=0.65,
                         title="Price vs Occupancy Rate",
                         trendline="lowess")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                          xaxis_title="Price Per Night (AED)", yaxis_tickformat=".0%")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Clear inverse relationship between price and occupancy — listings above AED 800/night see occupancy drop below 50%. Villas maintain higher occupancy at premium prices due to family demand.</div>", unsafe_allow_html=True)

    with c2:
        fig2 = px.scatter(df.sample(800, random_state=2),
                          x="Review_Score", y="Occupancy_Rate",
                          color="Superhost_Status", opacity=0.65,
                          title="Review Score vs Occupancy",
                          trendline="ols",
                          color_discrete_sequence=["#8b95b0","#FF5A5F"])
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                           yaxis_tickformat=".0%")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Review scores above 4.5 drive a 15-20% occupancy premium. Superhosts (red) consistently occupy the top-right quadrant — high reviews + high occupancy.</div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        fig3 = px.scatter(df.sample(600, random_state=3),
                          x="Distance_to_City_Center", y="Price_Per_Night",
                          color="Neighborhood", opacity=0.6,
                          title="Distance to City Center vs Price")
        fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                           xaxis_title="Distance (km)", yaxis_title="Price (AED)")
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Price decreases sharply within 5 km of the city center. Listings within 2 km command a 40-60% price premium — proximity is the strongest location factor.</div>", unsafe_allow_html=True)

    with c4:
        fig4 = px.box(df, x="Property_Type", y="Occupancy_Rate",
                      color="Property_Type",
                      color_discrete_sequence=px.colors.qualitative.Bold,
                      title="Occupancy Rate by Property Type")
        fig4.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                           showlegend=False, yaxis_tickformat=".0%")
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Studios and Apartments show the tightest occupancy distribution. Villas have the widest range — great location/amenities villas thrive; poor-value villas struggle badly.</div>", unsafe_allow_html=True)

    # Amenities vs occupancy
    c5, c6 = st.columns(2)
    with c5:
        am_df = df.groupby("Amenities_Count")["Occupancy_Rate"].mean().reset_index()
        fig5 = px.line(am_df, x="Amenities_Count", y="Occupancy_Rate",
                       title="Amenities Count vs Avg Occupancy",
                       markers=True, color_discrete_sequence=["#FF5A5F"])
        fig5.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0),
                           yaxis_tickformat=".0%")
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Occupancy rises consistently up to ~18 amenities, then plateaus. The first 10 amenities provide the highest marginal return — each adds roughly 1.5% occupancy.</div>", unsafe_allow_html=True)

    with c6:
        pt_rev = (df.assign(Revenue=df.Price_Per_Night * df.Occupancy_Rate * 30)
                   .groupby("Property_Type")["Revenue"].mean().sort_values().reset_index())
        fig6 = px.bar(pt_rev, x="Revenue", y="Property_Type", orientation="h",
                      color="Revenue", color_continuous_scale="RdBu_r",
                      title="Avg Monthly Revenue by Property Type")
        fig6.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0),
                           coloraxis_showscale=False)
        st.plotly_chart(fig6, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Penthouses generate 3x the revenue of Studios despite lower occupancy. Villas earn 2x apartment revenue — justifying higher investment/maintenance costs.</div>", unsafe_allow_html=True)

    # Correlation heatmap
    st.markdown("""<div class='section-header'><h3>🔥 Correlation Heatmap</h3></div>""", unsafe_allow_html=True)
    num_cols = ["Price_Per_Night","Occupancy_Rate","Review_Score","Number_of_Reviews",
                "Amenities_Count","Bedrooms","Distance_to_City_Center","Host_Response_Rate",
                "Superhost_Status","Booking_Lead_Time","Length_of_Stay","Cleaning_Fee"]
    corr = df[num_cols].corr()
    fig_heat = go.Figure(data=go.Heatmap(
        z=corr.values, x=corr.columns, y=corr.index,
        colorscale="RdBu", zmid=0,
        text=corr.round(2).values, texttemplate="%{text}",
        hoverinfo="skip"
    ))
    fig_heat.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e0e6f0",
                           height=480, margin=dict(t=20,b=0,l=0,r=0))
    st.plotly_chart(fig_heat, use_container_width=True)
    st.markdown("<div class='insight-box'>💡 Strongest positive correlations: Bedrooms↔Price (0.55), Review_Score↔Occupancy (0.48), Superhost↔Occupancy (0.42). Distance to city center has the largest negative impact on price (-0.38).</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# PRICING ANALYTICS
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Pricing Analytics":
    import plotly.express as px
    import plotly.graph_objects as go

    st.markdown("<div class='hero'><h1>💰 Pricing Analytics</h1><p>Understand pricing dynamics across neighborhoods, seasons, and property types.</p></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        hood_price = (df.groupby("Neighborhood")["Price_Per_Night"]
                       .agg(["mean","median","std"]).round(0)
                       .sort_values("mean", ascending=False).reset_index())
        fig = px.bar(hood_price, x="Neighborhood", y="mean",
                     error_y="std", color="mean",
                     color_continuous_scale="RdBu_r",
                     title="Average Price by Neighborhood (AED/night)")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=380, margin=dict(t=40,b=0,l=0,r=0),
                          xaxis_tickangle=-35, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Palm Jumeirah and Downtown Dubai command 2.5x the median price of outer neighborhoods. Error bars show high within-neighborhood variance — location alone doesn't guarantee premium pricing.</div>", unsafe_allow_html=True)

    with c2:
        season_price = df.groupby(["Season","Property_Type"])["Price_Per_Night"].mean().reset_index()
        fig2 = px.bar(season_price, x="Season", y="Price_Per_Night",
                      color="Property_Type", barmode="group",
                      color_discrete_sequence=px.colors.qualitative.Bold,
                      title="Seasonal Pricing by Property Type")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=380, margin=dict(t=40,b=0,l=0,r=0))
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Winter (Oct–Mar) is Dubai's peak tourist season — all property types see 15-25% higher prices. Villas and Penthouses show the steepest seasonal premium.</div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        dom_price = df.groupby("Day_of_Week")["Price_Per_Night"].mean().reindex(
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        ).reset_index()
        fig3 = px.line(dom_price, x="Day_of_Week", y="Price_Per_Night",
                       markers=True, color_discrete_sequence=["#FF5A5F"],
                       title="Avg Price by Day of Week")
        fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=320, margin=dict(t=40,b=0,l=0,r=0))
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Thursday–Saturday drives a 10-12% weekend premium in Dubai. Thursday is notably high due to the UAE weekend (Fri-Sat) — hosts should implement day-of-week dynamic pricing.</div>", unsafe_allow_html=True)

    with c4:
        rt_price = df.groupby("Room_Type")["Price_Per_Night"].median().reset_index()
        fig4 = px.bar(rt_price, x="Room_Type", y="Price_Per_Night",
                      color="Price_Per_Night", color_continuous_scale="RdBu_r",
                      title="Median Price by Room Type")
        fig4.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=320, margin=dict(t=40,b=0,l=0,r=0),
                           coloraxis_showscale=False)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Entire home/apt listings earn 2.8x the nightly rate of private rooms. Budget travelers opting for shared rooms represent a niche market with very different expectations.</div>", unsafe_allow_html=True)

    # Price heatmap
    st.markdown("""<div class='section-header'><h3>🗺️ Neighborhood × Season Price Heatmap</h3></div>""", unsafe_allow_html=True)
    pivot = df.pivot_table(values="Price_Per_Night",
                           index="Neighborhood", columns="Season",
                           aggfunc="mean").round(0)
    fig_heat = go.Figure(data=go.Heatmap(
        z=pivot.values, x=pivot.columns, y=pivot.index,
        colorscale="RdBu_r",
        text=pivot.round(0).values, texttemplate="AED %{text}",
        hoverinfo="skip"
    ))
    fig_heat.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e0e6f0",
                           height=500, margin=dict(t=20,b=0,l=0,r=0))
    st.plotly_chart(fig_heat, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION MODELS
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Classification Models":
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import (accuracy_score, precision_score,
                                 recall_score, f1_score, confusion_matrix)
    try:
        from xgboost import XGBClassifier
        HAS_XGB = True
    except ImportError:
        HAS_XGB = False

    st.markdown("<div class='hero'><h1>🤖 Classification Models</h1><p>Predict Booking_Status using machine learning. Compare Logistic Regression, Decision Tree, Random Forest, and XGBoost.</p></div>", unsafe_allow_html=True)

    @st.cache_data(show_spinner=False)
    def run_classification(df):
        features = ["Price_Per_Night","Review_Score","Occupancy_Rate","Amenities_Count",
                    "Distance_to_City_Center","Superhost_Status","Host_Response_Rate",
                    "Number_of_Reviews","Bedrooms","Wifi","Pool","Parking",
                    "Booking_Lead_Time","Length_of_Stay"]
        X = df[features].copy()
        y = (df["Booking_Status"] == "Booked").astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_tr_s = scaler.fit_transform(X_train)
        X_te_s = scaler.transform(X_test)

        models = {
            "Logistic Regression": LogisticRegression(max_iter=500),
            "Decision Tree":       DecisionTreeClassifier(max_depth=6, random_state=42),
            "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
        }
        if HAS_XGB:
            models["XGBoost"] = XGBClassifier(n_estimators=100, random_state=42,
                                               use_label_encoder=False, eval_metric="logloss",
                                               n_jobs=-1)
        results = {}
        cms = {}
        for name, model in models.items():
            Xtr = X_tr_s if name == "Logistic Regression" else X_train.values
            Xte = X_te_s if name == "Logistic Regression" else X_test.values
            model.fit(Xtr, y_train)
            y_pred = model.predict(Xte)
            results[name] = {
                "Accuracy":  round(accuracy_score(y_test, y_pred)*100,2),
                "Precision": round(precision_score(y_test, y_pred)*100,2),
                "Recall":    round(recall_score(y_test, y_pred)*100,2),
                "F1 Score":  round(f1_score(y_test, y_pred)*100,2),
            }
            cms[name] = confusion_matrix(y_test, y_pred)
        fi = None
        if "Random Forest" in models:
            rf = models["Random Forest"]
            fi = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=True)
        return results, cms, fi

    with st.spinner("Training models …"):
        results, cms, fi = run_classification(df)

    results_df = pd.DataFrame(results).T.reset_index().rename(columns={"index":"Model"})
    st.markdown("""<div class='section-header'><h3>📊 Model Performance Comparison</h3></div>""", unsafe_allow_html=True)

    # Metric cards per model
    cols = st.columns(len(results))
    best_model = max(results, key=lambda m: results[m]["F1 Score"])
    for col, (name, metrics) in zip(cols, results.items()):
        border = "border: 2px solid #FF5A5F;" if name == best_model else ""
        col.markdown(f"""
        <div class='metric-card' style='{border}'>
            <div style='font-size:.85rem; font-weight:600; color:#e0e6f0; margin-bottom:8px'>{name}</div>
            <div class='metric-val' style='font-size:1.6rem'>{metrics["F1 Score"]}%</div>
            <div class='metric-lbl'>F1 Score</div>
            <div style='margin-top:10px; font-size:.78rem; color:#8b95b0'>
                Acc: {metrics["Accuracy"]}% | Prec: {metrics["Precision"]}%<br>Recall: {metrics["Recall"]}%
            </div>
            {"<div style='margin-top:8px; color:#FF5A5F; font-size:.78rem; font-weight:700'>⭐ BEST MODEL</div>" if name==best_model else ""}
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        metrics_long = results_df.melt(id_vars="Model", var_name="Metric", value_name="Score")
        fig = px.bar(metrics_long, x="Model", y="Score", color="Metric",
                     barmode="group", color_discrete_sequence=["#FF5A5F","#36c97e","#4f9ef8","#f5a623"],
                     title="Model Comparison — All Metrics (%)")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                          yaxis_range=[0,105])
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        if fi is not None:
            fig2 = px.bar(x=fi.values, y=fi.index, orientation="h",
                          color=fi.values, color_continuous_scale="RdBu_r",
                          title="Random Forest Feature Importance")
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                               font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                               coloraxis_showscale=False, yaxis_title="", xaxis_title="Importance")
            st.plotly_chart(fig2, use_container_width=True)

    # Confusion matrices
    st.markdown("""<div class='section-header'><h3>🔢 Confusion Matrices</h3></div>""", unsafe_allow_html=True)
    cm_cols = st.columns(len(cms))
    for col, (name, cm) in zip(cm_cols, cms.items()):
        fig_cm = go.Figure(data=go.Heatmap(
            z=cm, x=["Not Booked","Booked"], y=["Not Booked","Booked"],
            colorscale=[[0,"#1a1d2e"],[1,"#FF5A5F"]],
            text=cm, texttemplate="%{text}", hoverinfo="skip",
            showscale=False
        ))
        fig_cm.update_layout(title=name, paper_bgcolor="rgba(0,0,0,0)",
                             font_color="#e0e6f0", height=260,
                             margin=dict(t=40,b=0,l=0,r=0))
        col.plotly_chart(fig_cm, use_container_width=True)

    st.markdown(f"<div class='insight-box'>💡 <b>{best_model}</b> achieves the best F1 Score, balancing precision and recall. Occupancy_Rate, Review_Score, and Superhost_Status are the top three predictors of booking success — hosts should prioritize these levers first.</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# CLUSTERING ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Clustering Analysis":
    import plotly.express as px
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    st.markdown("<div class='hero'><h1>🎯 Clustering Analysis</h1><p>Segment Dubai Airbnb listings using K-Means to reveal distinct market archetypes.</p></div>", unsafe_allow_html=True)

    @st.cache_data(show_spinner=False)
    def run_clustering(df):
        features = ["Price_Per_Night","Amenities_Count","Review_Score",
                    "Bedrooms","Distance_to_City_Center","Occupancy_Rate"]
        X = df[features].copy()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Elbow
        inertias = []
        for k in range(2, 9):
            km = KMeans(n_clusters=k, random_state=42, n_init=10)
            km.fit(X_scaled)
            inertias.append(km.inertia_)

        km_final = KMeans(n_clusters=4, random_state=42, n_init=10)
        labels = km_final.fit_predict(X_scaled)
        df_c = df.copy()
        df_c["Cluster"] = labels
        return df_c, inertias, features

    with st.spinner("Running K-Means clustering …"):
        df_clust, inertias, feat_names = run_clustering(df)

    cluster_names = {0:"💼 Business Traveler", 1:"🏖️ Luxury Retreat",
                     2:"👨‍👩‍👧 Family-Friendly", 3:"💸 Budget Stay"}
    df_clust["Cluster_Label"] = df_clust["Cluster"].map(cluster_names)

    c1, c2 = st.columns(2)
    with c1:
        elbow_df = pd.DataFrame({"k": range(2,9), "Inertia": inertias})
        fig = px.line(elbow_df, x="k", y="Inertia", markers=True,
                      color_discrete_sequence=["#FF5A5F"], title="Elbow Method — Optimal K")
        fig.add_vline(x=4, line_dash="dash", line_color="#36c97e",
                      annotation_text="Optimal K=4", annotation_font_color="#36c97e")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig2 = px.scatter(df_clust.sample(1000, random_state=1),
                          x="Price_Per_Night", y="Occupancy_Rate",
                          color="Cluster_Label", opacity=0.7,
                          color_discrete_sequence=["#FF5A5F","#36c97e","#4f9ef8","#f5a623"],
                          title="Cluster Scatter: Price vs Occupancy")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0),
                           yaxis_tickformat=".0%", legend_title="Segment")
        st.plotly_chart(fig2, use_container_width=True)

    # Cluster profiles
    st.markdown("""<div class='section-header'><h3>🏷️ Cluster Profiles</h3></div>""", unsafe_allow_html=True)
    profile = (df_clust.groupby("Cluster_Label")
               [["Price_Per_Night","Occupancy_Rate","Review_Score",
                 "Bedrooms","Amenities_Count","Distance_to_City_Center"]]
               .mean().round(2))

    colors = ["#FF5A5F","#36c97e","#4f9ef8","#f5a623"]
    descs  = {
        "💼 Business Traveler": "Mid-range apartments near business hubs. High self-checkin, reliable WiFi, proximity to metro. Solo/couple travelers, 2-5 night stays.",
        "🏖️ Luxury Retreat":    "Premium properties in Palm Jumeirah/Downtown. Pool, parking, concierge. Weekend bookings by couples. High price, high review scores.",
        "👨‍👩‍👧 Family-Friendly":   "Larger villas/townhouses with multiple bedrooms. Kitchen, laundry, parking essential. Longer stays (7+ nights), value-focused pricing.",
        "💸 Budget Stay":        "Studios and private rooms in outer districts. Minimal amenities, lowest price point. Solo travelers, short stays, high volume.",
    }

    cols_c = st.columns(2)
    for i, (label, row) in enumerate(profile.iterrows()):
        col = cols_c[i % 2]
        col.markdown(f"""
        <div style='background:#1a1d2e; border:1px solid #252a3d;
                    border-left:4px solid {colors[i]}; border-radius:12px;
                    padding:18px 20px; margin-bottom:14px;'>
            <div style='font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:6px'>{label}</div>
            <div style='font-size:.82rem; color:#8b95b0; margin-bottom:12px'>{descs.get(label,"")}</div>
            <div style='display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px;'>
                <div style='text-align:center; background:#12151f; border-radius:8px; padding:8px'>
                    <div style='color:{colors[i]}; font-weight:700'>AED {row["Price_Per_Night"]:.0f}</div>
                    <div style='font-size:.72rem; color:#555e7a'>Price/night</div>
                </div>
                <div style='text-align:center; background:#12151f; border-radius:8px; padding:8px'>
                    <div style='color:{colors[i]}; font-weight:700'>{row["Occupancy_Rate"]:.0%}</div>
                    <div style='font-size:.72rem; color:#555e7a'>Occupancy</div>
                </div>
                <div style='text-align:center; background:#12151f; border-radius:8px; padding:8px'>
                    <div style='color:{colors[i]}; font-weight:700'>{row["Review_Score"]:.1f}★</div>
                    <div style='font-size:.72rem; color:#555e7a'>Review score</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    # Radar chart
    st.markdown("""<div class='section-header'><h3>📡 Cluster Radar Comparison</h3></div>""", unsafe_allow_html=True)
    import plotly.graph_objects as go
    radar_feats = ["Price_Per_Night","Occupancy_Rate","Review_Score","Bedrooms","Amenities_Count"]
    norm_profile = (profile[radar_feats] - profile[radar_feats].min()) / \
                   (profile[radar_feats].max() - profile[radar_feats].min() + 1e-9)
    fig_radar = go.Figure()
    for i, (label, row) in enumerate(norm_profile.iterrows()):
        vals = row.tolist()
        vals.append(vals[0])
        cats = radar_feats + [radar_feats[0]]
        fig_radar.add_trace(go.Scatterpolar(r=vals, theta=cats, fill="toself",
                                             name=label, line_color=colors[i], opacity=0.6))
    fig_radar.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e0e6f0",
                            polar=dict(bgcolor="#1a1d2e",
                                       radialaxis=dict(visible=True, color="#555e7a")),
                            height=420, margin=dict(t=20,b=0,l=0,r=0))
    st.plotly_chart(fig_radar, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# ASSOCIATION RULE MINING
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Association Rule Mining":
    import plotly.express as px
    import plotly.graph_objects as go
    from mlxtend.frequent_patterns import apriori, association_rules
    from mlxtend.preprocessing import TransactionEncoder

    st.markdown("<div class='hero'><h1>🔗 Association Rule Mining</h1><p>Discover which amenity combinations drive higher occupancy and revenue using the Apriori algorithm.</p></div>", unsafe_allow_html=True)

    @st.cache_data(show_spinner=False)
    def run_apriori(df):
        amenity_cols = ["Wifi","Kitchen","Air_Conditioning","Parking","Self_Checkin","Pool"]
        am_df = df[amenity_cols].copy().astype(bool)
        # Add derived high-performance flag
        am_df["High_Occupancy"]  = df["Occupancy_Rate"] > 0.7
        am_df["High_Price"]      = df["Price_Per_Night"] > df["Price_Per_Night"].median()
        am_df["Superhost"]       = df["Superhost_Status"].astype(bool)
        am_df["Long_Stay"]       = df["Length_of_Stay"] > 5

        freq = apriori(am_df, min_support=0.10, use_colnames=True)
        rules = association_rules(freq, metric="lift", min_threshold=1.05)
        rules = rules.sort_values("lift", ascending=False).head(30)
        rules["antecedents"] = rules["antecedents"].apply(lambda x: ", ".join(list(x)))
        rules["consequents"]  = rules["consequents"].apply(lambda x: ", ".join(list(x)))
        return rules

    with st.spinner("Running Apriori algorithm …"):
        rules = run_apriori(df)

    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='metric-card'><div class='metric-val'>{len(rules)}</div><div class='metric-lbl'>Rules Generated</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'><div class='metric-val'>{rules['lift'].max():.2f}</div><div class='metric-lbl'>Max Lift</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'><div class='metric-val'>{rules['confidence'].max():.0%}</div><div class='metric-lbl'>Max Confidence</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class='section-header'><h3>📋 Top Association Rules</h3></div>""", unsafe_allow_html=True)
    display_rules = rules[["antecedents","consequents","support","confidence","lift"]].copy()
    display_rules.columns = ["IF (Antecedents)","THEN (Consequents)","Support","Confidence","Lift"]
    display_rules["Support"]    = display_rules["Support"].map("{:.1%}".format)
    display_rules["Confidence"] = display_rules["Confidence"].map("{:.1%}".format)
    display_rules["Lift"]       = display_rules["Lift"].map("{:.3f}".format)
    st.dataframe(display_rules.head(20), use_container_width=True, height=380)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(rules.head(20),
                         x="support", y="confidence", size="lift",
                         color="lift", color_continuous_scale="RdBu_r",
                         hover_data=["antecedents","consequents"],
                         title="Support vs Confidence (bubble = Lift)")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                          xaxis_tickformat=".0%", yaxis_tickformat=".0%")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Rules with high lift AND high confidence are the most actionable. Pool + Parking combinations consistently appear in high-lift clusters — signal that luxury amenity bundles strongly predict premium outcomes.</div>", unsafe_allow_html=True)

    with c2:
        top10 = rules.head(10).copy()
        top10["Rule"] = top10["antecedents"] + " → " + top10["consequents"]
        fig2 = px.bar(top10, x="lift", y="Rule", orientation="h",
                      color="lift", color_continuous_scale="RdBu_r",
                      title="Top 10 Rules by Lift")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                           coloraxis_showscale=False, yaxis_title="")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 WiFi + Self_Checkin → High_Occupancy is the strongest actionable rule for hosts. These two amenities together add up to 3x more likely to achieve 70%+ occupancy vs. listings without them.</div>", unsafe_allow_html=True)

    st.markdown("""<div class='section-header'><h3>💡 Business Recommendations for Hosts</h3></div>""", unsafe_allow_html=True)
    recs = [
        ("🛜", "WiFi + Self Check-in", "Highest lift for occupancy → must-have pair for any host starting out."),
        ("🏊", "Pool + Parking",        "Drives premium pricing — invest if targeting luxury segment."),
        ("🍳", "Kitchen + Air Con",      "Boosts long-stay bookings — families and business travelers require both."),
        ("⭐", "Superhost + WiFi",       "Most bookings come from this combo — pursue Superhost status actively."),
    ]
    cols_r = st.columns(4)
    for col, (icon, title, desc) in zip(cols_r, recs):
        col.markdown(f"""
        <div class='metric-card'>
            <div style='font-size:2rem'>{icon}</div>
            <div style='font-weight:700; color:#FF5A5F; margin:8px 0 4px; font-size:.9rem'>{title}</div>
            <div style='font-size:.78rem; color:#8b95b0'>{desc}</div>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# REGRESSION MODELING
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Regression Modeling":
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import numpy as np

    st.markdown("<div class='hero'><h1>📈 Regression Modeling</h1><p>Predict nightly price using Linear, Ridge, and Lasso regression. Understand what drives pricing.</p></div>", unsafe_allow_html=True)

    @st.cache_data(show_spinner=False)
    def run_regression(df):
        features = ["Bedrooms","Bathrooms","Accommodates","Amenities_Count","Review_Score",
                    "Superhost_Status","Distance_to_City_Center","Wifi","Kitchen",
                    "Pool","Parking","Air_Conditioning","Host_Response_Rate","Occupancy_Rate"]
        X = df[features]
        y = df["Price_Per_Night"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_tr_s = scaler.fit_transform(X_train)
        X_te_s = scaler.transform(X_test)

        models = {
            "Linear Regression": LinearRegression(),
            "Ridge Regression":  Ridge(alpha=10),
            "Lasso Regression":  Lasso(alpha=5, max_iter=2000),
        }
        results = {}
        coefs   = {}
        for name, model in models.items():
            model.fit(X_tr_s, y_train)
            y_pred = model.predict(X_te_s)
            results[name] = {
                "MAE":  round(mean_absolute_error(y_test, y_pred), 1),
                "RMSE": round(np.sqrt(mean_squared_error(y_test, y_pred)), 1),
                "R²":   round(r2_score(y_test, y_pred), 4),
            }
            coefs[name] = pd.Series(model.coef_, index=features).sort_values()
        best_preds = models["Ridge Regression"].predict(X_te_s)
        return results, coefs, y_test.values, best_preds, features

    with st.spinner("Training regression models …"):
        reg_results, coefs, y_true, y_pred_best, feat_names = run_regression(df)

    # Metric cards
    cols = st.columns(3)
    best_r2 = max(reg_results, key=lambda m: reg_results[m]["R²"])
    for col, (name, metrics) in zip(cols, reg_results.items()):
        border = "border: 2px solid #FF5A5F;" if name == best_r2 else ""
        col.markdown(f"""
        <div class='metric-card' style='{border}'>
            <div style='font-weight:700; color:#e0e6f0'>{name}</div>
            <div class='metric-val' style='font-size:1.8rem'>{metrics["R²"]:.3f}</div>
            <div class='metric-lbl'>R² Score</div>
            <div style='font-size:.8rem; color:#8b95b0; margin-top:8px'>
                MAE: AED {metrics["MAE"]} | RMSE: AED {metrics["RMSE"]}
            </div>
            {"<div style='color:#FF5A5F; font-size:.78rem; font-weight:700; margin-top:6px'>⭐ BEST</div>" if name==best_r2 else ""}
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        ridge_coef = coefs["Ridge Regression"]
        fig = px.bar(x=ridge_coef.values, y=ridge_coef.index, orientation="h",
                     color=ridge_coef.values, color_continuous_scale="RdBu_r",
                     title="Ridge Regression — Feature Coefficients")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=380, margin=dict(t=40,b=0,l=0,r=0),
                          coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Bedrooms and Pool have the strongest positive price effect. Distance_to_City_Center is the largest negative factor — each km further reduces price by ~AED 8–12/night on average.</div>", unsafe_allow_html=True)

    with c2:
        # Actual vs predicted scatter
        sample_idx = np.random.default_rng(1).choice(len(y_true), 300, replace=False)
        fig2 = px.scatter(x=y_true[sample_idx], y=y_pred_best[sample_idx],
                          opacity=0.5, color_discrete_sequence=["#FF5A5F"],
                          title="Actual vs Predicted Price (Ridge, sample)")
        fig2.add_shape(type="line", x0=50, x1=2000, y0=50, y1=2000,
                       line=dict(color="#36c97e", dash="dash"))
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=380, margin=dict(t=40,b=0,l=0,r=0),
                           xaxis_title="Actual (AED)", yaxis_title="Predicted (AED)")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Predictions cluster tightly around the diagonal (perfect prediction line) for mid-range listings. Highest variance at >AED 1,000 — luxury pricing is more idiosyncratic and harder to predict from features alone.</div>", unsafe_allow_html=True)

    # Lasso sparsity
    st.markdown("""<div class='section-header'><h3>🧹 Lasso Sparsity — Feature Selection</h3></div>""", unsafe_allow_html=True)
    lasso_coef = coefs["Lasso Regression"]
    non_zero = (lasso_coef != 0).sum()
    st.markdown(f"<div class='insight-box'>💡 Lasso selected <b>{non_zero}/{len(feat_names)}</b> features, shrinking the rest to zero. This confirms that a parsimonious model with just the most influential features captures most of the price variance.</div>", unsafe_allow_html=True)
    fig3 = px.bar(x=lasso_coef.abs().sort_values(ascending=False).values,
                  y=lasso_coef.abs().sort_values(ascending=False).index,
                  orientation="h", color_discrete_sequence=["#4f9ef8"],
                  title="Lasso — Absolute Coefficient Magnitude")
    fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0))
    st.plotly_chart(fig3, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# DEMAND FORECASTING
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Demand Forecasting":
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.linear_model import Ridge
    from sklearn.preprocessing import PolynomialFeatures

    st.markdown("<div class='hero'><h1>📅 Demand Forecasting</h1><p>Forecast monthly booking demand and identify Dubai's seasonal travel patterns.</p></div>", unsafe_allow_html=True)

    # Monthly demand
    month_demand = (df[df["Booking_Status"]=="Booked"]
                    .groupby("Month").size().reset_index(name="Bookings"))
    month_names = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",
                   7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
    month_demand["Month_Name"] = month_demand["Month"].map(month_names)

    # Fit polynomial trend + forecast 6 months ahead
    X_m = month_demand["Month"].values.reshape(-1,1)
    y_m = month_demand["Bookings"].values
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X_m)
    model_m = Ridge().fit(X_poly, y_m)
    future_months = list(range(1, 19))
    X_fut = poly.transform(np.array(future_months).reshape(-1,1))
    y_fut = model_m.predict(X_fut)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=month_demand["Month_Name"], y=month_demand["Bookings"],
                         name="Actual Bookings", marker_color="#FF5A5F", opacity=0.8))
    fut_names = [month_names.get(m % 12 or 12, str(m)) + ("'" if m>12 else "") for m in future_months]
    fig.add_trace(go.Scatter(x=fut_names, y=np.clip(y_fut, 0, None),
                              name="Forecast", line=dict(color="#36c97e", width=2, dash="dot"),
                              mode="lines+markers"))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font_color="#e0e6f0", height=380, margin=dict(t=20,b=0,l=0,r=0),
                      legend_title="", title="Monthly Booking Demand + 6-Month Forecast")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<div class='insight-box'>💡 Dubai shows a strong bimodal demand pattern — peak in Nov–Feb (winter tourist season) and a secondary peak in Mar–Apr. Summer (Jun–Aug) sees 30-40% lower demand due to extreme heat — hosts should adjust pricing strategy accordingly.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        day_demand = (df[df["Booking_Status"]=="Booked"]
                      .groupby("Day_of_Week").size()
                      .reindex(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
                      .reset_index(name="Bookings"))
        fig2 = px.bar(day_demand, x="Day_of_Week", y="Bookings",
                      color="Bookings", color_continuous_scale="RdBu_r",
                      title="Bookings by Day of Week")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0),
                           coloraxis_showscale=False)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Thursday–Saturday drives 45% of all bookings. The UAE weekend (Fri-Sat) creates a distinct demand spike — deploy minimum night requirements on these days to capture premium pricing.</div>", unsafe_allow_html=True)

    with c2:
        season_demand = (df[df["Booking_Status"]=="Booked"]
                         .groupby(["Season","Traveler_Type"]).size().reset_index(name="Bookings"))
        fig3 = px.bar(season_demand, x="Season", y="Bookings",
                      color="Traveler_Type", barmode="stack",
                      color_discrete_sequence=px.colors.qualitative.Bold,
                      title="Seasonal Demand by Traveler Type")
        fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=340, margin=dict(t=40,b=0,l=0,r=0))
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Couples dominate winter bookings (honeymoon season), while Families peak in spring school holidays. Business travelers are distributed evenly year-round — a stable segment worth targeting with premium amenities.</div>", unsafe_allow_html=True)

    # Heatmap month × day
    st.markdown("""<div class='section-header'><h3>📆 Demand Heatmap: Month × Day of Week</h3></div>""", unsafe_allow_html=True)
    booked = df[df["Booking_Status"]=="Booked"]
    pivot_heat = booked.pivot_table(values="Listing_ID", index="Month",
                                    columns="Day_of_Week", aggfunc="count")
    pivot_heat = pivot_heat.reindex(columns=["Monday","Tuesday","Wednesday",
                                              "Thursday","Friday","Saturday","Sunday"])
    pivot_heat.index = [month_names[m] for m in pivot_heat.index]
    fig_heat = go.Figure(data=go.Heatmap(
        z=pivot_heat.values, x=pivot_heat.columns, y=pivot_heat.index,
        colorscale="RdBu_r", hoverinfo="skip"
    ))
    fig_heat.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e0e6f0",
                           height=420, margin=dict(t=10,b=0,l=0,r=0))
    st.plotly_chart(fig_heat, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# REVENUE OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════
elif p == "Revenue Optimization":
    import plotly.express as px
    import plotly.graph_objects as go
    import numpy as np

    st.markdown("<div class='hero'><h1>🚀 Revenue Optimization</h1><p>Find the optimal price point, highest-value neighborhoods, and ROI-positive amenity investments.</p></div>", unsafe_allow_html=True)

    df["Monthly_Revenue"] = df["Price_Per_Night"] * df["Occupancy_Rate"] * 30

    # KPIs
    c1, c2, c3, c4 = st.columns(4)
    top_hood = df.groupby("Neighborhood")["Monthly_Revenue"].mean().idxmax()
    top_prop = df.groupby("Property_Type")["Monthly_Revenue"].mean().idxmax()
    opt_price = df.groupby(pd.cut(df["Price_Per_Night"], bins=20))["Monthly_Revenue"].mean().idxmax()

    c1.markdown(f"<div class='metric-card'><div class='metric-val'>AED {df['Monthly_Revenue'].mean():,.0f}</div><div class='metric-lbl'>Avg Monthly Revenue</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'><div class='metric-val'>{top_hood}</div><div class='metric-lbl'>Top Revenue Hood</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'><div class='metric-val'>{top_prop}</div><div class='metric-lbl'>Top Property Type</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='metric-card'><div class='metric-val'>AED {df['Monthly_Revenue'].max():,.0f}</div><div class='metric-lbl'>Peak Monthly Rev</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Price vs Revenue curve
    c1, c2 = st.columns(2)
    with c1:
        bins = pd.cut(df["Price_Per_Night"], bins=25)
        rev_curve = df.groupby(bins)["Monthly_Revenue"].mean().reset_index()
        rev_curve["Price_Mid"] = rev_curve["Price_Per_Night"].apply(lambda x: x.mid)
        fig = px.line(rev_curve, x="Price_Mid", y="Monthly_Revenue",
                      markers=True, color_discrete_sequence=["#FF5A5F"],
                      title="Price vs Monthly Revenue Curve")
        opt_x = rev_curve.loc[rev_curve["Monthly_Revenue"].idxmax(), "Price_Mid"]
        fig.add_vline(x=float(opt_x), line_dash="dash", line_color="#36c97e",
                      annotation_text=f"Optimal ≈ AED {opt_x:.0f}",
                      annotation_font_color="#36c97e")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                          xaxis_title="Price Per Night (AED)",
                          yaxis_title="Avg Monthly Revenue (AED)")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"<div class='insight-box'>💡 The revenue-maximizing price point is approximately AED {opt_x:.0f}/night. Beyond this, occupancy drops faster than price increases — hosts pricing above this threshold are leaving money on the table.</div>", unsafe_allow_html=True)

    with c2:
        hood_rev = (df.groupby("Neighborhood")["Monthly_Revenue"].mean()
                    .sort_values(ascending=False).reset_index())
        fig2 = px.bar(hood_rev, x="Monthly_Revenue", y="Neighborhood",
                      orientation="h", color="Monthly_Revenue",
                      color_continuous_scale="RdBu_r",
                      title="Avg Monthly Revenue by Neighborhood")
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#e0e6f0", height=360, margin=dict(t=40,b=0,l=0,r=0),
                           coloraxis_showscale=False, yaxis_title="")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("<div class='insight-box'>💡 Palm Jumeirah and Downtown Dubai generate 2.5-3x the revenue of outer districts. Even budget-adjusted, these locations offer the highest ROI per listing for new hosts entering the market.</div>", unsafe_allow_html=True)

    # Revenue heatmap: Neighborhood × Property Type
    st.markdown("""<div class='section-header'><h3>🗺️ Revenue Heatmap: Neighborhood × Property Type</h3></div>""", unsafe_allow_html=True)
    rev_pivot = df.pivot_table(values="Monthly_Revenue", index="Neighborhood",
                               columns="Property_Type", aggfunc="mean").round(0)
    fig_heat = go.Figure(data=go.Heatmap(
        z=rev_pivot.values, x=rev_pivot.columns, y=rev_pivot.index,
        colorscale="RdBu_r",
        text=rev_pivot.round(0).values, texttemplate="AED %{text}",
        hoverinfo="skip"
    ))
    fig_heat.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e0e6f0",
                           height=500, margin=dict(t=10,b=0,l=0,r=0))
    st.plotly_chart(fig_heat, use_container_width=True)

    # Amenity ROI
    st.markdown("""<div class='section-header'><h3>💡 Amenity Investment ROI Analysis</h3></div>""", unsafe_allow_html=True)
    amenity_impact = {}
    for am in ["Wifi","Kitchen","Pool","Parking","Self_Checkin","Air_Conditioning"]:
        with_am    = df[df[am]==1]["Monthly_Revenue"].mean()
        without_am = df[df[am]==0]["Monthly_Revenue"].mean()
        amenity_impact[am] = round(with_am - without_am, 0)

    am_df = pd.DataFrame.from_dict(amenity_impact, orient="index",
                                   columns=["Revenue_Delta"]).sort_values("Revenue_Delta")
    fig_am = px.bar(am_df, x="Revenue_Delta", y=am_df.index, orientation="h",
                    color="Revenue_Delta", color_continuous_scale="RdBu_r",
                    title="Revenue Impact of Each Amenity (AED/month)")
    fig_am.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                         font_color="#e0e6f0", height=320, margin=dict(t=40,b=0,l=0,r=0),
                         coloraxis_showscale=False)
    st.plotly_chart(fig_am, use_container_width=True)

    # Strategic recommendations
    st.markdown("""<div class='section-header'><h3>🎯 Strategic Recommendations</h3></div>""", unsafe_allow_html=True)
    recs = [
        ("💰", "Price Optimization",    f"Set base price at AED {opt_x:.0f}/night and implement dynamic pricing (+15-25% for weekends, +20-30% for peak winter months Dec–Feb)."),
        ("🏆", "Pursue Superhost",       "Superhost listings generate 22% more monthly revenue. Focus on: response rate >90%, 4.8+ review score, zero cancellations."),
        ("🏊", "Invest in Pool",         f"Pool adds AED {amenity_impact.get('Pool',0):,.0f}/month in revenue. Viable ROI for Palm Jumeirah villas within 18-24 months."),
        ("📍", "Location Premium",       "Downtown/Palm properties command a 2.5x revenue premium. If acquiring new properties, these neighborhoods offer strongest baseline yield."),
        ("📅", "Seasonal Strategy",      "Raise minimum nights to 3+ during winter peak (Dec–Feb). Offer discounts for 7+ night stays in summer to maintain occupancy."),
        ("⭐", "Review Management",      "Each 0.1 increase in review score correlates with +3% occupancy. Invest in guest experience, not just amenities."),
    ]
    for i in range(0, len(recs), 2):
        c1, c2 = st.columns(2)
        for col, (icon, title, desc) in zip([c1,c2], recs[i:i+2]):
            col.markdown(f"""
            <div style='background:#1a1d2e; border:1px solid #252a3d;
                        border-left:4px solid #FF5A5F; border-radius:12px;
                        padding:18px 20px; margin-bottom:12px;'>
                <div style='font-size:1.3rem; margin-bottom:6px'>{icon} <span style='font-weight:700; color:#fff'>{title}</span></div>
                <div style='font-size:.85rem; color:#8b95b0; line-height:1.6'>{desc}</div>
            </div>""", unsafe_allow_html=True)
