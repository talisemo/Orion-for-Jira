import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# 1. הגדרות דף - האייקון השקוף לטאב
st.set_page_config(
    page_title="Orion - Smart Executive Insights",
    page_icon="icon.png", 
    layout="wide"
)

# 2. עיצוב CSS (מותאם ל-Jira Soft Blue ויישור לימין)
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
        box-shadow: 0 4px 12px rgba(0, 101, 255, 0.05);
    }

    .insight-box {
        background-color: var(--light-blue-hover);
        border-right: 6px solid var(--jira-soft-blue);
        padding: 20px;
        border-radius: 4px;
        color: #172B4D;
        font-size: 1.1rem;
    }

    .stButton>button {
        border-radius: 20px;
        border: 1px solid var(--jira-soft-blue);
        color: var(--jira-soft-blue);
        background-color: white;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: var(--jira-soft-blue);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. כותרת האפליקציה עם הלוגו המלא
col_logo, col_title = st.columns([0.2, 0.8])
with col_logo:
    # הצגת הלוגו המלא בתוך האפליקציה
    try:
        st.image("logo.jpg", width=180)
    except:
        st.write("### Orion")

with col_title:
    st.title("מרכז התובנות של Orion")
    st.caption(f"● סריקה אחרונה: {datetime.now().strftime('%H:%M')} | מסונכרן עם Jira Cloud")

st.markdown("---")

# 4. מבנה העמוד: נתונים בצד ימין, צ'אט בצד שמאל
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### 🎯 מדדים אסטרטגיים")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Scope Outflow", "3", "משימות")
    with m2: st.metric("Cycle Time", "5.2 ימים", "+1.2")
    with m3: st.metric("Risk Level", "Medium", "Stable")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # תיבת תובנות AI
    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 ניתוח אוריון (AI Insights):</strong><br>
            זיהיתי מגמת האטה בביצועי ה-Frontend. <b>אלון</b> ו<b>דנה</b> נמצאים בצוואר בקבוק במשימת ה-Integration. 
            מומלץ לבדוק בדיילי האם יש חוסם טכני או צורך בעזרה מרוני.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # כפתורי פעולה מהירים (ללא אימוג'ים בתוך הטקסט למניעת שגיאות)
    st.markdown("### 🛠️ פעולות מהירות")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("הפק דווח סטטוס"):
            st.info("מייצר דווח סטטוס על בסיס נתוני הג'ירה...")
    with c2: 
        if st.button("ניתוח סיכונים"):
            st.warning("סורק חריגות ועיכובים בלו"ז...")
    with c3: 
        if st.button("תקציר דיילי"):
            st.success("מכין נקודות מרכזיות לישיבת הבוקר...")

with col_chat:
    st.markdown("### 🦉 שאל את אוריון")
    
    # ניהול זיכרון הצ'אט
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! אני אוריון. אני סורק את הג'ירה ברקע. יש משהו ספציפי שתרצי שאבדוק?"}]

    # הצגת היסטוריית ההודעות
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # קלט מהמשתמש וחיבור ל-Gemini
    if prompt := st.chat_input("שאל את אוריון..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): 
            st.markdown(prompt)
        
        # ניסיון התחברות ל-API
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
                st.error(f"שגיאה בחיבור ל-AI: {e}")
        else:
            with st.chat_message("assistant"):
                st.markdown("היי! כדי שאוכל לענות, את צריכה להגדיר את ה-API Key ב-Secrets של Streamlit.")
