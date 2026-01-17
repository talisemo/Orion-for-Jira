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

# 3. CSS - שחזור ויזואלי מלא + עיצוב Preview משופר ואלגנטי
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif; direction: rtl; text-align: right;
    }
    
    /* סטטוס חיבור ויישור כותרת */
    .sync-status { color: #28a745; font-size: 0.8rem; text-align: left; margin-bottom: -20px; }
    
    /* כרטיס תובנה AI כחול */
    .ai-insight-card {
        background-color: #EBF2FF; border-right: 6px solid #0052CC;
        padding: 20px; border-radius: 4px; margin: 20px 0;
        font-size: 1.1rem; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* עיצוב המדדים */
    [data-testid="stMetric"] {
        background: white; border: 1px solid #DFE1E6;
        border-radius: 10px; padding: 15px !important;
    }

    /* עיצוב ה-Preview המשופר (אלגנטי ונקי) */
    .preview-container {
        background-color: white; border: 1px solid #E1E4E8; padding: 50px;
        border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        max-width: 800px; margin: 40px auto; color: #2C3E50;
    }
    .preview-header { border-bottom: 2px solid #F4F7F9; padding-bottom: 20px; margin-bottom: 30px; }
    .preview-section { margin-bottom: 25px; }
    .personal-note-box {
        background-color: #FDFBEE; border-right: 4px solid #F1C40F;
        padding: 15px; font-style: italic; margin: 20px 0; border-radius: 4px;
    }
    .preview-bullet { margin-bottom: 10px; padding-right: 15px; position: relative; }
    </style>
    """, unsafe_allow_html=True)

# פונקציות ניווט
def navigate_to(page_name):
    st.session_state.page = page_name
    st.session_state.show_preview = False

# --- Sidebar (צ'אט וכפתורי קיצור) ---
with st.sidebar:
    st.markdown('### שאל את אוריון 🧠')
    c1, c2 = st.columns(2)
    with c1: st.button("🚨 מי תקוע?", use_container_width=True)
    with c2: st.button("⚠️ סיכון ספרינט", use_container_width=True)
    st.markdown("---")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, המערכת מסונכרנת. איך אוכל לעזור?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    st.chat_input("שאלי משהו...")

# --- עמוד 1: דאשבורד ---
if st.session_state.page == 'dashboard':
    st.markdown('<div class="sync-status">✅ Jira Cloud Connected | 15:45</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:left;">מרכז התובנות של Orion</h1>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📌 תמונת מצב אסטרטגית")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Communication Gaps", "2.4", "0.8 ↓")
    with m2: st.metric("Focus Factor", "62%", "5% ↓ ⚠️")
    with m3: st.metric("Sentiment Score", "7.2/10", "0.4 ↑")

    st.markdown("""
        <div class="ai-insight-card">
            🦉 <strong>תובנת אוריון:</strong> זיהיתי שיפור משמעותי בתקשורת סביב ה-API. 
            עם זאת, יש עומס קוגניטיבי ב-Backend שעלול לעכב את הדליברי. מומלץ לתעדף משימות קריטיות.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📈 מגמות עומק (Exclusive Trends)")
    data = pd.DataFrame(np.random.randint(5, 15, size=(10, 3)))
    st.write("**🧠 עומס קוגניטיבי**")
    st.area_chart(data[0], color="#FFADCC", height=200)
    st.write("**📢 חוסר בתקשורת**")
    st.line_chart(data[1], color="#FFAB00", height=200)
    st.write("**📅 עמידה בלו\"ז**")
    st.bar_chart(data[2], color="#5243AA", height=200)

    st.markdown("---")
    st.markdown("### ⚡ פעולות ניהוליות")
    b1, b2, b3 = st.columns(3)
    with b1: st.button("📊 הפקת דוח מותאם", on_click=lambda: navigate_to('report'), use_container_width=True)
    with b2: st.button("🔍 ניתוח סיכונים", on_click=lambda: navigate_to('risks'), use_container_width=True)
    with b3: st.button("📅 נושאים לדיילי", on_click=lambda: navigate_to('daily'), use_container_width=True)

# --- עמוד 2: בונה הדוח ---
elif st.session_state.page == 'report':
    if not st.session_state.show_preview:
        st.markdown("# 🛠️ בונה דוח תובנות")
        st.info("🦉 **ניתוח AI:** זיהיתי שיפור של 12% בעמידה בלו\"ז לעומת שבוע שעבר.")
        
        col_r1, col_r2 = st.columns([2, 1])
        with col_r1:
            st.markdown("### 1. בחרי תובנות:")
            st.checkbox("🦉 **עומס:** סיכון בצוות Backend.", value=True)
            st.checkbox("📅 **לו\"ז:** שיפור לעומת שבוע שעבר.", value=True)
            st.checkbox("📊 **גרפים:** כלול מגמות אינטראקטיביות.", value=True)
        with col_r2:
            st.markdown("### 2. יעדי הפצה:")
            st.checkbox("Slack", value=True)
            st.checkbox("Email")
            st.checkbox("Download PDF")
            
        st.session_state.personal_note = st.text_area("✍️ הערה אישית לדוח:", height=100, placeholder="הוסיפי כאן דגשים משלך...")
        
        if st.button("👁️ תצוגה מקדימה", type="primary"): 
            st.session_state.show_preview = True
            st.rerun()
        st.button("🔙 חזרה לדאשבורד", on_click=lambda: navigate_to('dashboard'))
    
    else:
        # --- תצוגת Preview מעוצבת ואלגנטית (סעיף 5) ---
        st.markdown(f"""
            <div class="preview-container">
                <div class="preview-header">
                    <h1 style="margin:0; color:#1A202C;">דוח סטטוס Orion</h1>
                    <p style="color:#718096; margin-top:5px;">תאריך הפקה: {datetime.now().strftime('%d/%m/%Y')}</p>
                </div>
                
                <div class="preview-section">
                    <h3 style="color:#2D3748; border-right: 3px solid #0052CC; padding-right:10px;">תקציר AI אסטרטגי</h3>
                    <p>ניתוח המערכת מראה מגמת שיפור יציבה בעמידה בלוחות הזמנים (12%+). מוקד תשומת הלב הניהולית נדרש בצוות ה-Backend לצמצום עומס קוגניטיבי.</p>
                </div>

                {f'<div class="personal-note-box"><strong>💬 הערת המנהלת:</strong><br>{st.session_state.personal_note}</div>' if st.session_state.personal_note else ''}

                <div class="preview-section">
                    <h3 style="color:#2D3748; border-right: 3px solid #0052CC; padding-right:10px;">תובנות נבחרות</h3>
                    <div class="preview-bullet">• סיכון עומס בצוות ה-Backend עקב ריבוי משימות במקביל.</div>
                    <div class="preview-bullet">• שיפור משמעותי בעמידה ביעדי הספרינט לעומת תקופה מקבילה.</div>
                </div>

                <div style="margin-top:40px; border:1px dashed #E2E8F0; padding:30px; text-align:center; color:#A0AEC0; border-radius:8px;">
                    <small>[כאן ישולבו הגרפים האינטראקטיביים שנבחרו]</small>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        c_send, c_edit = st.columns([1, 4])
        with c_send:
            if st.button("🚀 שלח דוח סופי"): st.success("הדוח הופץ בהצלחה!")
        with c_edit:
            if st.button("✍️ חזור לעריכה"):
                st.session_state.show_preview = False
                st.rerun()

# --- עמודים נוספים ---
elif st.session_state.page == 'risks':
    st.markdown("# 🔍 ניתוח סיכונים עמוק")
    st.info("כאן יופיע ניתוח סיכונים המבוסס על נתוני Jira.")
    st.button("🔙 חזרה", on_click=lambda: navigate_to('dashboard'))

elif st.session_state.page == 'daily':
    st.markdown("# 📅 נושאים לדיילי")
    st.success("נקודות מומלצות לשיחה עם הצוות הבוקר.")
    st.button("🔙 חזרה", on_click=lambda: navigate_to('dashboard'))
