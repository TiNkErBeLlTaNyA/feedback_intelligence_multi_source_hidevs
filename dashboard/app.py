import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.db import load_from_db
from analysis.trends import sentiment_trend
from analysis.prioritization import prioritize_issues
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Feedback Intelligence System", layout="wide")

# ===== CUSTOM CSS (HiDevs Style) =====
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #eef2f3, #f9fbfc);
}

/* Header */
.header-box {
    background: linear-gradient(90deg, #2E86C1, #48C9B0);
    padding: 18px;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* KPI Cards */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    border-left: 5px solid #2E86C1;
}

/* Section Cards */
.section-box {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #E74C3C, #C0392B);
    color: white;
    border-radius: 8px;
    padding: 8px 18px;
    font-weight: bold;
}

/* Titles */
h1, h2, h3 {
    color: #2E4053;
}

</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header-box">📊 Multi-Source Feedback Intelligence System</div>', unsafe_allow_html=True)

# ===== LOAD DATA =====
df = load_from_db()

# ===== FILTERS =====
st.markdown("### 🔍 Filters")
f1, f2 = st.columns(2)

source = f1.selectbox("Source", ["All"] + list(df['source'].unique()))
sentiment = f2.selectbox("Sentiment", ["All"] + list(df['sentiment'].unique()))

filtered = df.copy()

if source != "All":
    filtered = filtered[filtered['source'] == source]

if sentiment != "All":
    filtered = filtered[filtered['sentiment'] == sentiment]

# ===== KPI SECTION =====
st.markdown('<div class="section-box">', unsafe_allow_html=True)

k1, k2, k3 = st.columns(3)

k1.metric("Total Feedback", len(filtered))
k2.metric("Positive %", round((filtered['sentiment']=="positive").mean()*100, 2))
k3.metric("Negative %", round((filtered['sentiment']=="negative").mean()*100, 2))

st.markdown('</div>', unsafe_allow_html=True)

# ===== ALERT =====
if (filtered['sentiment']=="negative").mean() > 0.4:
    st.error("🚨 High Negative Sentiment Detected!")

# ===== MAIN GRID =====
col1, col2 = st.columns(2)

# Trend Chart
with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("📈 Real-Time Sentiment Trends")
    trend = sentiment_trend(filtered)
    st.line_chart(trend)
    st.markdown('</div>', unsafe_allow_html=True)

# Recurring Issues
with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("⚠️ Recurring Issues")
    issues = prioritize_issues(filtered)
    for issue, count in issues:
        st.write(f"🔹 {issue} → {count}")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== WORDCLOUD =====
st.markdown('<div class="section-box">', unsafe_allow_html=True)

st.subheader("☁️ Negative Feedback Insights")

text = " ".join(filtered[filtered['sentiment']=="negative"]['text'].astype(str))

if text:
    wc = WordCloud(background_color="white", colormap="viridis").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# ===== PDF REPORT =====
st.markdown('<div class="section-box">', unsafe_allow_html=True)

st.subheader("📄 Weekly Insight Reports")

if st.button("Generate PDF Report"):
    from reports.report_generator import generate_report
    generate_report(filtered)
    st.success("✅ Report Generated Successfully!")

st.markdown('</div>', unsafe_allow_html=True)