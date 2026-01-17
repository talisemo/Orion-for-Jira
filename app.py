import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף בסיסיות
st.set_page_config(page_title="Orion Executive Insights", page_icon="logo.png", layout="wide")

# 2. ניהול מצב העמוד (Dashboard או Report Builder)
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'

# 3. CSS מקצועי - כולל עיצוב למצב עריכת דוח
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl; text-align: right;
    }
    .main .block-container { max-width: 1100px; padding: 2rem; margin: 0 auto; }
    .sync-text { color: #28a745; font-size: 0.8rem; display: block; margin-top: -5px; }
    
    /* עיצוב רשימת בחירה בדוח */
    .report-item {
        background-color: #f9f9f9;
        border: 1px solid #eee;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציות מעבר בין דפים
def go_to_report(): st.session_state.page = 'report'
def go_to_dashboard(): st.session_state.page = 'dashboard'

# --- תצוגת ה-Sidebar (משותפת לכל העמודים) ---
with st.sidebar:
    st.markdown('<div><span class="orion-icon"></span> שאל את אוריון</div>', unsafe_allow_html=True)
    if st.button("🚨 מי תקוע?"): query = "צווארי בקבוק"
    if st.button("📅 סיכון ספרינט"): query = "משימות באיחור"
    
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

    # מדדים עליונים
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable")
    with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
    with m3: st.metric("Communication Gaps", "2.4", "-0.8")

    st.markdown('<div class="insight-card" style="background:#DEEBFF; padding:15px; border-right:5px solid #0052CC; margin:20px 0;">'
                '<strong>🦉 תובנת אוריון:</strong> זוהה עומס קוגניטיבי ב-Backend עקב ריבוי משימות קטנות. '
                'מומלץ לאחדן ל-Epic אחד.</div>', unsafe_allow_html=True)

    # גרפים (כולל המדד השלישי החדש)
    st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
    g1, g2, g3 = st.columns(3)
    data = pd.DataFrame(np.random.randint(5, 15, size=(12, 3)), columns=['A', 'B', 'C'])
    
    with g1:
        st.write("**🧠 עומס קוגניטיבי**")
        st.area_chart(data['A'], color="#FFADCC", height=150)
    with g2:
        st.write("**📢 חוסר בתקשורת**")
        st.line_chart(data['B'], color="#FFAB00", height=150)
    with g3:
        st.write("**📅 עמידה בלו"ז**")
        st.bar_chart(data['C'], color="#5243AA", height=150)

    st.markdown("---")
    # כפתורי פעולה - הפקת דוח עכשיו מובילה לעמוד החדש
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📊 הפקת דוח מותאם", on_click=go_to_report)
    with c2: st.button("🔍 ניתוח סיכונים")
    with c3: st.button("📅 נושאים לדיילי")

# --- עמוד 2: בונה הדוח (העמוד הנפרד) ---
elif st.session_state.page == 'report':
    st.markdown("# 🛠️ בונה דוח תובנות")
    st.write("בחרי את התובנות שברצונך לכלול בדוח המופץ:")
    
    st.markdown("---")
    
    # רשימת תובנות לבחירה
    ins1 = st.checkbox("🦉 **תובנת עומס:** סיכון בצוות Backend עקב Context Switching גבוה.", value=True)
    ins2 = st.checkbox("📢 **תובנת תקשורת:** פערים בתיעוד API בין הצוותים.")
    ins3 = st.checkbox("📅 **תובנת לו\"ז:** עיכוב פוטנציאלי של 3 ימים במשימות ה-Integration.")
    ins4 = st.checkbox("📊 **גרפים:** כלול את צילומי המגמות השבועיות.")

    st.markdown("---")
    
    # כפתורי סיום/חזרה
    col_save, col_cancel = st.columns([1, 4])
    with col_save:
        if st.button("🚀 הפץ דוח", type="primary"):
            st.success("הדוח נשלח בהצלחה ל-Slack ולמייל!")
            # כאן אפשר להוסיף לוגיקה של שליחה
    with col_cancel:
        st.button("✖️ ביטול וחזרה", on_click=go_to_dashboard)
