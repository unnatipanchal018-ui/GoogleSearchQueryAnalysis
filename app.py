import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Google Search Query Analysis",
    page_icon="📊",
    layout="wide"
)

# ================= CUSTOM DESIGN =================
st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: bold;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# ================= TITLE =================
st.markdown(
    '<div class="main-title">📊 Google Search Query Analysis Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Social Media Search Interest Analysis in India</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ================= LOAD DATA =================
data = pd.read_csv("data/social_media_trends.csv")

date_column = data.columns[0]

data[date_column] = pd.to_datetime(data[date_column])


# ================= SIDEBAR =================
st.sidebar.title("📊 Dashboard")

st.sidebar.markdown("### Search Information")

st.sidebar.write("📍 Location: India")
st.sidebar.write("📅 Time: Past Year")
st.sidebar.write("🔎 Search Type: Web Search")

st.sidebar.markdown("---")

st.sidebar.info(
    "This dashboard analyzes Google search interest "
    "for popular social media platforms."
)


# ================= STATISTICS CARDS =================
st.markdown(
    '<div class="section-title">📌 Search Statistics</div>',
    unsafe_allow_html=True
)

average = data[
    ["Instagram", "Facebook", "YouTube", "Twitter"]
].mean()

highest = average.idxmax()
highest_value = average.max()

highest_search = int(
    data[
        ["Instagram", "Facebook", "YouTube", "Twitter"]
    ].max().max()
)

lowest_search = int(
    data[
        ["Instagram", "Facebook", "YouTube", "Twitter"]
    ].min().min()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📅 Total Records",
    len(data)
)

col2.metric(
    "🔝 Highest Value",
    highest_search
)

col3.metric(
    "🔻 Lowest Value",
    lowest_search
)

col4.metric(
    "🏆 Top Platform",
    highest
)


# ================= DATA TABLE =================
st.markdown(
    '<div class="section-title">📋 Google Search Data</div>',
    unsafe_allow_html=True
)

st.dataframe(
    data,
    use_container_width=True
)


# ================= SEARCH TREND =================
st.markdown(
    '<div class="section-title">📈 Search Interest Over Time</div>',
    unsafe_allow_html=True
)

plt.figure(figsize=(12, 5))

plt.plot(
    data[date_column],
    data["Instagram"],
    label="Instagram"
)

plt.plot(
    data[date_column],
    data["Facebook"],
    label="Facebook"
)

plt.plot(
    data[date_column],
    data["YouTube"],
    label="YouTube"
)

plt.plot(
    data[date_column],
    data["Twitter"],
    label="Twitter"
)

plt.xlabel("Date")
plt.ylabel("Search Interest")
plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(plt)


# ================= AVERAGE =================
st.markdown(
    '<div class="section-title">📊 Average Search Interest</div>',
    unsafe_allow_html=True
)

st.bar_chart(average)


# ================= TOP PLATFORM =================
st.markdown(
    '<div class="section-title">🏆 Most Searched Platform</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

col1.metric(
    "Platform",
    highest
)

col2.metric(
    "Average Search Interest",
    round(highest_value, 2)
)


# ================= PLATFORM FILTER =================
st.markdown(
    '<div class="section-title">🔍 Platform Search Analysis</div>',
    unsafe_allow_html=True
)

platform = st.selectbox(
    "Select Social Media Platform",
    ["Instagram", "Facebook", "YouTube", "Twitter"]
)

st.write("Selected Platform:", platform)

st.line_chart(
    data.set_index(date_column)[platform]
)


# ================= SUMMARY =================
st.markdown(
    '<div class="section-title">📋 Search Trend Summary</div>',
    unsafe_allow_html=True
)

summary = data[
    ["Instagram", "Facebook", "YouTube", "Twitter"]
].agg(["mean", "max", "min"])

summary = summary.round(2)

st.dataframe(
    summary,
    use_container_width=True
)


# ================= FOOTER =================
st.markdown("---")

st.markdown(
    "<center>📊 Google Search Query Analysis Dashboard | Social Media Analysis</center>",
    unsafe_allow_html=True
)