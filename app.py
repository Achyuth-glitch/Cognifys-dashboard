import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cognifyz Data Analysis Dashboard", layout="wide")

# --- CLEAN 3D GLASS + BLACK SIDEBAR STYLING ---
st.markdown("""
    <style>
    /* === App Background === */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a1a 0%, #2c3e50 100%);
        color: white;
        animation: fadeIn 1.5s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* === Sidebar Styling === */
    [data-testid="stSidebar"] {
        background: black;
        border-right: 1px solid #333;
        color: white;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] p, 
    [role="radiogroup"] label {
        color: white !important;
        font-weight: 600;
    }

    /* === Headings === */
    h1, h2 {
        text-align: center;
        color: #00ffff;
        text-shadow: 0 0 8px rgba(0, 255, 255, 0.5);
    }

    /* === Card / Container Style === */
    .stMarkdown, .stDataFrame {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }
    .stMarkdown:hover, .stDataFrame:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(0, 255, 255, 0.3);
    }

    /* === Buttons === */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #0072ff, #00c6ff);
        transform: scale(1.05);
        box-shadow: 0 0 10px #00c6ff;
    }

    /* === Animations === */
    .stPlotlyChart, .stPyplot, .stDataFrame {
        animation: fadeUp 1s ease-in;
    }
    @keyframes fadeUp {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📊 Cognifyz Dashboard")
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🍽️ Task 1", "🏙️ Task 2", "💰 Task 3", "🌐 Task 4"]
)

# --- HOME PAGE ---
if page == "🏠 Home":
    st.title("🚀 Cognifyz Data Analysis Dashboard (Level 1)")
    st.markdown("""
    <div style="text-align:center; font-size:18px;">
    <p>Welcome to your <b>Cognifyz Data Analysis Dashboard</b>!</p>
    <p>Use the sidebar to explore different analysis tasks:</p>
    <ul style="text-align:left; margin:auto; width:60%;">
        <li>🍽️ <b>Task 1:</b> Top 3 Cuisines</li>
        <li>🏙️ <b>Task 2:</b> City-wise Analysis</li>
        <li>💰 <b>Task 3:</b> Price Range Insights</li>
        <li>🌐 <b>Task 4:</b> Online Delivery Preferences</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.success("✅ Dashboard Loaded Successfully!")

# --- TASK 1 ---
elif page == "🍽️ Task 1":
    st.markdown("<h2>🍽️ Top 3 Cuisines Analysis</h2>", unsafe_allow_html=True)
    exec(open("task1_top_cuisines.py", encoding="utf-8").read())

# --- TASK 2 ---
elif page == "🏙️ Task 2":
    st.markdown("<h2>🏙️ City Analysis</h2>", unsafe_allow_html=True)
    exec(open("task2_city_analysis.py", encoding="utf-8").read())

# --- TASK 3 ---
elif page == "💰 Task 3":
    st.markdown("<h2>💰 Price Range Analysis</h2>", unsafe_allow_html=True)
    exec(open("task3_price_range.py", encoding="utf-8").read())

# --- TASK 4 ---
elif page == "🌐 Task 4":
    st.markdown("<h2>🌐 Online Delivery Analysis</h2>", unsafe_allow_html=True)
    exec(open("task4_online_delivery.py", encoding="utf-8").read())
