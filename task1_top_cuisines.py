import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="🍽️ Top Cuisines Analysis", layout="centered")

# --- CUSTOM CSS (Warm Gradient Theme) ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        animation: fadeIn 2s ease-in;
    }
    @keyframes fadeIn {from {opacity:0;} to {opacity:1;}}
    h1 {text-align:center; color:#e63946; animation: slideIn 1.2s ease-in-out;}
    @keyframes slideIn {from {transform:translateY(-20px); opacity:0;} to {transform:translateY(0); opacity:1;}}
    .stDataFrame, .stMarkdown {
        background: rgba(255,255,255,0.85);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .stDataFrame:hover, .stMarkdown:hover {transform: scale(1.01);}
    </style>
""", unsafe_allow_html=True)

st.title("🍽️ Task 1 – Top 3 Cuisines Analysis")
st.markdown("#### Cognifyz Data Analyst Internship | Level 1")

uploaded_file = st.file_uploader("📂 Upload Dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.dropna(subset=['Cuisines'], inplace=True)
    df['Cuisines'] = df['Cuisines'].str.split(',')
    df = df.explode('Cuisines')
    df['Cuisines'] = df['Cuisines'].str.strip()
    cuisine_counts = df['Cuisines'].value_counts()
    top3 = cuisine_counts.head(3)
    total = len(df)
    percentage = (top3 / total) * 100

    result = pd.DataFrame({'Cuisine': top3.index, 'Count': top3.values, 'Percentage (%)': percentage.round(2)})
    st.subheader("📊 Top 3 Most Common Cuisines")
    st.dataframe(result)

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(result['Cuisine'], result['Percentage (%)'], color=['#e63946','#f4a261','#2a9d8f'])
    ax.set_title("Top 3 Cuisines by Percentage of Restaurants")
    st.pyplot(fig)

    st.markdown(f"""
    ### 🔍 Key Insights  
    - **{result.iloc[0,0]}** is most popular ({result.iloc[0,2]}%).  
    - Followed by **{result.iloc[1,0]}** and **{result.iloc[2,0]}**.  
    """)
    st.success("✅ Task 1 Completed Successfully!")
else:
    st.info("👆 Please upload your dataset.")
