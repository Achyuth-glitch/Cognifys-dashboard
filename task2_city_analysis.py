import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🏙️ City Analysis", layout="centered")

# --- COOL BLUE THEME ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        animation: fadeIn 1.8s ease-in;
    }
    @keyframes fadeIn {from{opacity:0;} to{opacity:1;}}
    h1 {color:#003049; text-align:center; animation: pulse 2s infinite alternate;}
    @keyframes pulse {from{transform:scale(1);} to{transform:scale(1.05);}}
    .stDataFrame {
        background-color: rgba(255,255,255,0.9);
        border: 2px solid #003049;
        border-radius: 12px;
        padding: 10px;
        transition: box-shadow 0.3s ease;
    }
    .stDataFrame:hover {box-shadow: 0 0 15px #003049;}
    </style>
""", unsafe_allow_html=True)

st.title("🏙️ Task 2 – City Analysis")
st.markdown("#### Cognifyz Data Analyst Internship | Level 1")

uploaded = st.file_uploader("📂 Upload Dataset", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    df.dropna(subset=['City','Aggregate rating'], inplace=True)

    if df.empty:
        st.info("🚫 No data available after removing missing values. Please upload a valid dataset.")
    else:
        city_counts = df['City'].value_counts()
        avg_rating = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
        top_city, best_city = city_counts.idxmax(), avg_rating.idxmax()

        result = pd.DataFrame({'City': city_counts.index, 'Restaurant Count': city_counts.values,
                               'Average Rating': avg_rating.reindex(city_counts.index).values})
        st.dataframe(result)

        fig, ax = plt.subplots(figsize=(8,4))
        ax.bar(result['City'][:10], result['Restaurant Count'][:10], color='#0077b6')
        ax.set_title("Top 10 Cities by Restaurant Count", color="#003049")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.markdown(f"### 🌆 Insights\n- Most restaurants: **{top_city}**.\n- Highest average rating: **{best_city} ({avg_rating[best_city]:.2f})**.")
        st.success("✅ Task 2 Completed Successfully!")
else:
    st.info("👆 Please upload your dataset.")
