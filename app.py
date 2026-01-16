import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os

# 1. הגדרות דף - האייקון השקוף לטאב
st.set_page_config(
    page_title="Orion | Smart Executive Insights",
    page_icon="icon.png", 
    layout="wide"
)

# 2. עיצוב CSS מתקדם - מחזיר את המראה המקצועי
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');
    
    html, body, [data-testid="ststMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .stApp { background-color: #F4F5F7; }

    /* עיצוב כרטיסי המדדים */
    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #DFE1E6;
        border-top: 5px solid #0065FF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    /* תיבת תובנות AI */
    .insight-box {
        background: linear-gradient(90deg, #DEEBFF 0%, #FFFFFF 100%);
        border-right: 8px solid #0065FF;
        padding: 25px;
        border-radius: 8px;
        margin: 20px 0;
        color: #172B4D;
        font-size: 1.2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* עיצוב כפתורים */
    .stButton>button {
        border-radius: 25px;
        border: 2px solid #0065FF;
        color: #0065FF;
        background-color: white;
        font-weight: bold;
        transition: all 0.3s;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #0065FF;
        color: white;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. באנר עליון - לוגו וכותרת
col_logo, col_title = st.columns([1, 5])

with col_logo:
    # ניסיון טעינת לוגו חכם
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=150)
    elif os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    else:
        st.markdown("## 🌌 Orion")

with col_title:
    st.title("מרכז התובנות של Orion")
    st.caption(f"✨ סנכרון אחרון: {datetime.now().strftime('%H:%M')} | Jira Cloud Connected")

st.markdown("---")

# 4. חלוקת העמוד
col_data, col_chat = st.columns([1.8, 1])

with col_data:
    st.markdown("### 📊 מדדים אסטרטגיים")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Scope Outflow", "3", "משימות חריגות")
    with m2: st.metric("Cycle Time", "5.2 ימים", "1.2+ ⚠️")
    with m3: st.metric("Risk Level", "Medium", "Stable ✅")

    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 תובנת אוריון:</strong><br>
            זיהיתי צוואר בקבוק בצוות ה-Frontend. המשימות של <b>אלון ודנה</b> מעכבות את ה-Integration. 
            מומלץ לתת עדיפות ב-Daily הקרוב לסגירת ה-PRs הפתוחים.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ פעולות מהירות")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📝 הפקת דוח סטטוס"):
            st.info("מכין דוח PDF מפורט...")
    with c2: 
        if st.button("🔍 ניתוח סיכונים"):
            st.warning("סורק חריגות בלוחות הזמנים...")
    with c3: 
        if st.button("📅 תקציר דיילי"):
            st.success("התקציר מוכן להצגה!")

with col_chat:
    st.markdown("### 🦉 שאל את אוריון")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! אני אוריון. אני מחוברת לג'ירה שלך. מה תרצי שאבדוק עבורך?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("למשל: מי הצוות הכי עמוס השבוע?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # חיבור לבינה מלאכותית
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
                st.error("חיבור ה-AI נכשל. בדקי את ה-API Key.")
        else:
            st.info("אנא הגדירי API Key כדי להפעיל את אוריון.")
