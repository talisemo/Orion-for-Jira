import streamlit as st
import google.generativeai as genai
import pandas as pd

# הגדרות דף
st.set_page_config(page_title="Orion - TPM Insights", page_icon="🦉", layout="wide")

# CSS מתקדם ליישור ועיצוב
st.markdown("""
    <style>
    /* הגדרת כיוון כתיבה כללי */
    .main, .stApp { direction: rtl; text-align: right; }
    
    /* יישור כותרות ומדדים */
    h1, h2, h3, [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
        text-align: right !important;
        direction: rtl !important;
    }

    /* עיצוב כרטיסי המדדים */
    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
        box-shadow: 0 4px 6px rgba(9, 30, 66, 0.08);
    }

    /* עיצוב אזור ה-Insight */
    .insight-box {
        background-color: #EBF2FF;
        border-right: 5px solid #0052CC;
        padding: 20px;
        border-radius: 4px;
        color: #172B4D;
        margin-bottom: 20px;
    }

    /* התאמת תיבת הקלט של הצ'אט */
    .stChatInputContainer { direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# כותרת עליונה עם לוגו קטן
col_header1, col_header2 = st.columns([0.1, 0.9])
with col_header1:
    try:
        st.image("logo.png", width=60)
    except:
        st.write("🦉")
with col_header2:
    st.title("Orion Insights - עוזר ה-TPM החכם")

st.markdown("---")

# חלוקה ראשית
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### 🎯 תובנות ניהוליות (ספרינט נוכחי)")
    
    # שורת מדדים
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Scope Outflow", "3", "משימות שיצאו", delta_color="normal")
    with m2:
        st.metric("Cycle Time", "5.2 ימים", "+1.2", delta_color="inverse")
    with m3:
        st.metric("Risk Level", "Medium", "Trending Up", delta_color="inverse")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # אזור תובנה מיוחדת של אוריון
    st.markdown("""
        <div class="insight-box">
            <strong>🦉 התובנה של אוריון:</strong><br>
            זיהיתי חוסר איזון בעומסים. <b>דנה</b> נמצאת בקיבולת שיא (120%), מה שמעלה את הסיכון ל-Cycle Time של משימות ה-Review. 
            מומלץ לשקול ניוד משימות ל<b>רוני</b>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚠️ עומס צוות (Heatmap)")
    load_data = pd.DataFrame({
        'איש צוות': ['יוסי', 'דנה', 'רוני', 'אלון'],
        'עומס (%)': [85, 120, 45, 90]
    })
    st.bar_chart(load_data.set_index('איש צוות'), color='#0052CC')

with col_chat:
    st.markdown("### 🦉 התייעצות")
    
    # אתחול צ'אט
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! אני אוריון. אני עוקב אחרי השינויים בספרינט. רוצה לדעת למה המדדים השתנו היום?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("שאל את אוריון..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            with st.chat_message("assistant", avatar="🦉"):
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
