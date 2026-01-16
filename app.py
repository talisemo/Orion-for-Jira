import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os

# 1. הגדרות דף
st.set_page_config(
    page_title="Orion | Executive Insights",
    page_icon="icon.png", 
    layout="wide"
)

# 2. CSS מקצועי - שפת העיצוב של Atlassian (Jira)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@200;300;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .stApp { background-color: #FFFFFF; }

    /* עיצוב כרטיסי המדדים */
    [data-testid="stMetric"] {
        background-color: #FAFBFC;
        border: 1px solid #DFE1E6;
        border-radius: 3px;
        padding: 20px !important;
    }

    /* תיבת תובנות AI בכחול העדין */
    .insight-box {
        background-color: #DEEBFF;
        border-right: 6px solid #0052CC;
        padding: 25px;
        border-radius: 3px;
        color: #172B4D;
        margin: 20px 0;
    }

    /* כפתורי Jira Primary */
    .stButton>button {
        background-color: #0052CC;
        color: white;
        border-radius: 3px;
        border: none;
        font-weight: 600;
        height: 3.2em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #0065FF;
        color: white;
    }

    /* כותרות סקשנים עם אייקונים */
    .section-title {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.4rem;
        font-weight: 600;
        color: #172B4D;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header - לוגו ונוכחות מותגית
header_col1, header_col2 = st.columns([1, 5])

with header_col1:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=180)
    elif os.path.exists("logo.png"):
        st.image("logo.png", width=180)

with header_col2:
    st.markdown("<h1 style='margin-top: 10px;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #6B778C; margin-top: -10px;'>סנכרון אחרון: {datetime.now().strftime('%H:%M')} | Jira Cloud Active</p>", unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid #EBECF0; margin-top: 0;'>", unsafe_allow_html=True)

# 4. חלוקת העמוד המרכזי
col_main, col_chat = st.columns([2, 1])

with col_main:
    st.markdown('<div class="section-title">📊 מדדים אסטרטגיים</div>', unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Scope Outflow", "3", "משימות חריגות")
    with m2:
        st.metric("Cycle Time", "5.2 ימים", "1.2+ ⚠️")
    with m3:
        st.metric("Risk Level", "Medium", "Stable ✅")

    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 ניתוח אוריון:</strong><br>
            זיהיתי האטה בביצועי ה-Frontend. צוות הפיתוח נמצא בעומס נקודתי על משימות ה-Integration. 
            מומלץ לתעדף סגירת PRs פתוחים ב-Daily הקרוב.
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">⚡ פעולות ניהוליות</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    # הוספת אייקונים לכפתורים
    with c1: st.button("📝 הפקת דוח סטטוס")
    with c2: st.button("🔍 ניתוח סיכונים")
    with c3: st.button("📅 תקציר ישיבה")

with col_chat:
    st.markdown('<div class="section-title">✨ שאל את אוריון</div>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור היום?"}]

    chat_container = st.container(height=450)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("למשל: איזה צוות הכי עמוס?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if api_key:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                with st.chat_message("assistant"):
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
            except:
                st.error("חיבור ל-AI נכשל.")
