import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף
st.set_page_config(page_title="Orion Executive Insights", page_icon="logo.png", layout="wide")

# 2. ניהול מצבי עמוד
if 'page' not in st.session_state: st.session_state.page = 'dashboard'
if 'show_preview' not in st.session_state: st.session_state.show_preview = False
if 'personal_note' not in st.session_state: st.session_state.personal_note = ""

# 3. CSS מקצועי - יישור ימין ו-RTL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif; direction: rtl; text-align: right;
    }
    .main .block-container { max-width: 1100px; padding: 2rem; margin: 0 auto; }
    .preview-paper {
        background-color: white; border: 1px solid #ddd; padding: 30px;
        border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #333; margin: 20px 0; text-align: right;
    }
    .personal-note-box {
        background-color: #FFF9C4; padding: 10px; border-right: 4px solid #FBC02D;
        margin-top: 15px; font-style: italic;
    }
    .trend-analysis-box {
        background-color: #F4F5F7; border-radius: 8px; padding: 15px; border: 1px solid #DFE1E6;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציות ניווט
def go_to_report(): st.session_state.page = 'report'; st.session_state.show_preview = False
def go_to_dashboard(): st.session_state.page = 'dashboard'

# --- Sidebar (צ'אט) ---
with st.sidebar:
    st.markdown('<div>🧠 שאל את אוריון</div>', unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "טלי, אני מוכנה לנתח את מגמות העומק עבורך."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    st.chat_input("שאלי משהו...")

# --- עמוד 1: דאשבורד עם גרפים אינטראקטיביים ---
if st.session_state.page == 'dashboard':
    st.markdown(f"<h1>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # מדדים עליונים
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable")
    with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
    with m3: st.metric("Communication Gaps", "2.4", "-0.8")
    
    st.markdown("### 📈 מגמות עומק (Interactive)")
    g1, g2, g3 = st.columns(3)
    
    # יצירת נתונים לגרפים אינטראקטיביים
    chart_data = pd.DataFrame({
        'day': range(1, 11),
        'Switching': np.random.randint(5, 15, 10),
        'Gaps': np.random.randint(1, 5, 10),
        'Variance': np.random.randint(0, 10, 10)
    })

    with g1:
        st.write("**🧠 עומס קוגניטיבי**")
        st.area_chart(chart_data, x='day', y='Switching', color="#FFADCC")
    with g2:
        st.write("**📢 חוסר בתקשורת**")
        st.line_chart(chart_data, x='day', y='Gaps', color="#FFAB00")
    with g3:
        st.write("**📅 עמידה בלו\"ז**")
        st.bar_chart(chart_data, x='day', y='Variance', color="#5243AA")
    
    st.markdown("---")
    st.button("📊 הפקת דוח מותאם", on_click=go_to_report)

# --- עמוד 2: בונה הדוח ---
elif st.session_state.page == 'report':
    if not st.session_state.show_preview:
        st.markdown("# 🛠️ בונה דוח אסטרטגי")
        
        # אזור ניתוח המגמות (ההשוואה ההיסטורית)
        st.markdown("### 🧠 ניתוח מגמות Orion (למה להפיץ?)")
        st.markdown("""
            <div class="trend-analysis-box">
                <p>📈 <strong>עמידה בלו"ז:</strong> שיפור של 12% לעומת ספרינט קודם. מומלץ לציין כנקודת חוזק.</p>
                <p>📉 <strong>פוקוס:</strong> ירידה קלה של 5% - ייתכן בגלל עומס ישיבות.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        col_checks, col_dest = st.columns([2, 1])
        with col_checks:
            st.markdown("### 1. בחרי תובנות:")
            st.checkbox("🦉 תובנת עומס: סיכון בצוות Backend.", value=True)
            st.checkbox("📢 תובנת תקשורת: פערים בתיעוד API.", value=True)
            st.checkbox("📅 תובנת לו\"ז: שיפור לעומת שבוע שעבר.", value=True)
        
        with col_dest:
            st.markdown("### 2. יעדי הפצה:")
            st.checkbox("Slack (PDF)", value=True)
            st.checkbox("Email (PDF)")
            st.checkbox("Download PDF")
            
        st.session_state.personal_note = st.text_area("✍️ הוסף הערה אישית לדוח:", height=100)

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
                {f'<div class="personal-note-box"><strong>💬 הערת המנהלת:</strong><br>{st.session_state.personal_note}</div>' if st.session_state.personal_note else ''}
                <hr>
                <h4>תובנות נבחרות:</h4>
                <ul><li>שיפור של 12% בעמידה בלוחות זמנים.</li><li>סיכון עומס בצוות ה-Backend.</li></ul>
            </div>
        """, unsafe_allow_html=True)
        
        c_send, c_edit = st.columns([1, 4])
        with c_send:
            if st.button("🚀 אישור ושליחה סופית"): st.success("הדוח נשלח לכל היעדים!")
        with c_edit:
            if st.button("✍️ חזור לעריכה"):
                st.session_state.show_preview = False
                st.rerun()
