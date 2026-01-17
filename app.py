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

# 3. CSS יציב - ללא שינויי מבנה, רק עיצוב רכיבים
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif; direction: rtl; text-align: right;
    }
    .sync-status { color: #28a745; font-size: 0.85rem; text-align: left; margin-bottom: -15px; }
    
    /* כרטיס תובנה AI כחול מקורי */
    .ai-insight-card {
        background-color: #EBF2FF; border-right: 6px solid #0052CC;
        padding: 15px; border-radius: 4px; margin: 20px 0; font-size: 1.1rem;
    }

    /* עיצוב דף דוח (Preview) אלגנטי */
    .report-paper {
        background: white; border: 1px solid #E2E8F0; padding: 40px;
        border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        max-width: 800px; margin: auto; color: #2D3748;
    }
    .report-header { border-bottom: 2px solid #EDF2F7; padding-bottom: 20px; margin-bottom: 25px; }
    .personal-note-display { 
        background-color: #FFFBEB; border-right: 4px solid #F6E05E;
        padding: 15px; margin: 20px 0; font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

def navigate_to(page):
    st.session_state.page = page
    st.session_state.show_preview = False

# --- Sidebar ---
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

# --- עמוד 1: דאשבורד (שחזור מלא לפי התמונות) ---
if st.session_state.page == 'dashboard':
    st.markdown('<div class="sync-status">✅ Jira Cloud Connected | 15:45</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:left;">מרכז התובנות של Orion</h1>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📌 תמונת מצב")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable ✅")
    with m2: st.metric("Focus Factor", "62%", "5% ↓ ⚠️")
    with m3: st.metric("Sentiment Score", "7.2/10", "0.4 ↑")

    st.markdown("""<div class="ai-insight-card">🦉 <strong>תובנת אוריון:</strong> זוהה עומס קוגניטיבי גבוה בצוות ה-Backend. מומלץ לרכז משימות קטנות ל-Epic אחד כדי לשמור על רצף עבודה.</div>""", unsafe_allow_html=True)

    # גרפים רחבים (סעיף 3 שלך)
    st.markdown("### 📈 מגמות עומק (Exclusive Trends) 📈")
    g1, g2, g3 = st.columns(3)
    data = pd.DataFrame(np.random.randint(5, 15, size=(10, 3)))
    with g1:
        st.write("**🧠 עומס קוגניטיבי**")
        st.area_chart(data[0], color="#FFADCC")
    with g2:
        st.write("**📢 חוסר בתקשורת**")
        st.line_chart(data[1], color="#FFAB00")
    with g3:
        st.write("**📅 עמידה בלו\"ז**")
        st.bar_chart(data[2], color="#5243AA")

    st.markdown("---")
    st.markdown("### ⚡ פעולות ניהוליות")
    b1, b2, b3 = st.columns(3)
    with b1: st.button("📊 הפקת דוח מותאם", on_click=lambda: navigate_to('report'), use_container_width=True)
    with b2: st.button("🔍 ניתוח סיכונים", use_container_width=True)
    with b3: st.button("📅 נושאים לדיילי", use_container_width=True)

# --- עמוד 2: בונה דוח ו-Preview ---
elif st.session_state.page == 'report':
    if not st.session_state.show_preview:
        st.markdown("# 🛠️ בונה דוח תובנות ⚒️")
        st.info("🦉 **ניתוח AI:** זיהיתי שיפור של 12% בעמידה בלו\"ז לעומת שבוע שעבר.")
        
        c_r1, c_r2 = st.columns([2, 1])
        with c_r1:
            st.markdown("### בחרי תובנות:")
            st.checkbox("🦉 **עומס:** סיכון בצוות Backend.", value=True)
            st.checkbox("📅 **לו\"ז:** שיפור לעומת שבוע שעבר.", value=True)
            st.checkbox("📊 **גרפים:** כלול מגמות אינטראקטיביות.", value=True)
        with c_r2:
            st.markdown("### יעדי הפצה:")
            st.checkbox("Slack", value=True)
            st.checkbox("Email")
            
        st.session_state.personal_note = st.text_area("✍️ הערה אישית לדוח:", height=100)
        
        if st.button("👁️ תצוגה מקדימה", type="primary"): 
            st.session_state.show_preview = True
            st.rerun()
        st.button("🔙 ביטול", on_click=lambda: navigate_to('dashboard'))
    
    else:
        # תצוגת דוח אלגנטית נקייה (מתוקנת!)
        st.markdown('<div class="report-paper">', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="report-header">
                <h1 style="margin:0;">דוח סטטוס Orion</h1>
                <p style="color:#718096;">תאריך: {datetime.now().strftime('%d/%m/%Y')}</p>
            </div>
            <h3>תקציר AI אסטרטגי:</h3>
            <p>מגמת שיפור של 12% בעמידה בזמנים. דגש על צמצום עומס קוגניטיבי בצוות Backend.</p>
        """, unsafe_allow_html=True)
        
        if st.session_state.personal_note:
            st.markdown(f'<div class="personal-note-display"><strong>💬 הערת המנהלת:</strong><br>{st.session_state.personal_note}</div>', unsafe_allow_html=True)
            
        st.markdown("""
            <h3>תובנות נבחרות:</h3>
            <ul>
                <li>סיכון עומס בצוות ה-Backend עקב ריבוי משימות.</li>
                <li>שיפור משמעותי בעמידה בלוחות זמנים לעומת ספרינט קודם.</li>
            </ul>
            <br>
            <div style="border: 1px dashed #CBD5E0; padding:20px; text-align:center; color:#A0AEC0; border-radius:4px;">
                [צילומי הגרפים האינטראקטיביים יצורפו כאן]
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        c_send, c_edit = st.columns([1, 4])
        with c_send:
            if st.button("🚀 שלח עכשיו"): st.success("הדוח נשלח!")
        with c_edit:
            st.button("✍️ ערוך שוב", on_click=lambda: setattr(st.session_state, 'show_preview', False))
