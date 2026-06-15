# import uuid
# import requests
# import streamlit as st

# st.set_page_config(page_title="Investigator AI", page_icon="🔬", layout="wide")

# # -----------------------------
# # Premium Light CSS
# # -----------------------------
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

# /* ── Base ── */
# html, body, .stApp {
#     font-family: 'Inter', sans-serif !important;
# }
# .stApp {
#     background: #F0F4FA !important;
# }

# /* ── Scrollbar ── */
# ::-webkit-scrollbar { width: 4px; height: 4px; }
# ::-webkit-scrollbar-track { background: transparent; }
# ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 8px; }
# ::-webkit-scrollbar-thumb:hover { background: #94A3B8; }

# /* ── Sidebar panel ── */
# section[data-testid="stSidebar"] > div:first-child {
#     background: #FFFFFF !important;
#     border-right: 1px solid #E2E8F0 !important;
#     padding: 0 !important;
#     box-shadow: 2px 0 12px #1E3A5F0A;
# }

# /* ── Main content area ── */
# .main .block-container {
#     background: #F0F4FA !important;
#     padding-top: 1.5rem !important;
#     padding-bottom: 2rem !important;
# }

# /* ── Divider ── */
# hr {
#     border: none !important;
#     border-top: 1px solid #E9EEF6 !important;
#     margin: 0.75rem 0 !important;
# }

# /* ── Stat card ── */
# .stat-card {
#     background: #FFFFFF;
#     border: 1px solid #E2E8F0;
#     border-radius: 16px;
#     padding: 16px 14px;
#     position: relative;
#     overflow: hidden;
#     transition: border-color 0.25s, transform 0.2s, box-shadow 0.25s;
#     box-shadow: 0 1px 4px #1E3A5F08;
# }
# .stat-card:hover {
#     border-color: #2563EB44;
#     transform: translateY(-2px);
#     box-shadow: 0 6px 24px #2563EB14;
# }
# .stat-card::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 0; right: 0;
#     height: 3px;
#     background: linear-gradient(90deg, #2563EB, #7C3AED);
#     opacity: 0;
#     transition: opacity 0.25s;
# }
# .stat-card:hover::before { opacity: 1; }
# .stat-label {
#     font-size: 10px;
#     font-weight: 700;
#     letter-spacing: 0.09em;
#     text-transform: uppercase;
#     color: #94A3B8;
#     margin-bottom: 6px;
# }
# .stat-value {
#     font-size: 30px;
#     font-weight: 700;
#     color: #1E293B;
#     line-height: 1;
# }
# .stat-icon {
#     position: absolute;
#     top: 14px; right: 14px;
#     font-size: 20px;
#     opacity: 0.12;
# }

# /* ── Status badge ── */
# .status-badge {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     padding: 5px 12px;
#     border-radius: 999px;
#     font-size: 11px;
#     font-weight: 600;
#     letter-spacing: 0.04em;
# }
# .status-online {
#     background: #F0FDF4;
#     color: #16A34A;
#     border: 1px solid #BBF7D0;
# }
# .status-offline {
#     background: #FEF2F2;
#     color: #DC2626;
#     border: 1px solid #FECACA;
# }
# .status-dot {
#     width: 6px; height: 6px;
#     border-radius: 50%;
#     background: currentColor;
#     animation: pulse 2s infinite;
# }
# @keyframes pulse {
#     0%, 100% { opacity: 1; }
#     50% { opacity: 0.35; }
# }

# /* ── Chat messages ── */
# .stChatMessage {
#     background: transparent !important;
#     border: none !important;
# }
# [data-testid="stChatMessageContent"] {
#     background: #FFFFFF !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 14px !important;
#     padding: 14px 16px !important;
#     color: #334155 !important;
#     font-size: 14px !important;
#     line-height: 1.65 !important;
#     box-shadow: 0 1px 4px #1E3A5F06;
# }
# [data-testid="stChatMessageContent"] p {
#     color: #334155 !important;
# }

