import streamlit as st
import google.generativeai as genai
import pandas as pd

# הגדרות דף
st.set_page_config(page_title="Orion - TPM Insights", page_icon="🦉", layout="wide")

# CSS עם גווני הכחול הרך ויישור RTL
st.markdown("""
    <style>
    /* צבעים רכים של Atlassian */
    :root {
        --soft-blue: #4C9AFF;
        --light-blue: #DEEBFF;
        --text-dark: #172B4D;
        --jira-gray: #F4F5F7;
    }

    .stApp { direction: rtl; text-align: right; background-color: var(--jira-gray); }
    
    /* יישור כללי */
    h1, h2, h3, p, span, div, [data-testid="stMarkdownContainer"] {
        text-align: right !important;
        direction: rtl !important;
    }

    /* כרטיסי מדדים מעוצבים בכחול רך */
    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #DFE1E6;
        border-top: 4px solid var(--soft-blue);
        border-radius: 8px;
        padding: 15px !important;
        box-shadow: 0 2px 4px rgba(9, 30, 66, 0.08);
    }

    /* תיבת התובנה - רקע כחול בהיר מאוד */
    .insight-box {
        background-color: var(--light-blue);
        border-right: 6px solid var(--soft-blue);
        padding: 20px;
        border-radius: 4px;
        color: var(--text-dark);
        margin-bottom: 25px;
        line-height: 1.6;
    }

    /* עיצוב כפתורי פעולה */
    .stButton>button {
        background-color: white;
        color: var(--soft-blue);
        border: 1px solid var(--soft-blue);
        border-radius: 20px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: var(--soft-blue);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# כותרת
col_header1, col_header2 = st.columns([0.1, 0.9])
with col_header1:
    try: st.image("logo.png", width=65)
    except: st.write("🦉")
with col_header2:
    st.title("מרכז התובנות של אוריון")

st.markdown("---")

# חלוקה ראשית
col_data, col_chat = st.columns([2, 1])

with col_data:
    st.markdown("### 🎯 מדדי ביצועים חכמים")
    
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Scope Outflow", "3", "משימות")
    with m2: st.metric("Cycle Time", "5.2 ימים", "+1.2")
    with m3: st.metric("Risk Level", "Medium", "יציב")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # תיבת תובנה מיושרת
    st.markdown(f"""
        <div class="insight-box">
            <strong>🦉 ניתוח אוריון ליום זה:</strong><br>
            זיהיתי שקצב סגירת המשימות ב-Frontend הואט ב-15% ביומיים האחרונים. 
            <b>אלון</b> ו<b>דנה</b> עובדים על משימה משותפת בסיכון גבוה. 
            כדאי לבדוק בדיילי אם יש חוסם (Blocker) טכני שלא דווח.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🛠️ פעולות מהירות ל-TPM")
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝 הפק דוח סטטוס")
    with c2: st.button("🔍 נתח סיכוני ספרינט")
    with c3: st.button("⏰ תקצר פגישת דיילי")

    st.markdown("<br>### ⚠️ עומס צוות (Heatmap)")
    load_data = pd.DataFrame({
        'איש צוות': ['יוסי', 'דנה', 'רוני', 'אלון'],
        'עומס (%)': [85, 110, 50, 95]
    })
    st.bar_chart(load_data.set_index('איש צוות'), color='#4C9AFF')

with col_chat:
    st.markdown("### 🦉 התייעצות עם אוריון")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי! אני אוריון. אני סורק את הג'ירה ברקע. יש משהו ספציפי שתרצי שאבדוק?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("למשל: 'מי הצוואר בקבוק כרגע?'"):
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
