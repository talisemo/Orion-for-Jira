import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף - טאב (Favicon) ולוגו
st.set_page_config(
    page_title="Orion Executive Insights",
    page_icon="logo.png", 
    layout="wide"
)

# 2. CSS מקצועי - כל התיקונים הויזואליים במקום אחד
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* מניעת מריחת תוכן ברזולוציות נמוכות (זום 25%) */
    .main .block-container {
        max-width: 1100px;
        padding: 2rem;
        margin: 0 auto;
    }

    /* יישור ימני קבוע לכותרת ולסנכרון */
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

    /* עיצוב כרטיסי המדדים */
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* תיבת תובנות AI */
    .insight-card {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 15px;
        border-radius: 4px;
        margin: 20px 0;
        line-height: 1.6;
    }
    
    /* אייקון אוריון בתוך הצ'אט */
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

    /* עיצוב כפתורי "תובנות מהירות" בצד */
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        font-size: 0.8rem;
        padding: 2px 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header האתר (ללא לוגו - נקי ומקצועי)
st.markdown(f"""
    <div class="header-section">
        <h1 style='margin:0;'>מרכז התובנות של Orion</h1>
        <span class="sync-text">✅ Jira Cloud Connected | {datetime.now().strftime("%H:%M")}</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 4. Sidebar - שאל את אוריון + "תובנות מהירות" (הפתרון לעול ה-JQL)
with st.sidebar:
    st.markdown('<div style="font-weight:600; font-size:1.1rem; margin-bottom:10px;"><span class="orion-icon"></span>שאל את אוריון</div>', unsafe_allow_html=True)
    
    st.caption("תובנות מהירות (בלי לכתוב קוד):")
    
    # משתנה עזר לניהול השאלות המוכנות
    quick_query = None
    
    # כפתורי פעולה מהירים
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🚨 מי תקוע?"):
            quick_query = "מי צווארי בקבוק המרכזיים בצוות כרגע?"
    with col_b:
        if st.button("⚠️ סיכון ספרינט"):
            quick_query = "אילו משימות בסכנת איחור משמעותית?"
    
    if st.button("📉 למה ה-Focus Factor ירד?"):
        quick_query = "נתח מדוע מדד הפוקוס ירד ב-5% האחרונים"

    st.markdown("---")

    # ניהול הודעות הצ'אט
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, במה אוכל לעזור היום?"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            
    # קלט משתמש (ידני או מהכפתורים)
    prompt = st.chat_input("שאלי את אוריון...")
    
    # אם נלחץ כפתור מהיר, נשתמש בו כפרומפט
    final_prompt = prompt or quick_query
    
    if final_prompt:
        st.session_state.messages.append({"role": "user", "content": final_prompt})
        # כאן תבוא הלוגיקה של אוריון בעתיד
        st.session_state.messages.append({"role": "assistant", "content": f"בדקתי עבורך: {final_prompt}... (בשלב זה אני מדמה את התשובה)"})
        st.rerun()

# 5. גוף הדף - מדדים (מבוסס על "אל תכתבי כלום, הכנתי לך")
st.markdown("### 📌 תמונת מצב אסטרטגית")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Resource Leak", "Low", "Stable")
with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
with m3: st.metric("Communication Gaps", "2.4", "-0.8")

st.markdown("""
    <div class="insight-card">
        <strong>🦉 תובנת אוריון (פרואקטיבית):</strong> זיהיתי עלייה ב-<strong>Communication Gaps</strong> סביב משימות ה-API. 
        הפער נוצר כי יש הרבה תגובות ב-Jira ללא סגירת משימה. מומלץ לבצע סנכרון טכני קצר בדיילי.
    </div>
""", unsafe_allow_html=True)

# 6. גרפים - פרופורציונליים וצבעוניים
st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
g1, g2 = st.columns(2)

# יצירת נתונים מדומים לגרפים
chart_data = pd.DataFrame(np.random.randint(5, 15, size=(12, 2)), columns=['Switching', 'Gaps'])

with g1:
    st.write("**🧠 עומס קוגניטיבי (Context Switching)**")
    # ורוד מוח מדויק
    st.area_chart(chart_data['Switching'], color="#FFADCC", height=180)

with g2:
    st.write("**📢 חוסר בתקשורת סביב משימות (Communication Gaps)**")
    # כתום אזהרה למדד פערים
    st.line_chart(chart_data['Gaps'], color="#FFAB00", height=180)

# 7. כפתורי ניהול בתחתית
st.markdown("### ⚡ פעולות ניהוליות")
c1, c2, c3 = st.columns(3)
with c1: st.button("📊 הפקת דוח סטטוס")
with c2: st.button("🔍 ניתוח סיכונים")
with c3: st.button("📅 נושאים לדיילי")