# /* ── Chat input ── */
# .stChatInput {
#     background: #FFFFFF !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 14px !important;
#     padding: 4px !important;
#     box-shadow: 0 2px 12px #1E3A5F08;
#     transition: border-color 0.2s, box-shadow 0.2s;
# }
# .stChatInput:focus-within {
#     border-color: #2563EB66 !important;
#     box-shadow: 0 2px 20px #2563EB12 !important;
# }
# .stChatInput > div {
#     background: transparent !important;
# }
# .stChatInput textarea {
#     background: transparent !important;
#     color: #1E293B !important;
#     font-size: 14px !important;
#     font-family: 'Inter', sans-serif !important;
#     border: none !important;
#     outline: none !important;
#     box-shadow: none !important;
#     padding: 10px 12px !important;
#     caret-color: #2563EB;
# }
# .stChatInput textarea::placeholder {
#     color: #CBD5E1 !important;
# }
# .stChatInput button {
#     background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
#     border-radius: 10px !important;
#     border: none !important;
#     width: 36px !important;
#     height: 36px !important;
#     transition: opacity 0.2s, transform 0.15s !important;
#     box-shadow: 0 2px 10px #2563EB33;
# }
# .stChatInput button:hover {
#     opacity: 0.88 !important;
#     transform: scale(1.04) !important;
# }
# .stChatInput button svg { fill: white !important; }

# /* ── Buttons ── */
# .stButton > button {
#     width: 100%;
#     background: transparent !important;
#     color: #64748B !important;
#     border: 1px solid #E2E8F0 !important;
#     border-radius: 10px !important;
#     font-size: 12px !important;
#     font-weight: 500 !important;
#     padding: 6px 10px !important;
#     transition: all 0.2s !important;
#     font-family: 'Inter', sans-serif !important;
#     text-align: left !important;
# }
# .stButton > button:hover {
#     background: #F8FAFC !important;
#     border-color: #2563EB44 !important;
#     color: #334155 !important;
# }
# /* Primary "New Investigation" button */
# .stButton > button:first-child:not([data-testid]) {
#     background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
#     color: white !important;
#     border-color: transparent !important;
#     border-radius: 12px !important;
#     padding: 9px 12px !important;
#     font-weight: 600 !important;
#     font-size: 13px !important;
#     text-align: center !important;
#     box-shadow: 0 4px 20px #2563EB28;
# }
# .stButton > button:first-child:not([data-testid]):hover {
#     opacity: 0.88 !important;
#     color: white !important;
#     box-shadow: 0 6px 28px #2563EB40 !important;
#     transform: translateY(-1px) !important;
# }

# /* ── File uploader ── */
# .stFileUploader {
#     background: #F8FAFC !important;
#     border: 1.5px dashed #CBD5E1 !important;
#     border-radius: 12px !important;
#     padding: 8px !important;
#     transition: border-color 0.2s, background 0.2s;
# }
# .stFileUploader:hover {
#     border-color: #2563EB66 !important;
#     background: #EFF6FF !important;
# }
# .stFileUploader label { color: #94A3B8 !important; font-size: 12px !important; }
# .stFileUploader [data-testid="stFileDropzone"] {
#     background: transparent !important;
#     border: none !important;
#     padding: 0 !important;
# }
# .stFileUploader [data-testid="stFileDropzone"] p {
#     color: #CBD5E1 !important;
#     font-size: 12px !important;
# }

# /* ── Expander ── */
# .streamlit-expanderHeader {
#     background: transparent !important;
#     color: #64748B !important;
#     font-size: 12px !important;
#     font-weight: 500 !important;
#     border: none !important;
#     padding: 4px 0 !important;
# }
# .streamlit-expanderHeader:hover { color: #2563EB !important; }
# .streamlit-expanderContent {
#     background: transparent !important;
#     border: none !important;
#     padding: 2px 0 0 8px !important;
# }

# /* ── Captions ── */
# .stCaption, .stCaption p {
#     color: #94A3B8 !important;
#     font-size: 10px !important;
#     letter-spacing: 0.1em !important;
#     text-transform: uppercase !important;
#     font-weight: 600 !important;
# }

# /* ── Spinner ── */
# .stSpinner > div { border-top-color: #2563EB !important; }

# /* ── Headings ── */
# h1, h2, h3 {
#     color: #1E293B !important;
#     font-family: 'Inter', sans-serif !important;
# }

# /* ── Alerts ── */
# .stAlert { border-radius: 12px !important; font-size: 13px !important; }
# .stSuccess { background: #F0FDF422 !important; border-left-color: #22C55E !important; }
# .stError   { background: #FEF2F222 !important; border-left-color: #EF4444 !important; }

