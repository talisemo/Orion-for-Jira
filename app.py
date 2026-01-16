import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os

# 1. הגדרות דף - אייקון הטאב
st.set_page_config(
    page_title="Orion Insights",
    page_icon="icon.png", 
    layout="wide"
)

# 2. עיצוב CSS פרימיום - יישור לימין וכחול אוריון
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    :root {
        --orion-blue: #0052CC;
        --bg-light: #F4F5F7;
    }

    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .stApp { background-color: var(--bg-light); }

    /* עיצוב כרטיסי המדדים (המספרים) */
    [data-testid="stMetric"] {
        background-color: white;
        border-right: 6px solid var(--orion-blue);
        border-radius: 8px;
        padding: 20px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    /* תיבת תובנות AI */
    .insight-box {
        background: white;
        border-right: 8px solid var(--orion-blue);
        padding: 25px;
        border-radius: 8px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    /* כפתורי פעולה */
    .stButton>button {
        border-radius: 8px;
        border: 2px solid var(--orion-blue);
        color: var(--orion-blue);
        background-color: white;
        font-weight: 700;
        height: 3.5em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: var(--orion-blue);
        color: white;
    }
    
    /* סידור כותרת ולוגו */
    .header-section {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 20px;
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. באנר עליון - לוגו וכותרת באותה שורה
col_header = st.container()
with col_header:
    c1, c2 = st.columns([1, 5])
    with c1:
        if os.path.exists("logo.jpg"):
            st.image("logo.jpg", width=140)
        elif os.path.exists("logo.png"):
            st.image("logo.png", width=140)
    with c2:
        st.title("מרכז התובנות של Orion")
        st.caption(f"✨ סנכרון אחרון: {datetime.now().strftime('%H:%M')} | Jira Cloud Connected")

st.markdown("---")

# 4. חלוקת העמוד
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### 📊 מדדים אסטרטגיים")
    # החזרת המבנה הנקי של 3 מדדים בשורה
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Scope Outflow", "3", "משימות חריגות")
    with m2: st.metric("Cycle Time", "5.2 ימים", "1.2+ ⚠️")
    with m3: st.metric("Risk Level", "Medium", "Stable ✅")

    # תובנת ה-AI מתחת למדדים
    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 תובנת אוריון:</strong><br>
            זיהיתי צוואר בקבוק בצוות ה-Frontend. המשימות של <b>אלון ודנה</b> מעכבות את ה-Integration. 
            מומלץ לתעדף סגירת PRs פתוחים ב-Daily הקרוב.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>### 🛠️ פעולות מהירות", unsafe_allow_html=True)
    b1, b2, b3 = st.columns(3)
    with b1: st.button("הפקת דוח סטטוס")
    with b2: st.button("ניתוח סיכונים")
    with b3: st.button("תקציר דיילי")

with col_chat:
    st.markdown("### ✨ שאל את אוריון (AI)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! אני אוריון. במה אוכל לעזור היום?"}]

    # מיכל לצ'אט
    chat_container = st.container(height=450)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("כתבי כאן..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
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
