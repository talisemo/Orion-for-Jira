import streamlit as st
import google.generativeai as genai

# הגדרות דף - Orion TPM
st.set_page_config(
    page_title="Orion - AI TPM Assistant", 
    page_icon="🦉", 
    layout="centered"
)

# עיצוב מותאם אישית בסגנון ג'ירה (Atlassian Design System)
st.markdown("""
    <style>
    /* צבעי בסיס ופונטים */
    :root {
        --jira-blue: #0052CC;
        --atlassian-gray: #F4F5F7;
    }
    
    .main {
        background-color: #FFFFFF;
        text-align: right;
        direction: rtl;
    }
    
    /* עיצוב כותרת וטקסטים */
    h1 {
        color: #172B4D;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* עיצוב תיבת הצ'אט */
    .stChatMessage {
        border-radius: 8px;
        margin-bottom: 10px;
    }
    
    /* עיצוב הסרגל הצידי */
    .stSidebar {
        background-color: #0747A6 !important;
        color: white;
    }
    
    /* כפתור ה-Submit */
    button[kind="primary"] {
        background-color: var(--jira-blue);
        border: none;
        color: white;
    }
    
    /* בועות צ'אט */
    [data-testid="stChatMessage"] {
        background-color: #F4F5F7;
        border: 1px solid #DFE1E6;
    }
    </style>
    """, unsafe_allow_html=True)

# הצגת הלוגו והכותרת במרכז
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    try:
        st.image("logo.png", width=100)
    except:
        st.write("🦉")

st.markdown("<h1 style='text-align: center;'>אוריון - עוזר ה-TPM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B778C;'>סנכרון נתונים וניתוח משימות ג'ירה בזמן אמת</p>", unsafe_allow_html=True)

# משיכת ה-API Key מה-Secrets
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    with st.sidebar:
        st.markdown("### הגדרות מערכת")
        api_key = st.text_input("הזן Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # שימוש במודל יציב ומהיר
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # ניהול היסטוריית שיחה
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # הצגת הודעות קודמות בפורמט צ'אט
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # תיבת קלט
        if prompt := st.chat_input("שאל את אוריון על הפרויקט שלך..."):
            # הוספת הודעת משתמש
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # יצירת תשובה מה-AI
            with st.chat_message("assistant", avatar="🦉"):
                with st.spinner("אוריון מנתח את הנתונים..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"אירעה שגיאה בחיבור למנוע ה-AI: {e}")
else:
    st.warning("המערכת ממתינה להגדרת מפתח API כדי להתחיל לפעול.")
