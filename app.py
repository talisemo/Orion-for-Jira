import streamlit as st
import os
from datetime import datetime
import pandas as pd
import numpy as np
from PIL import Image

# 1. הגדרות דף
st.set_page_config(
    page_title="Orion | Smart Insights",
    page_icon="logo.png",
    layout="wide"
)

# 2. CSS יציב (RTL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@200;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"], .stText {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* עיצוב המדדים */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* תיבת תובנות */
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

# 3. Header יציב עם לוגו (שימוש ב-PIL לטעינה בטוחה)
head_col1, head_col2 = st.columns([5, 1])

with head_col2:
    try:
        # טעינה באמצעות Image.open מבטיחה ש-Streamlit יזהה את הקובץ
        img = Image.open("logo.png")
        st.image(img, width=130)
    except:
        st.markdown("### 🌌 Orion")

with head_col1:
    st.markdown("<h1 style='margin:0;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.caption(f"סנכרון פעיל: {datetime.now().strftime('%H:%M')} | Jira Cloud Connected ✅")

st.markdown("---")

# 4. Sidebar לצ'אט - פתרון ה"מריחה" על העמוד
with st.sidebar:
    st.markdown("### ✨ שאל את אוריון")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            
    if prompt := st.chat_input("שאלי משהו..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

# 5. תוכן מרכזי
st.markdown("### 📌 תמונת מצב אסטרטגית")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Sentiment Score", "7.2/10", "+0.4 📈")
with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
with m3: st.metric("Resource Leak", "Low", "Stable ✅")

st.markdown(f"""
    <div class="insight-box">
        <strong>🦉 תובנת אוריון:</strong><br>
        המדדים מראים יציבות, אך בגרף ה-Context Switching ניתן לראות קפיצה משמעותית אתמול. 
        זה קרה בגלל ריבוי ישיבות דחופות שקטעו את זמן הפוקוס של צוות הפיתוח.
    </div>
""", unsafe_allow_html=True)

# 6. גרפים - הערך המוסף (Deep Data)
st.markdown("### 📈 ניתוח מגמות עומק (Exclusive)")
g1, g2 = st.columns(2)

# נתונים לגרפים
chart_data = pd.DataFrame(np.random.randint(2, 10, size=(12, 2)), columns=['Switching', 'Sentiment'])

with g1:
    st.write("**🧠 עומס קוגניטיבי (Context Switching)**")
    st.area_chart(chart_data['Switching'], color="#FFAB00", height=200)
    st.caption("מראה כמה פעמים ביום מפתחים נאלצו להחליף קונטקסט בין משימות שונות.")

with g2:
    st.write("**💬 מדד שביעות רצון (Sentiment Drift)**")
    st.line_chart(chart_data['Sentiment'], color="#36B37E", height=200)
    st.caption("ניתוח AI של הטון בתגובות ובמשימות בג'ירה לאורך זמן.")

# 7. פעולות
st.markdown("<br>### ⚡ פעולות ניהוליות", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.button("📊 דוח עומס")
with c2: st.button("🔍 ניתוח סיכונים")
with c3: st.button("📅 סיכום יום")
