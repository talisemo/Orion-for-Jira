import streamlit as st
import base64
import os
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף - חובה כהתחלה
st.set_page_config(
    page_title="Orion Executive Insights",
    page_icon="logo.png",
    layout="wide"
)

# פונקציה לטעינת לוגו בצורה יציבה
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# 2. CSS מתקדם לתיקון רזולוציה ו-RTL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* מניעת מריחה ברזולוציות נמוכות */
    .main .block-container {
        max-width: 1200px;
        padding: 1rem 2rem;
    }

    /* קיבוע לוגו בצד ימין */
    .logo-header {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 10px;
    }
    .logo-header img {
        height: 60px; /* גובה קבוע שיראה טוב תמיד */
        width: auto;
    }

    /* עיצוב כרטיסי מדדים */
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
    }

    /* תיבת תובנה */
    .insight-card {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 15px;
        border-radius: 4px;
        margin: 20px 0;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header עם לוגו (צד ימין)
logo_b64 = get_base64_logo("logo.png")
col_title, col_logo = st.columns([5, 1])

with col_logo:
    if logo_b64:
        st.markdown(f'<div class="logo-header"><img src="data:image/png;base64,{logo_b64}"></div>', unsafe_allow_html=True)
    else:
        st.subheader("Orion")

with col_title:
    st.markdown("<h1 style='margin:0;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.caption(f"Jira Cloud Connected | {datetime.now().strftime('%H:%M')} ✅")

st.markdown("---")

# 4. Sidebar (צ'אט) - רוחב קבוע
with st.sidebar:
    st.markdown("### ✨ שאל את אוריון")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("שאלי..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

# 5. מדדים (Real-time)
st.markdown("### 📌 תמונת מצב אסטרטגית")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Resource Leak", "Low", "Stable ✅")
with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
with m3: st.metric("Sentiment Score", "7.2/10", "+0.4 📈")

st.markdown("""
    <div class="insight-card">
        <strong>🦉 ניתוח אוריון:</strong> זיהיתי עומס קוגניטיבי חריג בצוות ה-Backend. 
        הדבר נובע מריבוי משימות קטנות שקוטעות את רצף העבודה. מומלץ לרכז משימות ב-Daily הבא.
    </div>
""", unsafe_allow_html=True)

# 6. גרפי עומק (Trends)
st.markdown("### 📈 מגמות עומק (Exclusive Data)")
g1, g2 = st.columns(2)

# נתונים מדומים
data = pd.DataFrame(np.random.randint(5, 15, size=(10, 2)), columns=['Switching', 'Sentiment'])

with g1:
    st.write("**🧠 עומס קוגניטיבי (Context Switching)**")
    st.area_chart(data['Switching'], color="#FFAB00", height=150)
with g2:
    st.write("**💬 מצב רוח צוותי (Sentiment Drift)**")
    st.line_chart(data['Sentiment'], color="#36B37E", height=150)

# 7. כפתורי פעולה - מתוקנים (בלי Syntax Error)
st.markdown("### ⚡ פעולות ניהוליות")
c1, c2, c3 = st.
