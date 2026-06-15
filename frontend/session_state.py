import streamlit as st


def initialize_session():
    defaults = {
        "logged_in": False,
        "user_email": None,
        "session_id": None,

        "chat_history": [],
        "investigation_history": [],

        "uploaded_files": [],

        "api_connected": False,

        "active_patient_id": None,
        "active_subject_id": None,
        "active_study_id": None,

        "current_investigation_title": None
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value