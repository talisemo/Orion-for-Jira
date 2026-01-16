import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# 1. הגדרות דף - שימוש באייקון השקוף לטאב
st.set_page_config(
    page_title="Orion - Smart Executive Insights",
    page_icon="icon.png", 
    layout="wide"
)

# 2. עיצוב CSS מותאם ל-Jira ויישור RTL
st.markdown("""
    <style>
    :root {
        --jira-soft-blue: #0065FF;
        --jira-background: #F4F5F7;
        --light-blue-hover: #DEEBFF;
    }

    .stApp { direction: rtl; text-align: right; background-color: var(--jira-background); }
    
    h1, h2, h3, p, span, div, [data-testid="stMarkdownContainer"] {
        text-align: right !important;
        direction: rtl !important;
    }

    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #DFE1E6;
        border-top: 5px solid var(--jira-soft-blue);
        border-radius: 8px;
    }

    .insight-box {
        background-color: var(--light-blue-hover);
        border-right: 6px solid var(--jira-soft-blue);
        padding: 20px;
        border-radius: 4px;
        color: #172B4D;
    }

    .stButton>button {
        border-radius: 20px;
        border: 1px solid var(--jira-soft-blue);
        color: var(--jira-soft-blue);
        background-color: white;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. כותרת האפליקציה עם לוגו
col_logo, col_title = st.columns([0.2, 0.8])
with col_logo:
    try:
        st.image("logo.jpg", width=180)
    except:
        st.write("### Orion")

with col_title:
    st.title("מרכז התובנות של Orion")
    st.caption(f"סנכרון אחרון: {datetime.now().strftime('%H:%M')}")

st.markdown("---")

# 4. תוכן האפליקציה
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### מדדים אסטרטגיים")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Scope Outflow", "3", "משימות")
    with m2: st.metric("Cycle Time", "5.2 ימים", "+1.2")
    with m3: st.metric("Risk Level", "Medium", "Stable")

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="insight-box">
            <strong>ניתוח אוריון:</strong><br>
            זיהיתי האטה בביצועי ה-Frontend. אלון ודנה נמצאים בצוואר בקבוק.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>### פעולות מהירות")
    c1, c2, c3 = st.columns(3)
    
    # תיקון השגיאה: טקסטים נקיים ללא סימנים מיוחדים בתוך הפונקציה
    with c1: 
        if st.button("הפקת דוח סטטוס"):
            st.info("מייצר דוח סטטוס כעת")
    with c2: 
        if st.button("ניתוח סיכונים"):
            st.warning("סורק חריגות בנתונים")
    with c3: 
        if st.button("תקציר יומי"):
            st.success("מכין תקציר לישיבה")

with col_chat:
    st.markdown("### שאל את אוריון")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי, איך אני יכול לעזור היום?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("כתבי כאן..."):
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
            except Exception as e:
                st.error("חלה שגיאה בחיבור לבינה המלאכותית")
