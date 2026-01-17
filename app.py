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

# 2. ניהול מצב העמוד (Dashboard או Report Builder)
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'

# 3. CSS מקצועי - יישור ימין, RTL ומניעת מריחה
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }

    .main .block-container {
        max-width: 1100px;
        padding: 2rem;
        margin: 0 auto;
    }

    .sync-text {
        color: #28a745;
        font-size: 0.8rem;
        display: block;
        margin-top: -5px;
    }

    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
    }

    .insight-card {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 15px;
        border-radius: 4px;
        margin: 20px 0;
    }
    
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
    </style>
    """, unsafe_allow_html=True)

# פונקציות ניווט
def go_to_report(): st.session_state.page = 'report'
def go_to_dashboard(): st.session_state.page = 'dashboard'

# --- Sidebar (צ'אט) ---
with st.sidebar:
    st.markdown('<div style="font-weight:600; font-size:1.1rem; margin-bottom:10px;"><span class="orion-icon"></span>שאל את אוריון</div>', unsafe_allow_html=True)
    st.caption("תובנות מהירות:")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚨 מי תקוע?"): prompt_input = "מי צווארי בקבוק?"
    with c2:
        if st.button("⚠️ סיכון ספרינט"): prompt_input = "משימות באיחור?"

    st.markdown("---")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, מוכנה לעבור על התובנות?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    st.chat_input("שאלי משהו...")

# --- עמוד 1: דאשבורד ראשי ---
if st.session_state.page == 'dashboard':
    st.markdown(f"""
        <div style="text-align: right;">
            <h1 style='margin:0;'>מרכז התובנות של Orion</h1>
            <span class="sync-text">✅ Jira Cloud Connected | {datetime.now().strftime("%H:%M")}</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # מדדים
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable")
    with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
    with m3: st.metric("Communication Gaps", "2.4", "-0.8")

    st.markdown("""
        <div class="insight-card">
            <strong>🦉 תובנת אוריון:</strong> זוהה עומס קוגניטיבי ב-Backend. מומלץ לאחד משימות ל-Epic אחד כדי לשפר את הפוקוס.
        </div>
    """, unsafe_allow_html=True)

    # גרפים (הוספת המדד השלישי)
    st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
    g1, g2, g3 = st.columns(3)
    data = pd.DataFrame(np.random.randint(5, 15, size=(10, 3)), columns=['A', 'B', 'C'])
    
    with g1:
        st.write("**🧠 עומס קוגניטיבי**")
        st.area_chart(data['A'], color="#FFADCC", height=150)
    with g2:
        st.write("**📢 חוסר בתקשורת**")
        st.line_chart(data['B'], color="#FFAB00", height=150)
    with g3:
        st.write("**📅 עמידה בלו\"ז**")
        st.bar_chart(data['C'], color="#5243AA", height=150)

    st.markdown("---")
    # כפתורי פעולה
    b1, b2, b3 = st.columns(3)
    with b1: st.button("📊 הפקת דוח מותאם", on_click=go_to_report)
    with b2: st.button("🔍 ניתוח סיכונים")
    with b3: st.button("📅 נושאים לדיילי")

# --- עמוד 2: עמוד הפקת דוח (נפרד) ---
elif st.session_state.page == 'report':
    st.markdown("# 🛠️ בונה דוח תובנות")
    st.write("בחרי אילו תובנות לכלול בדוח הסופי:")
    
    st.markdown("---")
    
    # רשימת בחירה
    with st.container():
        st.checkbox("🦉 **תובנת עומס:** סיכון בצוות Backend עקב ריבוי משימות.", value=True)
        st.checkbox("📢 **תובנת תקשורת:** פערים בתיעוד API בין הצוותים.")
        st.checkbox("📅 **תובנת לו\"ז:** עיכוב פוטנציאלי של 3 ימים במשימות האינטגרציה.")
        st.checkbox("📊 **ויזואליזציה:** כלול את גרפי המגמות של השבוע האחרון.", value=True)

    st.markdown("---")
    
    # כפתורי סיום
    col_fin, col_back = st.columns([1, 4])
    with col_fin:
        if st.button("🚀 הפץ דוח", type="primary"):
            st.success("הדוח נשלח בהצלחה לצוות!")
    with col_back:
        st.button("✖️ ביטול וחזרה לדאשבורד", on_click=go_to_dashboard)
