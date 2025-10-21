import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🌐 Online Delivery Analysis", layout="centered")

# --- GREEN NATURE THEME ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(120deg, #d4fc79 0%, #96e6a1 100%);
        animation: float 6s ease-in-out infinite alternate;
    }
    @keyframes float {
        from {background-position: left top;}
        to {background-position: right bottom;}
    }
    h1 {text-align:center; color:#1b4332;}
    .stDataFrame {
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        border: 2px solid #40916c;
        transition: transform 0.3s ease;
    }
    .stDataFrame:hover {transform: scale(1.02);}
    .stMarkdown {color:#081c15;}
    </style>
""", unsafe_allow_html=True)

st.title("🌐 Task 4 – Online Delivery Analysis")
st.markdown("#### Cognifyz Data Analyst Internship | Level 1")

uploaded = st.file_uploader("📂 Upload Dataset", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    df.dropna(subset=['Has Online delivery','Aggregate rating'], inplace=True)
    online_counts = df['Has Online delivery'].value_counts()
    percent = (online_counts / len(df)) * 100
    avg_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()

    result = pd.DataFrame({
        'Online Delivery': online_counts.index,
        'Count': online_counts.values,
        'Percentage (%)': percent.round(2),
        'Average Rating': avg_rating.values
    })
    st.dataframe(result)

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(result['Online Delivery'].astype(str), result['Percentage (%)'], color=['#52b788','#d8f3dc'])
    ax.set_title("Online Delivery Availability", color="#1b4332")
    ax.set_ylabel("Percentage (%)", color="#1b4332")
    st.pyplot(fig)

    percent_yes = percent.loc['Yes'] if 'Yes' in percent.index else 0
    st.markdown(f"### 🍃 Insights\n- {percent_yes:.2f}% offer delivery.\n")
    st.success("✅ Task 4 Completed Successfully!")
else:
    st.info("👆 Please upload your dataset.")