# /* ── Logo ── */
# .logo-wrap {
#     display: flex;
#     align-items: center;
#     gap: 10px;
#     padding: 20px 16px 12px;
# }
# .logo-icon {
#     width: 36px; height: 36px;
#     background: linear-gradient(135deg, #2563EB, #7C3AED);
#     border-radius: 10px;
#     display: flex; align-items: center; justify-content: center;
#     font-size: 18px;
#     box-shadow: 0 4px 14px #2563EB30;
#     flex-shrink: 0;
# }
# .logo-text {
#     font-size: 15px;
#     font-weight: 700;
#     color: #1E293B;
#     letter-spacing: -0.01em;
# }
# .logo-sub {
#     font-size: 10px;
#     color: #94A3B8;
#     letter-spacing: 0.06em;
#     text-transform: uppercase;
# }

# /* ── Section label ── */
# .section-label {
#     font-size: 10px;
#     font-weight: 700;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     color: #94A3B8;
#     padding: 8px 0 4px;
# }

# /* ── Chat header ── */
# .chat-header {
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     margin-bottom: 1rem;
#     padding-bottom: 1rem;
#     border-bottom: 1px solid #E9EEF6;
# }
# .chat-title {
#     font-size: 22px;
#     font-weight: 700;
#     color: #1E293B;
#     letter-spacing: -0.02em;
# }
# .chat-subtitle {
#     font-size: 12px;
#     color: #94A3B8;
#     margin-top: 2px;
# }

# /* ── Watermark ── */
# .watermark {
#     font-size: 10px;
#     color: #E2E8F0;
#     text-align: center;
#     padding: 8px;
#     letter-spacing: 0.08em;
# }

# /* ── User/assistant avatars ── */
# .stChatMessage [data-testid="chatAvatarIcon-user"] {
#     background: linear-gradient(135deg, #1D4ED8, #6D28D9) !important;
#     border-radius: 8px !important;
# }
# .stChatMessage [data-testid="chatAvatarIcon-assistant"] {
#     background: linear-gradient(135deg, #0F766E, #0369A1) !important;
#     border-radius: 8px !important;
# }

# /* ── Fade-up entrance ── */
# @keyframes fadeUp {
#     from { opacity: 0; transform: translateY(8px); }
#     to   { opacity: 1; transform: translateY(0); }
# }
# .stat-card { animation: fadeUp 0.4s ease both; }
# .stat-card:nth-child(1) { animation-delay: 0.05s; }
# .stat-card:nth-child(2) { animation-delay: 0.10s; }
# .stat-card:nth-child(3) { animation-delay: 0.15s; }
# .stat-card:nth-child(4) { animation-delay: 0.20s; }
# .stat-card:nth-child(5) { animation-delay: 0.25s; }
# .stat-card:nth-child(6) { animation-delay: 0.30s; }
# </style>
# """, unsafe_allow_html=True)

# # -----------------------------
# # Session
# # -----------------------------
# defaults = {
#     "session_id": str(uuid.uuid4()),
#     "chat_history": [],
#     "investigation_history": []
# }
# for k, v in defaults.items():
#     if k not in st.session_state:
#         st.session_state[k] = v

# BASE_URL = "http://localhost:8000"

# # -----------------------------
# # API helpers (unchanged)
# # -----------------------------
# def get_stats():
#     try:
#         return requests.get(f"{BASE_URL}/dashboard/stats").json()
#     except:
#         return {}

# def get_docs():
#     try:
#         return requests.get(f"{BASE_URL}/dashboard/documents").json()
#     except:
#         return []

# def backend_ok():
#     try:
#         return requests.get(f"{BASE_URL}/health", timeout=3).status_code == 200
#     except:
#         return False

# def ask_ai(question):
#     r = requests.post(
#         f"{BASE_URL}/investigator/chat",
#         json={
#             "session_id": st.session_state.session_id,
#             "question": question
#         },
#         timeout=120
#     )
#     return r.json().get("response", "No response")

# # -----------------------------
# # Data
# # -----------------------------
# stats = get_stats()
# docs  = get_docs()

# # -----------------------------
# # Layout
# # -----------------------------
# left, right = st.columns([1, 4])

