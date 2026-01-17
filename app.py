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

# 3. CSS יציב (RTL, עיצוב כרטיסים וטבלת דיילי)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif; direction: rtl; text-align: right;
    }
    .sync-status { color: #28a745; font-size: 0.85rem; margin-top: -10px; margin-bottom: 20px; }
    
    .ai-insight-card {
        background-color: #EBF2FF; border-right: 6px solid #0052CC;
        padding: 15px; border-radius: 4px; margin: 20px 0; font-size: 1.1rem;
    }
    
    /* עיצוב דף דוח (Preview) */
    .report-paper {
        background: white; border: 1px solid #E2E8F0; padding: 40px;
        border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        max-width: 850px; margin: auto; color: #2D3748;
    }

    /* עיצוב טבלת מפתחים (Daily) */
    .mini-table { font-size: 0.9rem; border-collapse: collapse; width: 100%; margin-top: 10px; }
    .mini-table th { background-color: #F4F5F7; padding: 8px; text-align: right; border-bottom: 2px solid #DFE1E6; }
    .mini-table td { padding: 8px; border-bottom: 1px solid #DFE1E6; }
    .status-badge { padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
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

# --- עמוד 1: דאשבורד (הגרסה המושלמת) ---
if st.session_state.page == 'dashboard':
    st.markdown('<h1>מרכז התובנות של Orion</h1>', unsafe_allow_html=True)
    st.markdown('<div class="sync-status">Jira Cloud Connected | 15:45 ✅</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📌 תמונת מצב")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable ✅")
    with m2: st.metric("Focus Factor", "62%", "5% ↓ ⚠️")
    with m3: st.metric("Sentiment Score", "7.2/10", "0.4 ↑")

    st.markdown("""<div class="ai-insight-card">🦉 <strong>תובנת אוריון:</strong> זוהה עומס קוגניטיבי גבוה בצוות ה-Backend. מומלץ לרכז משימות קטנות ל-Epic אחד כדי לשמור על רצף עבודה.</div>""", unsafe_allow_html=True)

    st.markdown("### מגמות עומק (Exclusive Trends) 📈")
    g1, g2, g3 = st.columns(3)
    data = pd.DataFrame(np.random.randint(5, 15, size=(10, 3)))
    with g1:
        st.write("**🧠 עומס קוגניטיבי**")
        st.area_chart(data[0], color="#FFADCC", height=220)
    with g2:
        st.write("**📢 חוסר בתקשורת**")
        st.line_chart(data[1], color="#FFAB00", height=220)
    with g3:
        st.write("**📅 עמידה בלו\"ז**")
        st.bar_chart(data[2], color="#5243AA", height=220)

    st.markdown("---")
    st.markdown("### ⚡ פעולות ניהוליות")
    b1, b2, b3 = st.columns(3)
    with b1: st.button("📊 הפקת דוח מותאם", on_click=lambda: navigate_to('report'), use_container_width=True)
    with b2: st.button("🔍 ניתוח סיכונים", on_click=lambda: navigate_to('risks'), use_container_width=True)
    with b3: st.button("📅 נושאים לדיילי", on_click=lambda: navigate_to('daily'), use_container_width=True)

# --- עמוד 2: בונה דוח ו-Preview ---
elif st.session_state.page == 'report':
    if not st.session_state.show_preview:
        st.markdown("# בונה דוח תובנות ⚒️")
        st.info("🦉 **ניתוח AI:** זיהיתי שיפור של 12% בעמידה בלו\"ז לעומת שבוע שעבר.")
        c_r1, c_r2 = st.columns([2, 1])
        with c_r1:
            st.markdown("### בחרי תובנות:")
            st.checkbox("🦉 **עומס:** סיכון בצוות Backend.", value=True)
            st.checkbox("📅 **לו\"ז:** שיפור שבועי.", value=True)
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
        st.markdown('<div class="report-paper">', unsafe_allow_html=True)
        st.markdown(f"<h2>דוח סטטוס Orion</h2><p>תאריך: {datetime.now().strftime('%d/%m/%Y')}</p><hr>", unsafe_allow_html=True)
        st.markdown("### תקציר AI אסטרטגי:")
        st.write("מגמת שיפור של 12% בעמידה בזמנים. דגש על צמצום עומס קוגניטיבי בצוות Backend.")
        if st.session_state.personal_note:
            st.info(f"💬 **הערת המנהלת:** {st.session_state.personal_note}")
        st.markdown("### תובנות נבחרות:")
        st.write("* סיכון עומס בצוות ה-Backend עקב ריבוי משימות.")
        st.write("* שיפור משמעותי בעמידה בלוחות זמנים.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🚀 שלח דוח"): st.success("הדוח הופץ!")
        st.button("✍️ ערוך שוב", on_click=lambda: setattr(st.session_state, 'show_preview', False))

# --- עמוד 3: נושאים לדיילי (התוספת המשופרת) ---
elif st.session_state.page == 'daily':
    st.markdown("# 📅 הכנה לישיבת דיילי")
    col_d1, col_d2 = st.columns([1, 1])
    with col_d1:
        st.markdown("### 🕒 רעננות עדכוני בורד")
        st.markdown("""
        <table class="mini-table">
            <tr><th>מפתח</th><th>עדכון אחרון</th><th>סטטוס</th></tr>
            <tr><td>דנה (Backend)</td><td>לפני 15 דק'</td><td><span class="status-badge" style="background:#E3FCEF; color:#006644;">מעודכן</span></td></tr>
            <tr><td>יוסי (Frontend)</td><td>לפני שעתיים</td><td><span class="status-badge" style="background:#E3FCEF; color:#006644;">מעודכן</span></td></tr>
            <tr><td>מיכל (Mobile)</td><td>אתמול</td><td><span class="status-badge" style="background:#FFFAE6; color:#826A00;">דורש בדיקה</span></td></tr>
            <tr><td>אלון (Infrastructure)</td><td>לפני 3 ימים</td><td><span class="status-badge" style="background:#FFEBE6; color:#BF2600;">לא מעודכן</span></td></tr>
        </table>
        """, unsafe_allow_html=True)
    with col_d2:
        st.markdown("### 🦉 דגשים לשיחה")
        st.warning("⚠️ **אלון:** הבורד לא עודכן זמן רב. לוודא אם יש חסם טכני.")
        st.info("💡 **מיכל:** כדאי לשאול אם היא צריכה עזרה בסגירת המשימה.")
    st.markdown("---")
    st.button("🔙 חזרה לדאשבורד", on_click=lambda: navigate_to('dashboard'))


# --- עמוד 4: ניתוח סיכונים חכם (תיקון עיצובי לחלק העליון) ---
elif st.session_state.page == 'risks':
    # כותרת מעודנת וממורכזת עם אייקון
    st.markdown("<h2 style='text-align: center;'>🔍 ניתוח סיכונים חכם</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # יצירת פריסה מאוזנת למדד ותובנה
    col1, col2 = st.columns([1, 2.5])
    
    with col1:
        # עיטוף המדד בתוך קופסה קטנה ליישור
        st.markdown("<div style='background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #e9ecef;'>", unsafe_allow_html=True)
        st.metric("ביטחון ספרינט", "82%", "-3%")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        # התובנה הכחולה מיושרת לגובה המדד
        st.markdown("""
            <div style='background-color: #EBF2FF; border-right: 6px solid #0052CC; padding: 20px; border-radius: 4px; height: 100%; display: flex; align-items: center;'>
                <span>🦉 <strong>תובנת אוריון:</strong> מדד הביטחון ירד בגלל הצטברות משימות ב-QA ב-48 השעות האחרונות. מומלץ לתגבר בדיקות.</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)
    
    
