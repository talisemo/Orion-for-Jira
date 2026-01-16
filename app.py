import streamlit as st
import google.generativeai as genai
from datetime import datetime
import pandas as pd
import numpy as np
import os

# 1. הגדרות דף
st.set_page_config(
    page_title="Orion | Executive Insights",
    page_icon="logo.png", 
    layout="wide"
)

# 2. CSS ברמת גימור גבוהה
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@200;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* לוגו צף בפינה השמאלית העליונה */
    .logo-container {
        position: absolute;
        left: 20px;
        top: -60px;
    }

    /* כרטיסי מדדים נקיים */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 20px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* תיבת תובנות AI */
    .insight-box {
        background-color: #DEEBFF;
        border-right: 6px solid #0052CC;
        padding: 20px;
        border-radius: 4px;
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
        height: 3.5em;
        width: 100%;
    }
    
    /* הפרדה ויזואלית לגרפים */
    .graph-section {
        background-color: #FAFBFC;
        padding: 20px;
        border-radius: 8px;
        border: 1px dashed #DFE1E6;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - צ'אט נקי בלבד
with st.sidebar:
    st.markdown("### ✨ שאל את אוריון")
    st.caption("AI Assistant connected to Jira Cloud")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור?"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if prompt := st.chat_input("שאלי משהו..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.rerun()

# 4. Header ראשי - כותרת ולוגו בשורה אחת
head_col1, head_col2 = st.columns([4, 1])
with head_col1:
    st.markdown("<h1 style='margin:0;'>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.caption(f"סנכרון פעיל: {datetime.now().strftime('%H:%M')} | Jira Cloud ✅")
with head_col2:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=120)

st.markdown("---")

# 5. תוכן מרכזי
# א) מדדים (Snapshots)
st.markdown("### 📌 תמונת מצב נוכחית")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Scope Outflow", "3", "משימות חריגות")
with m2: st.metric("Cycle Time", "5.2 ימים", "1.2+ ⚠️")
with m3: st.metric("Risk Level", "Medium", "Stable ✅")

# ב) תובנת AI
st.markdown(f"""
    <div class="insight-box">
        <strong>🦉 תובנת אוריון:</strong><br>
        הגרפים מראים מגמת עלייה ב-Velocity הצוותי, אך שימי לב שזמן סגירת המשימות (Cycle Time) עלה מעט ביומיים האחרונים. 
        זה מצביע על "צוואר בקבוק" בבדיקות ה-QA.
    </div>
""", unsafe_allow_html=True)

# ג) גרפי מגמה - מופרדים ויזואלית
st.markdown("### 📈 מגמות וביצועים (Trends)")
with st.container():
    st.markdown('<div class="graph-section">', unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    
    # נתונים לגרפים
    trend_data = pd.DataFrame(np.random.randint(10, 50, size=(10, 2)), columns=['Velocity', 'Quality'])
    
    with g1:
        st.caption("Velocity צוותי (שבועי)")
        st.bar_chart(trend_data['Velocity'], color="#0052CC", height=200)
    with g2:
        st.caption("מדד איכות קוד (נסיגה/שיפור)")
        st.line_chart(trend_data['Quality'], color="#36B37E", height=200)
    st.markdown('</div>', unsafe_allow_html=True)

# ד) פעולות
st.markdown("<br>### ⚡ פעולות ניהוליות", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.button("📝 הפקת דוח סטטוס")
with c2: st.button("🔍 ניתוח סיכונים")
with c3: st.button("📅 תקציר ישיבה")