# # ── Sidebar ─────────────────────────────────────────────────────────────
# with left:
#     st.markdown("""
#     <div class="logo-wrap">
#         <div class="logo-icon">🔬</div>
#         <div>
#             <div class="logo-text">Investigator AI</div>
#             <div class="logo-sub">Clinical Platform</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     if st.button("＋  New Investigation"):
#         st.session_state.chat_history = []
#         st.session_state.session_id  = str(uuid.uuid4())
#         st.rerun()

#     st.divider()

#     st.markdown('<div class="section-label">Recent Investigations</div>', unsafe_allow_html=True)

#     if not st.session_state.investigation_history:
#         st.markdown(
#             '<div style="font-size:11px;color:#CBD5E1;padding:4px 0;">No investigations yet</div>',
#             unsafe_allow_html=True
#         )
#     else:
#         for item in st.session_state.investigation_history[-10:]:
#             st.button(f"◎  {item}", key=item)

#     st.divider()

#     st.markdown('<div class="section-label">Source Files</div>', unsafe_allow_html=True)

#     grouped = {}
#     for d in docs:
#         grouped.setdefault(d["category"], []).append(d["name"])

#     if grouped:
#         for cat, files in grouped.items():
#             with st.expander(f"{cat}  ({len(files)})"):
#                 for f in files:
#                     st.markdown(
#                         f'<div style="font-size:11px;color:#64748B;padding:3px 0;'
#                         f'border-left:2px solid #E2E8F0;padding-left:8px;margin:2px 0;">'
#                         f'📄 {f}</div>',
#                         unsafe_allow_html=True
#                     )
#     else:
#         st.markdown(
#             '<div style="font-size:11px;color:#CBD5E1;padding:4px 0;">No files ingested yet</div>',
#             unsafe_allow_html=True
#         )

#     st.divider()

#     st.markdown('<div class="section-label">Upload</div>', unsafe_allow_html=True)
#     uploaded = st.file_uploader(
#         "Drop file here",
#         type=["pdf", "json", "xlsx", "xls"],
#         label_visibility="collapsed"
#     )
#     if uploaded and st.button("⬆  Ingest File"):
#         files = {"file": (uploaded.name, uploaded, uploaded.type)}
#         resp = requests.post(
#             f"{BASE_URL}/upload/upload",
#             files=files,
#             timeout=300
#         ).json()
#         st.success(resp.get("message", "Done"))
#         st.rerun()

#     st.markdown('<div class="watermark">INVESTIGATOR AI · v2.0</div>', unsafe_allow_html=True)

# # ── Main panel ──────────────────────────────────────────────────────────
# with right:

#     is_online = backend_ok()
#     status_html = (
#         '<span class="status-badge status-online"><span class="status-dot"></span>Connected</span>'
#         if is_online else
#         '<span class="status-badge status-offline"><span class="status-dot"></span>Offline</span>'
#     )

#     st.markdown(f"""
#     <div class="chat-header">
#         <div>
#             <div class="chat-title">Investigator AI Assistant</div>
#             <div class="chat-subtitle">Clinical Investigation Workspace</div>
#         </div>
#         {status_html}
#     </div>
#     """, unsafe_allow_html=True)

#     # ── Stat cards ──────────────────────────────────────────────────────
#     values = [
#         ("Patients",        stats.get("patients", 0)),
#         ("Adverse Events",  stats.get("adverse_events", 0)),
#         ("Labs",            stats.get("labs", 0)),
#         ("Medications",     stats.get("medications", 0)),
#         ("Studies",         stats.get("studies", 0)),
#         ("Documents",       stats.get("documents", 0)),
#     ]

#     cols = st.columns(6)
#     for col, (name, val) in zip(cols, values):
#         with col:
#             st.markdown(f"""
#             <div class="stat-card">
#                 <div class="stat-label">{name}</div>
#                 <div class="stat-value">{val}</div>
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

