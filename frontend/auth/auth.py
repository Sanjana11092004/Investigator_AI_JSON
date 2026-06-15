import uuid
import streamlit as st


def login(email: str):
    st.session_state.logged_in = True
    st.session_state.user_email = email

    if not st.session_state.session_id:
        st.session_state.session_id = str(uuid.uuid4())


def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.session_state.session_id = None

    st.session_state.chat_history = []
    st.session_state.active_patient_id = None
    st.session_state.active_subject_id = None
    st.session_state.active_study_id = None


def is_authenticated():
    return st.session_state.get("logged_in", False)