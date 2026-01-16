import streamlit as st
import base64
import os
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף
st.set_page_config(
    page_title="Orion Executive",
    page_icon="logo.png",
    layout="wide"
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 2. CSS רספונסיבי לחלוטין (Responsive)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* הגבלת רוחב התוכן כדי שלא יימרח ברזולוציות גבוהות */
    .block-container {
        max-width: 1200px !important;
        padding-top: 2rem !important;
    }

    /* לוגו גמיש לפי רוחב המסך (vw) */
    .logo-box img {
        width: 15vw !important; 
        min-width: 120px;
        max-width: 220px;
        height: auto;
    }

    /* עיצוב המדדים */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 1rem !important;
    }

    /* תיבת תובנות */
    .insight-box {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 1.5rem;
        border-radius: 4px;
        margin: 1.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
h1, h2 = st.columns([4, 1])

with h2:
    if os.path.exists("logo.png"):
        logo_b64 = get_base64("logo.png")
        st.markdown(f'<div class="logo-box"><img src="data:image/png;base64,{logo_b64}"></div>', unsafe_allow_html=True)

with h1:
    st.markdown("<h1 style='margin:0;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.caption(f"Jira Cloud Connected | {datetime.now().strftime('%H:%M')} ✅")

st.markdown("---")

# 4. Sidebar צ'אט (נשאר קבוע ונוח)
with st.sidebar:
    st.markdown("### ✨ שאל את אוריון")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("שאלי..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

# 5. נתונים (Real-time)
st.markdown("### 📌 מדדים אסטרטגיים")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Risk Level", "Medium", "Stable")
with m2: st.metric("Cycle Time", "5.2 ימים", "+1.2 ⚠️")
with m3: st.metric("Scope Outflow", "3", "משימות חריגות")

st.markdown("""
    <div class="insight-box">
        <strong>🦉 ניתוח אוריון:</strong> זוהתה האטה בביצועי ה-Frontend. 
        צוות הפיתוח נמצא בעומס נקודתי על משימות ה-Integration. מומלץ לתעדף סגירת PRs פתוחים.
    </div>
""", unsafe_allow_html=True)

# 6. גרפים מופרדים (Trends)
st.markdown("### 📈 מגמות וביצועים (Trends)")
g1, g2 = st.columns(2)

data = pd.DataFrame(np.random.randint(10, 50, size=(12, 2)), columns=['A', 'B'])

with g1:
    st.write("**🧠 עומס קוגניטיבי**")
    st.area_chart(data['A'], color="#FFAB00", height=180)

with g2:
    st.write("**💬 מצב רוח צוותי**")
    st.line_chart(data['B'], color="#36B37E", height=180)

# 7. כפתורי פעולה
st.markdown("### ⚡ פעולות")
c1, c2, c3 = st.columns(3)
with c1: st.button("📝 הפקת דוח")
with c2: st.button("🔍 ניתוח סיכ