#     # ── Chat ────────────────────────────────────────────────────────────
#     with st.container():
#         if not st.session_state.chat_history:
#             st.markdown("""
#             <div style="
#                 text-align: center;
#                 padding: 56px 20px;
#                 color: #CBD5E1;
#             ">
#                 <div style="
#                     width:64px;height:64px;
#                     background:linear-gradient(135deg,#EFF6FF,#F5F3FF);
#                     border:1px solid #E2E8F0;
#                     border-radius:20px;
#                     display:flex;align-items:center;justify-content:center;
#                     font-size:32px;
#                     margin:0 auto 16px;
#                     box-shadow:0 4px 16px #2563EB0F;
#                 ">🔬</div>
#                 <div style="font-size:18px;font-weight:600;color:#1E293B;margin-bottom:8px;">
#                     Start an Investigation
#                 </div>
#                 <div style="font-size:13px;color:#94A3B8;max-width:400px;margin:0 auto;line-height:1.65;">
#                     Ask about patients, adverse events, lab results, medications,
#                     or any clinical data ingested into the platform.
#                 </div>
#                 <div style="
#                     display:flex;gap:8px;justify-content:center;flex-wrap:wrap;
#                     margin-top:24px;
#                 ">
#                     <span style="background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;
#                         padding:6px 14px;border-radius:999px;font-size:11px;font-weight:500;
#                         box-shadow:0 1px 4px #1E3A5F06;">
#                         🔍 Find adverse events for Patient 12
#                     </span>
#                     <span style="background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;
#                         padding:6px 14px;border-radius:999px;font-size:11px;font-weight:500;
#                         box-shadow:0 1px 4px #1E3A5F06;">
#                         📋 Summarize latest labs
#                     </span>
#                     <span style="background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;
#                         padding:6px 14px;border-radius:999px;font-size:11px;font-weight:500;
#                         box-shadow:0 1px 4px #1E3A5F06;">
#                         💊 List active medications
#                     </span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             for msg in st.session_state.chat_history:
#                 with st.chat_message(msg["role"]):
#                     st.markdown(msg["content"])

#     # ── Input ────────────────────────────────────────────────────────────
#     prompt = st.chat_input("Ask Investigator AI anything about your clinical data…")

#     if prompt:
#         if len(st.session_state.chat_history) == 0:
#             st.session_state.investigation_history.insert(0, prompt[:50])

#         st.session_state.chat_history.append({"role": "user", "content": prompt})

#         with st.spinner("Analyzing…"):
#             answer = ask_ai(prompt)

#         st.session_state.chat_history.append({"role": "assistant", "content": answer})
#         st.rerun()



import uuid
import requests
import streamlit as st

st.set_page_config(page_title="Investigator AI", page_icon="🔬", layout="wide")

# -----------------------------
# Premium Light CSS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Base ── */
html, body, .stApp {
    font-family: 'Inter', sans-serif !important;
}
.stApp {
    background: #F0F4FA !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: #94A3B8; }

/* ── Block container ── */
.main .block-container {
    background: #F0F4FA !important;
    padding: 1.5rem 1.5rem 2rem !important;
    max-width: 100% !important;
}

/* ══════════════════════════════════════════════════════
   PANEL CARDS — scoped to our custom marker divs only
   These divs (#sidebar-panel-marker, #main-panel-marker)
   are injected as the FIRST child of each layout column,
   so we walk up via :has() to style the stColumn wrapper.
   ══════════════════════════════════════════════════════ */

/* Sidebar card */
div[data-testid="stColumn"]:has(> div > div > div > #sidebar-panel-marker) {
    background: #EEF3FB !important;
    border-radius: 16px !important;
    border: 1.5px solid #BFDBFE !important;
    box-shadow: 2px 0 16px rgba(37,99,235,0.08) !important;
    min-height: 82vh !important;
    padding: 4px 8px 12px !important;
}

/* Main panel card */
div[data-testid="stColumn"]:has(> div > div > div > #main-panel-marker) {
    background: #FFFFFF !important;
    border-radius: 16px !important;
    border: 1.5px solid #E2E8F0 !important;
    box-shadow: 0 2px 16px rgba(30,58,95,0.06) !important;
    min-height: 82vh !important;
    padding: 20px 24px !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid #E9EEF6 !important;
    margin: 0.75rem 0 !important;
}

/* ── Stat card ── */
.stat-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 14px 10px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.2s, box-shadow 0.25s;
    box-shadow: 0 1px 4px rgba(30,58,95,0.05);
}
.stat-card:hover {
    border-color: rgba(37,99,235,0.27);
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(37,99,235,0.08);
}
.stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #2563EB, #7C3AED);
    opacity: 0;
    transition: opacity 0.25s;
}
.stat-card:hover::before { opacity: 1; }
.stat-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #94A3B8;
    margin-bottom: 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.stat-value {
    font-size: 28px;
    font-weight: 700;
    color: #1E293B;
    line-height: 1;
}

