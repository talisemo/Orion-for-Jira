import streamlit as st
import google.generativeai as genai
import pandas as pd

st.set_page_config(page_title="Orion - TPM Insights", page_icon="🦉", layout="wide")

# עיצוב בסגנון ג'ירה עם דגש על Insights
st.markdown("""
    <style>
    .main, .stApp { direction: rtl; text-align: right; }
    .insight-card {
        background-color: #EBF2FF;
        border-right: 5px solid #0052CC;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .metric-container { background-color: white; border: 1px solid #DFE1E6; padding: 20px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# כותרת
st.title("Orion Insights - מעבר לדשבורד הרגיל")
st.markdown("---")

col_data, col_chat = st.columns([2, 1])

with col_data:
    st.subheader("🎯 תובנות ניהוליות (מעבר לג'ירה הסטנדרטית)")
    
    # מדדים חכמים
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Scope Outflow (הוצאו)", "3", "משימות", delta_color="normal")
        st.caption("משימות שיצאו מהספרינט הנוכחי")
    with m2:
        st.metric("Cycle Time", "5.2 ימים", "+1.2", delta_color="inverse")
        st.caption("זמן ממוצע לביצוע משימה (מגמת האטה)")
    with m3:
        st.metric("Risk Level", "Medium", "Trending Up", delta_color="inverse")
        st.caption("מדד סיכון משוקלל לספרינט")

    st.markdown("### ⚠️ זיהוי צווארי בקבוק (Heatmap)")
    # נתוני דמה של עומס אמיתי
    load_data = pd.DataFrame({
        'איש צוות': ['יוסי', 'דנה', 'רוני', 'אלון'],
        'עומס נוכחי (%)': [85, 120, 45, 90]
    })
    st.bar_chart(load_data.set_index('איש צוות'), color='#0052CC')
    st.warning("דנה נמצאת ב-Overload. מומלץ לבדוק העברת משימות לרוני.")

with col_chat:
    st.subheader("🦉 שאל את אוריון")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! זיהיתי ש-3 משימות יצאו מהספרינט אתמול. רוצה לדעת מי הוציא אותן ואיך זה משפיע על תאריך היעד?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("למשל: 'מי הכי עמוס בצוות?'"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # חיבור ל-AI
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            with st.chat_message("assistant", avatar="🦉"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
