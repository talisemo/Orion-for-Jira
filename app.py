import streamlit as st
import os
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרת טאב הדפדפן (Favicon) - ודאי שזה logo.png
st.set_page_config(
    page_title="Orion | Executive Insights",
    page_icon="logo.png", 
    layout="wide"
)

# 2. CSS לקיבוע הלוגו בפינה הימנית העליונה
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@200;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* קיבוע הלוגו בפינה הימנית העליונה */
    .fixed-logo {
        position: absolute;
        top: -60px; /* גובה מעל הכותרת */
        right: 20px; /* הצמדה לימין */
        z-index: 1000;
    }
    
    .fixed-logo img {
        width: 120px; /* גודל קבוע ללוגו */
    }

    /* עיצוב כותרת וסנכרון */
    .header-section {
        margin-top: -10px;
        margin-bottom: 30px;
        padding-bottom: 15px;
        border-bottom: 1px solid #EBECF0;
    }

    /* כרטיסי המדדים */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 20px !important;
    }

    /* תיבת התובנות */
    .insight-box {
        background-color: #DEEBFF;
        border-right: 6px solid #0052CC;
        padding: 20px;
        border-radius: 4px;
        color: #172B4D;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. הצגת הלוגו בפינה הימנית (באמצעות קישור או קובץ מקומי)
# אם הקובץ בגיטהאב, עדיף להשתמש בקישור ה-RAW שלו בתוך ה-src
st.markdown(f'''
    <div class="fixed-logo">
        <img src="https://raw.githubusercontent.com/[USER]/[REPO]/main/logo.png" onerror="this.src='https://via.placeholder.com/120x40?text=Orion'">
    </div>
''', unsafe_allow_html=True)

# 4. כותרת הדף (מיושרת לימין)
st.markdown(f"""
    <div class="header-section">
        <h1 style="margin:0; color:#172B4D;">מרכז התובנות של Orion</h1>
        <p style="color:#6B778C; margin:0;">
            Jira Cloud Active ● סנכרון אחרון: {datetime.now().strftime('%H:%M')}
        </p>
    </div>
""", unsafe_allow_html=True)

# 5. מבנה הדף
m1, m2, m3 = st.columns(3)
with m1: st.metric("Sentiment Score", "7.2/10", "+0.4 📈")
with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
with m3: st.metric("Resource Leak", "Low", "Stable ✅")

st.markdown('<div class="insight-box"><strong>🦉 תובנת אוריון:</strong> זיהיתי עומס קוגניטיבי גבוה בצוות ה-Backend. מומלץ לבדוק אם יש יותר מדי פגישות שקוטעות את רצף העבודה.</div>', unsafe_allow_html=True)

# 6. גרפים - ניתוק ויזואלי מהמדדים
st.markdown("### 📈 ניתוח מגמות עומק")
g1, g2 = st.columns(2)
with g1:
    st.write("**🧠 עומס קוגניטיבי (Context Switching)**")
    st.area_chart(np.random.randint(2, 10, size=(15, 1)), color="#FFAB00", height=200)
with g2:
    st.write("**💬 מצב רוח צוותי (Sentiment Drift)**")
    st.line_chart(np.random.uniform(5, 9, size=(15, 1)), color="#36B37E", height=200)

# 7. Sidebar לצ'אט נקי
with st.sidebar:
    st.markdown("### ✨ שאל את אוריון")
    st.caption("AI Assistant connected to Jira")
    # כאן יבוא הקוד של הצ'אט שכתבנו...
