import streamlit as st
import google.generativeai as genai
from datetime import datetime
import pandas as pd
import numpy as np
import os

# 1. הגדרות דף
st.set_page_config(
    page_title="Orion | Smart Executive Insights",
    page_icon="logo.png", 
    layout="wide"
)

# 2. CSS מקצועי לניקוי הממשק
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@200;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* עיצוב המדדים */
    [data-testid="stMetric"] {
        background-color: #FAFBFC;
        border: 1px solid #DFE1E6;
        border-radius: 4px;
        padding: 15px !important;
    }

    /* תיבת תובנות - כחול Jira */
    .insight-box {
        background-color: #DEEBFF;
        border-right: 6px solid #0052CC;
        padding: 25px;
        border-radius: 4px;
        color: #172B4D;
        margin: 25px 0;
        font-size: 1.1rem;
    }

    /* כפתורי פעולה */
    .stButton>button {
        background-color: #0052CC;
        color: white;
        border: none;
        border-radius: 3px;
        font-weight: 600;
        height: 3.5em;
        width: 100%;
    }
    
    /* סידור ה-Sidebar (הצ'אט) */
    [data-testid="stSidebar"] {
        background-color: #F4F5F7;
        border-left: 1px solid #DFE1E6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - כאן יושב הלוגו והצ'אט
with st.sidebar:
    # לוגו קבוע בראש הצ'אט
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    
    st.markdown("### ✨ שאל את אוריון")
    st.caption("AI Assistant connected to Jira")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]

    # מיכל הודעות
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if prompt := st.chat_input("שאלי משהו..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        # לוגיקה של Gemini (מקוצרת ליציבות)
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.rerun()

# 4. תוכן מרכזי - דאשבורד
st.markdown("<h1 style='color: #172B4D;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
st.caption(f"סנכרון פעיל: {datetime.now().strftime('%H:%M')} | Jira Cloud Connected ✅")
st.markdown("---")

# תצוגת מדדים עם גרפים משמעותיים
st.markdown("### 📊 מדדים אסטרטגיים וביצועים")
m1, m2, m3 = st.columns(3)

# נתוני דוגמה לגרפים (Area Charts נראים הרבה יותר טוב)
chart_data = pd.DataFrame(np.random.rand(10, 1), columns=['Value'])

with m1:
    st.metric("Scope Outflow", "3", "משימות חריגות")
    st.area_chart(chart_data, height=100, use_container_width=True)

with m2:
    st.metric("Cycle Time", "5.2 ימים", "1.2+ ⚠️")
    st.area_chart(chart_data * 1.5, height=100, use_container_width=True)

with m3:
    st.metric("Risk Level", "Medium", "Stable ✅")
    st.area_chart(chart_data * 0.5, height=100, use_container_width=True)

# תיבת תובנות
st.markdown(f"""
    <div class="insight-box">
        <strong>🦉 תובנת אוריון:</strong><br>
        זיהיתי עיכוב משמעותי בשלב ה-Integration. צוות ה-Frontend סיים את חלקו, אך הבדיקות מתעכבות.
        מומלץ להקצות בודק נוסף ל-Sprint הנוכחי.
    </div>
""", unsafe_allow_html=True)

# פעולות ניהוליות
st.markdown("### ⚡ פעולות ניהוליות")
c1, c2, c3 = st.columns(3)
with c1: st.button("📝 הפקת דוח סטטוס")
with c2: st.button("🔍 ניתוח סיכונים")
with c3: st.button("📅 תקציר ישיבה")
