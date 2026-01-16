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

# 2. CSS מתקדם - פתרון בעיית המרווחים והצ'אט
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@200;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .stApp { background-color: #FFFFFF; }

    /* עיצוב Header נקי - לוגו בצד הכותרת */
    .header-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 2px solid #EBECF0;
        margin-bottom: 2rem;
    }

    /* עיצוב מדדים עם גרף מגמה בפנים */
    .metric-card {
        background-color: #FAFBFC;
        border: 1px solid #DFE1E6;
        border-radius: 3px;
        padding: 15px;
    }

    /* תיבת תובנות - כחול עדין */
    .insight-box {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 20px;
        border-radius: 3px;
        margin: 20px 0;
    }

    /* צמצום הצ'אט שלא ימרח את העמוד */
    [data-testid="stChatMessageContainer"] {
        max-height: 400px;
        overflow-y: auto;
    }
    
    /* עיצוב כפתורים */
    .stButton>button {
        background-color: #0052CC;
        color: white;
        border-radius: 3px;
        font-weight: 600;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. בניית ה-Header (לוגו + כותרת בשורה אחת)
col_h1, col_h2 = st.columns([4, 1])
with col_h1:
    st.markdown("<h1 style='margin:0;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.caption(f"סנכרון פעיל: {datetime.now().strftime('%H:%M')} | Jira Cloud Active ✨")
with col_h2:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=120)

st.markdown("---")

# 4. חלוקת העמוד - תוכן מרכזי וצ'אט בצד
col_main, col_spacer, col_chat = st.columns([1.5, 0.1, 1])

with col_main:
    st.markdown("### 📊 מדדים ומגמות (Real-time Trends)")
    
    m1, m2, m3 = st.columns(3)
    
    # פונקציה לייצור גרף מגמה קטן (Sparkline)
    def trend_chart():
        chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['trend'])
        st.line_chart(chart_data, height=60, use_container_width=True)

    with m1:
        st.metric("Scope Outflow", "3", "משימות חריגות")
        trend_chart() # גרף מגמה מתחת למדד
    with m2:
        st.metric("Cycle Time", "5.2 ימים", "1.2+ ⚠️")
        trend_chart()
    with m3:
        st.metric("Risk Level", "Medium", "Stable ✅")
        trend_chart()

    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 תובנת אוריון:</strong><br>
            זיהיתי צוואר בקבוק בצוות ה-Frontend. המשימות של <b>אלון ודנה</b> מעכבות את ה-Integration. 
            מומלץ לתת עדיפות לסגירת PRs פתוחים ב-Daily הקרוב.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ פעולות ניהוליות")
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝 הפקת דוח סטטוס")
    with c2: st.button("🔍 ניתוח סיכונים")
    with c3: st.button("📅 תקציר ישיבה")

with col_chat:
    st.markdown("### ✨ שאל את אוריון")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]

    # מיכל צ'אט מוגבל בגובה
    with st.container(height=400):
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])

    if prompt := st.chat_input("שאלי את אוריון..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
