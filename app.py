import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# הגדרות דף - כאן אנחנו מחליפים את הינשוף בלוגו החדש בטאב!
st.set_page_config(
    page_title="Orion - Smart Executive Insights",
    page_icon="logo.png", # כאן הקסם קורה - הלוגו יופיע בטאב של הדפדפן
    layout="wide"
)

# CSS עם הכחול הרך המדויק (#0065FF) והיישור לימין
st.markdown("""
    <style>
    :root {
        --jira-soft-blue: #0065FF;
        --jira-background: #F4F5F7;
        --light-blue-hover: #DEEBFF;
    }

    .stApp { direction: rtl; text-align: right; background-color: var(--jira-background); }
    
    /* יישור כותרות וטקסט */
    h1, h2, h3, p, span, div, [data-testid="stMarkdownContainer"] {
        text-align: right !important;
        direction: rtl !important;
    }

    /* כרטיסי מדדים בכחול של אוריון */
    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #DFE1E6;
        border-top: 5px solid var(--jira-soft-blue);
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 101, 255, 0.05);
    }

    /* תיבת התובנה של אוריון */
    .insight-box {
        background-color: var(--light-blue-hover);
        border-right: 6px solid var(--jira-soft-blue);
        padding: 20px;
        border-radius: 4px;
        color: #172B4D;
        font-size: 1.1rem;
    }

    /* עיצוב כפתורים מעוגלים ומקצועיים */
    .stButton>button {
        border-radius: 20px;
        border: 1px solid var(--jira-soft-blue);
        color: var(--jira-soft-blue);
        background-color: white;
        padding: 0.5rem 2rem;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: var(--jira-soft-blue);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# כותרת עם הלוגו החדש
col_logo, col_title = st.columns([0.1, 0.9])
with col_logo:
    st.image("logo.png", width=70) # הלוגו החדש והמדהים שלך
with col_title:
    st.title("מרכז התובנות של Orion")
    st.caption(f"● סריקה אחרונה: {datetime.now().strftime('%H:%M')} | מסונכרן עם Jira Cloud")

st.markdown("---")

# המשך הממשק (כמו קודם, אבל עם העיצוב החדש)
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### 🎯 מדדים אסטרטגיים")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Scope Outflow", "3", "משימות")
    with m2: st.metric("Cycle Time", "5.2 ימים", "+1.2")
    with m3: st.metric("Risk Level", "Medium", "Stable")

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 ניתוח אוריון (AI Insights):</strong><br>
            זיהיתי מגמת האטה בביצועי ה-Frontend. <b>אלון</b> ו<b>דנה</b> נמצאים בצוואר בקבוק במשימת ה-Integration. 
            מומלץ לבדוק בדיילי האם יש חוסם טכני או צורך בעזרה מרוני.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🛠️ פעולות מהירות")
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝 דו"ח סטטוס")
    with c2: st.button("🔍 ניתוח סיכונים")
    with c3: st.button("⏰ תקציר דיילי")

with col_chat:
    # כאן הינשוף נשאר בתור ה-Avatar של הצ'אט
    st.markdown("### 🦉 שאל את אוריון")
    # ... (שאר קוד הצ'אט)