/* ── Status badge ── */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.status-online {
    background: #F0FDF4;
    color: #16A34A;
    border: 1px solid #BBF7D0;
}
.status-offline {
    background: #FEF2F2;
    color: #DC2626;
    border: 1px solid #FECACA;
}
.status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.35; }
}

/* ── Chat messages ── */
.stChatMessage {
    background: transparent !important;
    border: none !important;
}
[data-testid="stChatMessageContent"] {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 14px !important;
    padding: 14px 16px !important;
    color: #334155 !important;
    font-size: 14px !important;
    line-height: 1.65 !important;
    box-shadow: 0 1px 4px rgba(30,58,95,0.04);
}
[data-testid="stChatMessageContent"] p { color: #334155 !important; }

/* ── Chat input ── */
.stChatInput {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 14px !important;
    padding: 4px !important;
    box-shadow: 0 2px 12px rgba(30,58,95,0.05);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.stChatInput:focus-within {
    border-color: rgba(37,99,235,0.4) !important;
    box-shadow: 0 2px 20px rgba(37,99,235,0.07) !important;
}
.stChatInput > div { background: transparent !important; }
.stChatInput textarea {
    background: transparent !important;
    color: #1E293B !important;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
    padding: 10px 12px !important;
    caret-color: #2563EB;
}
.stChatInput textarea::placeholder { color: #CBD5E1 !important; }
.stChatInput button {
    background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
    border-radius: 10px !important;
    border: none !important;
    width: 36px !important;
    height: 36px !important;
    transition: opacity 0.2s, transform 0.15s !important;
    box-shadow: 0 2px 10px rgba(37,99,235,0.2);
}
.stChatInput button:hover {
    opacity: 0.88 !important;
    transform: scale(1.04) !important;
}
.stChatInput button svg { fill: white !important; }

/* ── Buttons ── */
.stButton > button {
    width: 100%;
    background: transparent !important;
    color: #64748B !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 10px !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    padding: 6px 10px !important;
    transition: all 0.2s !important;
    font-family: 'Inter', sans-serif !important;
    text-align: left !important;
}
.stButton > button:hover {
    background: #F8FAFC !important;
    border-color: rgba(37,99,235,0.27) !important;
    color: #334155 !important;
}
.new-investigation-btn .stButton > button {
    background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
    color: white !important;
    border-color: transparent !important;
    border-radius: 12px !important;
    padding: 9px 12px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    text-align: center !important;
    box-shadow: 0 4px 20px rgba(37,99,235,0.16);
}
.new-investigation-btn .stButton > button:hover {
    opacity: 0.88 !important;
    color: white !important;
    box-shadow: 0 6px 28px rgba(37,99,235,0.25) !important;
    transform: translateY(-1px) !important;
}

/* ── File uploader ── */
.stFileUploader {
    background: #F8FAFC !important;
    border: 1.5px dashed #CBD5E1 !important;
    border-radius: 12px !important;
    padding: 8px !important;
    transition: border-color 0.2s, background 0.2s;
}
.stFileUploader:hover {
    border-color: rgba(37,99,235,0.4) !important;
    background: #EFF6FF !important;
}
.stFileUploader label { color: #94A3B8 !important; font-size: 12px !important; }
.stFileUploader [data-testid="stFileDropzone"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
.stFileUploader [data-testid="stFileDropzone"] p {
    color: #CBD5E1 !important;
    font-size: 12px !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: transparent !important;
    color: #64748B !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    border: none !important;
    padding: 4px 0 !important;
}
.streamlit-expanderHeader:hover { color: #2563EB !important; }
.streamlit-expanderContent {
    background: transparent !important;
    border: none !important;
    padding: 2px 0 0 8px !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #2563EB !important; }

/* ── Headings ── */
h1, h2, h3 {
    color: #1E293B !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── Alerts ── */
.stAlert { border-radius: 12px !important; font-size: 13px !important; }
.stSuccess { background: rgba(240,253,244,0.13) !important; border-left-color: #22C55E !important; }
.stError   { background: rgba(254,242,242,0.13) !important; border-left-color: #EF4444 !important; }

/* ── Logo ── */
.logo-wrap {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 20px 8px 12px;
}
.logo-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #2563EB, #7C3AED);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    box-shadow: 0 4px 14px rgba(37,99,235,0.19);
    flex-shrink: 0;
}
.logo-text {
    font-size: 15px;
    font-weight: 700;
    color: #1E293B;
    letter-spacing: -0.01em;
}
.logo-sub {
    font-size: 10px;
    color: #94A3B8;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* ── Section label ── */
.section-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #94A3B8;
    padding: 8px 0 4px;
}

/* ── Chat header ── */
.chat-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #E9EEF6;
}
.chat-title {
    font-size: 22px;
    font-weight: 700;
    color: #1E293B;
    letter-spacing: -0.02em;
}
.chat-subtitle {
    font-size: 12px;
    color: #94A3B8;
    margin-top: 2px;
}

/* ── Watermark ── */
.watermark {
    font-size: 10px;
    color: #CBD5E1;
    text-align: center;
    padding: 8px;
    letter-spacing: 0.08em;
}

/* ── Avatars ── */
.stChatMessage [data-testid="chatAvatarIcon-user"] {
    background: linear-gradient(135deg, #1D4ED8, #6D28D9) !important;
    border-radius: 8px !important;
}
.stChatMessage [data-testid="chatAvatarIcon-assistant"] {
    background: linear-gradient(135deg, #0F766E, #0369A1) !important;
    border-radius: 8px !important;
}

/* ── Fade-up entrance ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
.stat-card { animation: fadeUp 0.4s ease both; }
.stat-card:nth-child(1) { animation-delay: 0.05s; }
.stat-card:nth-child(2) { animation-delay: 0.10s; }
.stat-card:nth-child(3) { animation-delay: 0.15s; }
.stat-card:nth-child(4) { animation-delay: 0.20s; }
.stat-card:nth-child(5) { animation-delay: 0.25s; }
.stat-card:nth-child(6) { animation-delay: 0.30s; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session
# -----------------------------
defaults = {
    "session_id": str(uuid.uuid4()),
    "chat_history": [],
    "investigation_history": []
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

BASE_URL = "http://localhost:8000"

# -----------------------------
# API helpers
# -----------------------------
def get_stats():
    try:
        return requests.get(f"{BASE_URL}/dashboard/stats").json()
    except:
        return {}

def get_docs():
    try:
        return requests.get(f"{BASE_URL}/dashboard/documents").json()
    except:
        return []

def backend_ok():
    try:
        return requests.get(f"{BASE_URL}/health", timeout=3).status_code == 200
    except:
        return False

def ask_ai(question):
    r = requests.post(
        f"{BASE_URL}/investigator/chat",
        json={
            "session_id": st.session_state.session_id,
            "question": question
        },
        timeout=120
    )
    return r.json().get("response", "No response")

# -----------------------------
# Data
# -----------------------------
stats = get_stats()
docs  = get_docs()

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([1, 4], gap="medium")

# ── Sidebar ─────────────────────────────────────────────────────────────
with left:
    # Anchor marker — :has() selector latches onto this to style the column
    st.markdown('<div id="sidebar-panel-marker"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="logo-wrap">
        <div class="logo-icon">🔬</div>
        <div>
            <div class="logo-text">Investigator AI</div>
            <div class="logo-sub">Clinical Platform</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # New Investigation button — wrapped in a div for targeted styling
    st.markdown('<div class="new-investigation-btn">', unsafe_allow_html=True)
    if st.button("＋  New Investigation"):
        st.session_state.chat_history = []
        st.session_state.session_id  = str(uuid.uuid4())
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown('<div class="section-label">Recent Investigations</div>', unsafe_allow_html=True)

    if not st.session_state.investigation_history:
        st.markdown(
            '<div style="font-size:11px;color:#CBD5E1;padding:4px 0;">No investigations yet</div>',
            unsafe_allow_html=True
        )
    else:
        for item in st.session_state.investigation_history[-10:]:
            st.button(f"◎  {item}", key=item)

    st.divider()

    st.markdown('<div class="section-label">Source Files</div>', unsafe_allow_html=True)

    grouped = {}
    for d in docs:
        grouped.setdefault(d["category"], []).append(d["name"])

    if grouped:
        for cat, files in grouped.items():
            with st.expander(f"{cat}  ({len(files)})"):
                for f in files:
                    st.markdown(
                        f'<div style="font-size:11px;color:#64748B;padding:3px 0;'
                        f'border-left:2px solid #BFDBFE;padding-left:8px;margin:2px 0;">'
                        f'📄 {f}</div>',
                        unsafe_allow_html=True
                    )
    else:
        st.markdown(
            '<div style="font-size:11px;color:#CBD5E1;padding:4px 0;">No files ingested yet</div>',
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown('<div class="section-label">Upload</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader(
        "Drop file here",
        type=["pdf", "json", "xlsx", "xls"],
        label_visibility="collapsed"
    )
    if uploaded and st.button("⬆  Ingest File"):
        files = {"file": (uploaded.name, uploaded, uploaded.type)}
        resp = requests.post(
            f"{BASE_URL}/upload/upload",
            files=files,
            timeout=300
        ).json()
        st.success(resp.get("message", "Done"))
        st.rerun()

    st.markdown('<div class="watermark">INVESTIGATOR AI · v2.0</div>', unsafe_allow_html=True)

# ── Main panel ──────────────────────────────────────────────────────────
with right:
    # Anchor marker for the main panel
    st.markdown('<div id="main-panel-marker"></div>', unsafe_allow_html=True)

    is_online = backend_ok()
    status_html = (
        '<span class="status-badge status-online"><span class="status-dot"></span>Connected</span>'
        if is_online else
        '<span class="status-badge status-offline"><span class="status-dot"></span>Offline</span>'
    )

    st.markdown(f"""
    <div class="chat-header">
        <div>
            <div class="chat-title">Investigator AI Assistant</div>
            <div class="chat-subtitle">Clinical Investigation Workspace</div>
        </div>
        {status_html}
    </div>
    """, unsafe_allow_html=True)

    # ── Stat cards ──────────────────────────────────────────────────────
    values = [
        ("Patients",       stats.get("patients", 0)),
        ("Adverse Events", stats.get("adverse_events", 0)),
        ("Labs",           stats.get("labs", 0)),
        ("Medications",    stats.get("medications", 0)),
        ("Studies",        stats.get("studies", 0)),
        ("Documents",      stats.get("documents", 0)),
    ]

    cols = st.columns(6, gap="small")
    for col, (name, val) in zip(cols, values):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">{name}</div>
                <div class="stat-value">{val}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # ── Chat ────────────────────────────────────────────────────────────
    with st.container():
        if not st.session_state.chat_history:
            st.markdown("""
            <div style="text-align:center;padding:56px 20px;color:#CBD5E1;">
                <div style="
                    width:64px;height:64px;
                    background:linear-gradient(135deg,#EFF6FF,#F5F3FF);
                    border:1px solid #E2E8F0;border-radius:20px;
                    display:flex;align-items:center;justify-content:center;
                    font-size:32px;margin:0 auto 16px;
                    box-shadow:0 4px 16px rgba(37,99,235,0.06);
                ">🔬</div>
                <div style="font-size:18px;font-weight:600;color:#1E293B;margin-bottom:8px;">
                    Start an Investigation
                </div>
                <div style="font-size:13px;color:#94A3B8;max-width:400px;margin:0 auto;line-height:1.65;">
                    Ask about patients, adverse events, lab results, medications,
                    or any clinical data ingested into the platform.
                </div>
                <div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:24px;">
                    <span style="background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;
                        padding:6px 14px;border-radius:999px;font-size:11px;font-weight:500;
                        box-shadow:0 1px 4px rgba(30,58,95,0.04);">
                        🔍 Find adverse events for Patient 12
                    </span>
                    <span style="background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;
                        padding:6px 14px;border-radius:999px;font-size:11px;font-weight:500;
                        box-shadow:0 1px 4px rgba(30,58,95,0.04);">
                        📋 Summarize latest labs
                    </span>
                    <span style="background:#F8FAFC;border:1px solid #E2E8F0;color:#64748B;
                        padding:6px 14px;border-radius:999px;font-size:11px;font-weight:500;
                        box-shadow:0 1px 4px rgba(30,58,95,0.04);">
                        💊 List active medications
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

    # ── Input ────────────────────────────────────────────────────────────
    prompt = st.chat_input("Ask Investigator AI anything about your clinical data…")

    if prompt:
        if len(st.session_state.chat_history) == 0:
            st.session_state.investigation_history.insert(0, prompt[:50])

        st.session_state.chat_history.append({"role": "user", "content": prompt})

        with st.spinner("Analyzing…"):
            answer = ask_ai(prompt)

        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()
