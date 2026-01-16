import streamlit as st
import google.generativeai as genai

# הגדרות דף
st.set_page_config(page_title="Orion - AI TPM Assistant", page_icon="🦉", layout="centered")

# הצגת הלוגו (בהנחה שהעלית אותו בשם logo.png)
try:
    st.image("logo.png", width=150)
except:
    st.title("🦉 Orion")

st.title("ברוכים הבאים לאוריון")
st.subheader("עוזר ה-TPM האישי שלך לניתוח משימות ג'ירה")

st.markdown("""
---
### מה אוריון יודע לעשות?
* **ניתוח דאטה:** סריקת משימות ג'ירה וזיהוי צווארי בקבוק.
* **סיכום שבועי:** יצירת דוחות סטטוס אוטומטיים.
* **חיזוי סיכונים:** התראה על משימות שעלולות להתעכב.
---
""")

# הגדרת API Key בצורה מאובטחת
with st.sidebar:
    st.header("הגדרות")
    api_key = st.text_input("הזן את ה-Gemini API Key שלך:", type="password")
    if api_key:
        genai.configure(api_key=api_key)
        st.success("ה-API Key הוגדר בהצלחה!")

# ממשק צ'אט בסיסי למשתמש
if api_key:
    user_input = st.text_input("איך אוריון יכול לעזור לך היום?")
    if user_input:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_input)
        st.write("### תשובת אוריון:")
        st.write(response.text)
else:
    st.info("אנא הזן API Key בסרגל הצד כדי להתחיל לעבוד עם אוריון.")
