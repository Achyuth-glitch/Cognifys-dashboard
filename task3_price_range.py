import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="💰 Price Range Distribution", layout="centered")

# --- LUXURY GOLD THEME ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle, #000000 0%, #1b1b1b 100%);
        color: #f1c40f;
        animation: fadeIn 1.5s ease-in;
    }
    @keyframes fadeIn {from{opacity:0;} to{opacity:1;}}
    h1 {text-align:center; color:#f1c40f; text-shadow:0 0 10px #f1c40f;}
    .stDataFrame {
        border: 2px solid #f1c40f;
        border-radius: 10px;
        background-color: rgba(30,30,30,0.9);
        color: #f1c40f;
    }
    .stDataFrame:hover {box-shadow:0 0 15px #f1c40f;}
    </style>
""", unsafe_allow_html=True)

st.title("💰 Task 3 – Price Range Distribution")
st.markdown("#### Cognifyz Data Analyst Internship | Level 1")

uploaded = st.file_uploader("📂 Upload Dataset", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    df.dropna(subset=['Price range'], inplace=True)
    price_counts = df['Price range'].value_counts().sort_index()
    percent = (price_counts / len(df)) * 100
    result = pd.DataFrame({'Price Range': price_counts.index, 'Count': price_counts.values, 'Percentage (%)': percent.round(2)})

    st.dataframe(result)

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(result['Price Range'].astype(str), result['Percentage (%)'], color='#f1c40f')
    ax.set_facecolor("#1b1b1b")
    ax.set_title("Price Range Distribution", color="#f1c40f")
    ax.tick_params(colors="#f1c40f")
    for spine in ax.spines.values():
        spine.set_edgecolor("#f1c40f")
    st.pyplot(fig)

    if not result.empty:
        st.markdown(f"### 💎 Insights\n- Most restaurants: **Price Range {result.iloc[0,0]}**.\n")
    else:
        st.markdown("### 💎 Insights\n- No data available after filtering for Price Range.\n")
    st.success("✅ Task 3 Completed Successfully!")
else:
    st.info("👆 Please upload your dataset.")
