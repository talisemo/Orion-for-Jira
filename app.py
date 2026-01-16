import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os
import pandas as pd
import numpy as np

# 1. הגדרות דף - אייקון וטאב
st.set_page_config(
    page_title="Orion | Smart Executive Insights",
    page_icon="icon.png", 
    layout="wide"
)

# 2. עיצוב CSS - החזרת הכחול העמוק והיוקרתי
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    :root {
        --orion-blue: #0052CC; /* הכחול העמוק של אוריון/ג'ירה */
        --orion-light-blue: #DEEBFF;
    }

    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .stApp { background-color: #F4F5F7; }

    /* עיצוב כרטיסי המדדים והגרפים */
    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #DFE1E6;
        border-top: 5px solid var(--orion-blue);
        border-radius: 12px;
        padding: 15px !important;
    }

    /* תיבת תובנות AI מלוטשת */
    .insight-box {
        background: white;
        border-right: 8px solid var(--orion-blue);
        padding: 25px;
        border-radius: 8px;
        margin: 20px 0;
        color: #172B4D;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    /* כפתורי פעולה בכחול עמוק */
    .stButton>button {
        border-radius: 10px;
        border: 2px solid var(--orion-blue);
        color: var(--orion-blue);
        background-color: white;
        font-weight: bold;
        height: 3.5em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: var(--orion-blue);
        color: white;
    }

    /* תיקון צבע הגרפים לדיפולט כחול אוריון */
    .stPlotlyChart { color: var(--orion-blue); }
    </style>
    """, unsafe_allow_html=True)

# 3. באנר עליון
col_title, col_logo = st.columns([4, 1])

with col_title:
    st.title("מרכז התובנות של Orion")
    st.caption(f"✨ סנכרון אחרון: {datetime.now().strftime('%H:%M')} | Jira Cloud Connected")

with col_logo:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=140)
    elif os.path.exists("logo.png"):
        st.image("logo.png", width=140)

st.markdown("---")

# 4. חלוקת העמוד הראשי
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### 📊 מגמות וביצועים")
    
    # החזרת הגרפים הויזואליים
    m1, m2 = st.columns(2)
    
    with m1:
        st.write("**Cycle Time (שבועי)**")
        chart_data = pd.DataFrame(np.random.randn(10, 1), columns=['ימים'])
        st.area_chart(chart_data, height=150, use_container_width=True)
        st.metric("ממוצע נוכחי", "5.2 ימים", "1.2+ ⚠️")

    with m2:
        st.write("**משימות שהושלמו (Velocity)**")
        chart_data2 = pd.DataFrame(np.random.randn(10, 1), columns=['Tasks'])
        st.area_chart(chart_data2, height=150, use_container_width=True)
        st.metric("Scope Outflow", "3", "משימות חריגות")

    st.markdown("""
        <div class="insight-box">
            <strong>🦉 תובנת אוריון:</strong><br>
            זיהיתי צוואר בקבוק בצוות ה-Frontend. המשימות של <b>אלון ודנה</b> מעכבות את ה-Integration. 
            מומלץ לתת עדיפות ב-Daily הקרוב לסגירת ה-PRs הפתוחים.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ פעולות מהירות")
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝 הפקת דוח סטטוס")
    with c2: st.button("🔍 ניתוח סיכונים")
    with c3: st.button("📅 תקציר דיילי")

with col_chat:
    st.markdown("### 🦉 שאל את אוריון")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! אני אוריון. איך אני יכולה לעזור לך עם נתוני הג'ירה היום?"}]

    chat_container = st.container(height=450)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("למשל: איזה צוות הכי יעיל החודש?"):
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
                st.error("שגיאה בחיבור ל-AI.")
