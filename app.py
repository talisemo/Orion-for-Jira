import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף - שחזור הטאב והלוגו
st.set_page_config(
    page_title="Orion Executive Insights",
    page_icon="logo.png", 
    layout="wide"
)

# 2. ניהול מצבי עמוד (מניעת קריסה במעברים)
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'show_preview' not in st.session_state:
    st.session_state.show_preview = False

# 3. CSS מלא ומשוחזר - RTL, צבעים ויישור ימין קשיח
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

    /* כרטיסי המדדים */
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #DFE1E6;
        border-radius: 8px;
        padding: 15px !important;
    }

    /* תיבת תובנה AI */
    .insight-card {
        background-color: #DEEBFF;
        border-right: 5px solid #0052CC;
        padding: 15px;
        border-radius: 4px;
        margin: 20px 0;
    }

    /* דף ה-Preview המעוצב */
    .preview-paper {
        background-color: white;
        border: 1px solid #ddd;
        padding: 30px;
        border-radius: 4px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #333;
        margin: 20px 0;
        text-align: right;
    }
    
    .orion-icon {
        width: 24px; height: 24px;
        background-image: url('https://img.icons8.com/fluency/48/brain.png');
        background-size: contain; background-repeat: no-repeat;
        display: inline-block; vertical-align: middle; margin-left: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציות ניווט בטוחות
def go_to_report(): st.session_state.page = 'report'; st.session_state.show_preview = False
def go_to_dashboard(): st.session_state.page = 'dashboard'

# --- Sidebar (צ'אט משוחזר עם כל הכפתורים) ---
with st.sidebar:
    st.markdown('<div style="font-weight:600; font-size:1.1rem; margin-bottom:10px;"><span class="orion-icon"></span>שאל את אוריון</div>', unsafe_allow_html=True)
    st.caption("תובנות מהירות:")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚨 מי תקוע?"): q = "מי צווארי בקבוק?"
    with c2:
        if st.button("⚠️ סיכון ספרינט"): q = "משימות באיחור?"

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

    # 1. תמונת מצב אסטרטגית
    st.markdown("### 📌 תמונת מצב")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable")
    with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
    with m3: st.metric("Communication Gaps", "2.4", "-0.8")

    st.markdown('<div class="insight-card"><strong>🦉 תובנת אוריון:</strong> זוהה עומס קוגניטיבי ב-Backend. מומלץ לאחד משימות ל-Epic אחד כדי לשפר את הפוקוס.</div>', unsafe_allow_html=True)

    # 2. גרפים (שחזור 3 הגרפים המלאים)
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
    # 3. פעולות ניהוליות
    b1, b2, b3 = st.columns(3)
    with b1: st.button("📊 הפקת דוח מותאם", on_click=go_to_report)
    with b2: st.button("🔍 ניתוח סיכונים")
    with b3: st.button("📅 נושאים לדיילי")

# --- עמוד 2: בונה הדוח וה-Preview ---
elif st.session_state.page == 'report':
    st.markdown("# 🛠️ בונה דוח תובנות")
    
    if not st.session_state.show_preview:
        st.info("🦉 **ניתוח AI:** זיהיתי שיפור של 12% בעמידה בלו\"ז לעומת שבוע שעבר. כדאי לכלול זאת בדוח.")
        
        col_checks, col_opts = st.columns([2, 1])
        with col_checks:
            st.markdown("### בחרי תובנות:")
            st.checkbox("🦉 תובנת עומס: סיכון בצוות Backend.", value=True)
            st.checkbox("📢 תובנת תקשורת: פערים בתיעוד API.", value=True)
            st.checkbox("📅 תובנת לו\"ז: עיכוב של 3 ימים באינטגרציה.", value=True)
            st.checkbox("📊 גרפים: כלול את מגמות המדדים השבועיות.", value=True)
        
        with col_opts:
            st.markdown("### יעד הפצה:")
            st.radio("לאן לשלוח?", ["Slack (PDF)", "Email (PDF)", "Download Only"])
            st.text_area("הערה אישית לדוח:", height=100)

        st.markdown("---")
        if st.button("👁️ הצג תצוגה מקדימה", type="primary"): 
            st.session_state.show_preview = True
            st.rerun()
        st.button("✖️ ביטול וחזרה", on_click=go_to_dashboard)

    else:
        # תצוגת Preview
        st.markdown("### 📄 תצוגה מקדימה של הדוח")
        st.markdown(f"""
            <div class="preview-paper">
                <div style="border-bottom: 2px solid #eee; padding-bottom:10px; margin-bottom:20px;">
                    <h2 style="margin:0;">דוח סטטוס Orion</h2>
                    <span>תאריך: {datetime.now().strftime("%d/%m/%Y")}</span>
                </div>
                <h4>תקציר AI:</h4>
                <p>מגמת שיפור של 12% בעמידה בזמנים. דגש על צמצום עומס קוגניטיבי בצוות Backend.</p>
                <hr>
                <h4>תובנות שנבחרו:</h4>
                <ul><li>סיכון עומס ב-Backend</li><li>עיכוב פוטנציאלי באינטגרציה</li></ul>
                <div style="background:#f9f9f9; height:80px; border:1px dashed #ccc; text-align:center; padding-top:25px; color:#999;">
                    [צילומי הגרפים יצורפו כאן]
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        c_send, c_edit = st.columns([1, 4])
        with c_send:
            if st.button("🚀 אישור ושליחה"):
                st.success("הדוח נשלח בהצלחה!")
        with c_edit:
            if st.button("✍️ חזור לעריכה"):
                st.session_state.show_preview = False
                st.rerun()
