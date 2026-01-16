import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף - נשמר יציב
st.set_page_config(
    page_title="Orion Executive Insights",
    page_icon="logo.png", 
    layout="wide"
)

# 2. CSS - כל התיקונים הויזואליים בפנים
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
        max-width: 1100px;
        padding: 2rem;
        margin: 0 auto;
    }

    /* יישור ימני קשיח להדר */
    .header-section {
        text-align: right;
        width: 100%;
        margin-bottom: 20px;
    }

    .sync-text {
        color: #28a745;
        font-size: 0.85rem;
        display: block;
        margin-top: -5px;
    }

    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
    }

    .insight-card {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 15px;
        border-radius: 4px;
        margin: 20px 0;
    }
    
    .orion-icon {
        width: 24px;
        height: 24px;
        background-image: url('https://img.icons8.com/fluency/48/brain.png');
        background-size: contain;
        background-repeat: no-repeat;
        display: inline-block;
        vertical-align: middle;
        margin-left: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown(f"""
    <div class="header-section">
        <h1 style='margin:0;'>מרכז התובנות של Orion</h1>
        <span class="sync-text">✅ Jira Cloud Connected | {datetime.now().strftime("%H:%M")}</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 4. Sidebar
with st.sidebar:
    st.markdown('<div style="font-weight:600; font-size:1.1rem; margin-bottom:15px;"><span class="orion-icon"></span>שאל את אוריון</div>', unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("שאלי..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

# 5. מדדים
st.markdown("### 📌 תמונת מצב")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Resource Leak", "Low", "Stable")
with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
with m3: st.metric("Communication Gaps", "2.4", "-0.8") # המדד החדש כאן

st.markdown("""
    <div class="insight-card">
        <strong>🦉 תובנת אוריון:</strong> זיהיתי עלייה ב-"Communication Gaps" סביב משימות ה-API. מומלץ לוודא סנכרון בין צוותי ה-Frontend וה-Backend.
    </div>
""", unsafe_allow_html=True)

# 6. גרפים
st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
g1, g2 = st.columns(2)

data = pd.DataFrame(np.random.randint(5, 15, size=(12, 2)), columns=['A', 'B'])

with g1:
    st.write("**🧠 עומס קוגניטיבי (Context Switching)**")
    st.area_chart(data['A'], color="#FFADCC", height=180) # ורוד מוח נשמר

with g2:
    st.write("**📢 חוסר בתקשורת סביב משימות (Communication Gaps)**")
    st.line_chart(data['B'], color="#FFAB00", height=180) # כתום אזהרה

# 7. פעולות
st.markdown("### ⚡ פעולות ניהוליות")
c1, c2, c3 = st.columns(3)
with c1: st.button("📊 הפקת דוח סטטוס")
with c2: st.button("🔍 ניתוח סיכונים")
with c3: st.button("📅 נושאים לדיילי")
