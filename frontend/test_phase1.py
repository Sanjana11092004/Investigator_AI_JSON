import streamlit as st

from session_state import initialize_session
from auth.auth import login
from services.api_client import APIClient

initialize_session()

api = APIClient()

st.title("Phase 1 Test")

email = st.text_input("Email")

if st.button("Login"):
    login(email)

st.write("Logged In:", st.session_state.logged_in)
st.write("Session ID:", st.session_state.session_id)

if st.button("Check Backend"):
    st.session_state.api_connected = api.get_backend_status()

st.write("Backend Connected:", st.session_state.api_connected)

if st.button("Get Stats"):
    stats = api.get_dashboard_stats()
    st.json(stats)

if st.button("Get Documents"):
    docs = api.get_documents()
    st.json(docs)