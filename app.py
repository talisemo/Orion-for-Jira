import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף - שחזור טאב ולוגו
st.set_page_config(page_title="Orion Executive Insights", page_icon="logo.png", layout="wide")

# 2. ניהול מצבי עמוד
if 'page' not in st.session_state: st.session_state.page = 'dashboard'
if 'show_preview' not in st.session_state: st.session_state.show_preview = False
if 'personal_note' not in st.session_state: st.session_state.personal_note = ""

# 3. CSS מלא - RTL יציב ועיצוב כרטיסים
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif; direction: rtl; text-align: right;
    }
    .main .block-container { max-width: 1100px; padding: 2rem; margin: 0 auto; }
    
    /* שחזור עיצוב המדדים */
    [data-testid="stMetric"] {
        background: white; border: 1px solid #DFE1E6;
        border-radius: 8px; padding: 15px !important;
    }
    
    .insight-card {
        background-color: #DEEBFF; border-right: 5px solid #0052CC;
        padding: 15px; border-radius: 4px; margin: 20px 0;
    }
    
    .preview-paper {
        background-color: white; border: 1px solid #ddd; padding: 30px;
        border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #333; margin: 20px 0; text-align: right;
    }
    
    .personal-note-box {
        background-color: #FFF9C4; padding: 10px; border-right: 4px solid #FBC02D;
        margin-top: 15px; font-style: italic;
    }
    
    .trend-box {
        background-color: #F4F5F7; border: 1px solid #DFE1E6;
        padding: 15px; border-radius: 8px; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציות ניווט
def go_to_report(): st.session_state.page = 'report'; st.session_state.show_preview = False
def go_to_dashboard(): st.session_state.page = 'dashboard'

# --- Sidebar (צ'אט משוחזר עם אייקונים) ---
with st.sidebar:
    st.markdown('<div><span style="font-size:1.2rem;">🧠</span> שאל את אוריון</div>', unsafe_allow_html=True)
    if st.button("🚨 מי תקוע?"): pass
    if st.button("⚠️ סיכון ספרינט"): pass
    st.markdown("---")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, מוכנה לעבור על המגמות ההיסטוריות?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    st.chat_input("שאלי משהו...")

# --- עמוד 1: דאשבורד ---
if st.session_state.page == 'dashboard':
    st.markdown(f"<h1>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # שחזור מדדים אסטרטגיים
    st.markdown("### 📌 תמונת מצב")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Sentiment Score", "7.2/10", "0.4 ↑")
    with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
    with m3: st.metric("Resource Leak", "Low", "Stable")
    
    st.markdown('<div class="insight-card"><strong>🦉 תובנת אוריון:</strong> זוהה עומס קוגניטיבי גבוה ב-Backend. מומלץ לאחד משימות ל-Epic אחד.</div>', unsafe_allow_html=True)

    # גרפים אינטראקטיביים עם צבעים מקוריים
    st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
    g1, g2, g3 = st.columns(3)
    chart_data = pd.DataFrame(np.random.randint(5, 15, size=(10, 3)), columns=['V1', 'V2', 'V3'])
    
    with g1:
        st.write("**🧠 עומס קוגניטיבי**")
        st.area_chart(chart_data['V1'], color="#FFADCC", height=160)
    with g2:
        st.write("**📢 חוסר בתקשורת**")
        st.line_chart(chart_data['V2'], color="#FFAB00", height=160)
    with g3:
        st.write("**📅 עמידה בלו\"ז**")
        st.bar_chart(chart_data['V3'], color="#5243AA", height=160)
