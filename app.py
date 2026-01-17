import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

# 1. הגדרות דף
st.set_page_config(page_title="Orion Executive Insights", page_icon="logo.png", layout="wide")

# 2. ניהול מצבי עמוד (Dashboard / Report / Preview)
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'show_preview' not in st.session_state:
    st.session_state.show_preview = False

# 3. CSS מעודכן לתצוגה מקדימה ובחירת פלטפורמה
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600&display=swap');
    html, body, [data-testid="stMarkdownContainer"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl; text-align: right;
    }
    .main .block-container { max-width: 1100px; padding: 2rem; margin: 0 auto; }
    
    /* עיצוב דף ה-Preview (כמו דף נייר) */
    .preview-paper {
        background-color: white;
        border: 1px solid #ddd;
        padding: 40px;
        border-radius: 2px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        color: #333;
        margin: 20px 0;
    }
    .platform-card {
        border: 1px solid #DFE1E6;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציות ניווט
def go_to_report(): st.session_state.page = 'report'; st.session_state.show_preview = False
def go_to_dashboard(): st.session_state.page = 'dashboard'
def trigger_preview(): st.session_state.show_preview = True

# --- Sidebar (צ'אט אוריון) ---
with st.sidebar:
    st.markdown('<div><span class="orion-icon"></span> שאל את אוריון</div>', unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "היי טלי, מוכנה להפיץ את הבשורה?"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    st.chat_input("שאלי משהו...")

# --- עמוד 1: דאשבורד ראשי ---
if st.session_state.page == 'dashboard':
    st.markdown(f"<h1>מרכז התובנות של Orion</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # מדדים וגרפים (השארתי את המבנה המנצח שלך)
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Resource Leak", "Low", "Stable")
    with m2: st.metric("Focus Factor", "62%", "-5% ⚠️")
    with m3: st.metric("Communication Gaps", "2.4", "-0.8")

    st.markdown("### 📈 מגמות עומק")
    g1, g2, g3 = st.columns(3)
    data = pd.DataFrame(np.random.randint(5, 15, size=(10, 3)))
    with g1: st.area_chart(data[0], color="#FFADCC", height=150)
    with g2: st.line_chart(data[1], color="#FFAB00", height=150)
    with g3: st.bar_chart(data[2], color="#5243AA", height=150)

    st.markdown("---")
    if st.button("📊 הפקת דוח מותאם", on_click=go_to_report): pass

# --- עמוד 2: בונה הדוח + Preview + בחירת פלטפורמה ---
elif st.session_state.page == 'report':
    st.markdown("# 🛠️ בונה דוח אסטרטגי")
    
    if not st.session_state.show_preview:
        # שלב א': בחירת תובנות וניתוח AI
        st.info("💡 **ניתוח AI לארכיון:** זיהיתי שיפור של 12% בעמידה בלו\"ז לעומת הדוח מהשבוע שעבר. מומלץ לציין זאת לטובה.")
        
        col_list, col_meta = st.columns([2, 1])
        with col_list:
            st.markdown("### 1. בחרי תובנות להפצה")
            c1 = st.checkbox("🦉 **תובנת עומס:** סיכון בצוות Backend.", value=True)
            c2 = st.checkbox("📢 **תובנת תקשורת:** פערים בתיעוד API.", value=True)
            c3 = st.checkbox("📅 **תובנת לו\"ז:** עיכוב פוטנציאלי של 3 ימים.", value=True)
        
        with col_meta:
            st.markdown("### 2. יעד הפצה")
            target = st.radio("לאן לשלוח?", ["Slack (as PDF)", "Email (as PDF)", "Download PDF Only"])
            st.text_input("הוסף הערה אישית לדוח:", placeholder="למשל: 'כל הכבוד על המאמץ השבוע'...")

        st.markdown("---")
        st.button("👁️ הצג תצוגה מקדימה (Preview)", on_click=trigger_preview, type="primary")
        st.button("✖️ ביטול וחזרה", on_click=go_to_dashboard)

    else:
        # שלב ב': תצוגה מקדימה (The PDF Preview)
        st.markdown("### 📄 תצוגה מקדימה של הדוח (PDF Preview)")
        st.caption("כך הדוח ייראה כקובץ שיצורף להודעה:")
        
        st.markdown(f"""
            <div class="preview-paper">
                <div style="display:flex; justify-content:space-between; border-bottom: 2px solid #eee; padding-bottom:10px;">
                    <h2 style="margin:0;">Orion Executive Report</h2>
                    <span>{datetime.now().strftime("%d/%m/%Y")}</span>
                </div>
                <div style="margin-top:20px;">
                    <h4>תקציר מנהלים:</h4>
                    <p>השבוע זוהתה מגמת שיפור משמעותית בעמידה בלוחות הזמנים (12%+). עם זאת, יש לשים לב לעומס הקוגניטיבי בצוות ה-Backend.</p>
                    <hr>
                    <h4>תובנות נבחרות:</h4>
                    <ul>
                        <li>🦉 סיכון עומס עקב Context Switching גבוה.</li>
                        <li>📅 עיכוב פוטנציאלי של 3 ימים באינטגרציה.</li>
                    </ul>
                    <div style="background:#f0f0f0; height:100px; text-align:center; padding-top:40px; color:#666;">
                        [כאן יופיעו גרפי המגמות שבחרת]
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        col_send, col_edit = st.columns([1, 4])
        with col_send:
            if st.button("🚀 אישור ושליחה סופית"):
                st.success("הקובץ נוצר ונשלח ליעד הנבחר!")
        with col_edit:
            st.button("✍️ חזור לעריכה", on_click=lambda: setattr(st.session_state, 'show_preview', False))
