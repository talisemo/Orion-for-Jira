import streamlit as st
import base64
import os
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף - חייב להיות ראשון בקוד עבור הטאב (Favicon)
st.set_page_config(
    page_title="Orion Dashboard",
    page_icon="logo.png", # זה מסדר את התמונה בטאב
    layout="wide"
)

# פונקציה להצגת לוגו בצורה חסינה
def get_base64_logo(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# 2. CSS מתקדם לתיקון רזולוציה ויישור (RTL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* הגבלת רוחב כדי למנוע מריחה ב-25% זום */
    .main .block-container {
        max-width: 1200px;
        padding: 2rem;
        margin: 0 auto;
    }

    /* עיצוב הלוגו בפינה הימנית */
    .logo-container {
        display: flex;
        justify-content: flex-start;
        margin-bottom: -20px;
    }
    .logo-container img {
        width: 180px !important;
        height: auto;
    }

    /* מדדים ותובנות */
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #DFE1E6;
        border-radius: 10px;
        padding: 15px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .insight-card {
        background-color: #DEEBFF;
        border-right: 6px solid #0052CC;
        padding: 20px;
        border-radius: 4px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header - כותרת ולוגו
logo_b64 = get_base64_logo("logo.png")
h1, h2 = st.columns([4, 1])

with h2:
    if logo_b64:
        st.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo_b64}"></div>', unsafe_allow_html=True)
    else:
        st.subheader("Orion")

with h1:
    st.markdown("<h1 style='margin:0;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.caption(f"סנכרון פעיל: {datetime.now().strftime('%H:%M')} | Jira Cloud Connected ✅")

st.markdown("---")

# 4. Sidebar (צ'אט) - כדי שלא יפריע למבנה העמוד
with st.sidebar:
    st.markdown("### ✨ שאל את אוריון")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("שאלי..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

# 5. תוכן מרכזי - מדדים
st.markdown("### 📊 תמונת מצב")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Risk Level", "Medium", "Stable ✅")
with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
with m3: st.metric("Sentiment Score", "7.2/10", "+0.4 📈")

st.markdown("""
    <div class="insight-card">
        <strong>🦉 תובנת אוריון:</strong> זיהיתי עומס קוגניטיבי גבוה בצוות ה-Backend עקב ריבוי משימות קטנות. מומלץ לאחד משימות ל-Epic אחד כדי לשפר את הפוקוס ב-Sprint הנוכחי.
    </div>
""", unsafe_allow_html=True)

# 6. גרפים - הערך המוסף
st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
g1, g2 = st.columns(2)

data = pd.DataFrame(np.random.randint(5, 15, size=(12, 2)), columns=['Switching', 'Sentiment'])

with g1:
    st.write("**🧠 עומס קוגניטיבי (Context Switching)**")
    st.area_chart(data['Switching'], color="#FFAB00", height=180)

with g2:
    st.write("**💬 מדד שביעות רצון (AI Analysis)**")
    st.line_chart(data['Sentiment'], color="#36B37E", height=180)

# 7. פעולות - כאן תוקנו השגיאות מהצילום מסך
st.markdown("### ⚡ פעולות ניהוליות")
c1, c2, c3 = st.columns(3)
with c1: 
    st.button("📊 הפקת דוח סטטוס")
with c2: 
    st.button("🔍 ניתוח סיכונים")
with c3: 
    st.button("📅 תקציר ישיבה")
