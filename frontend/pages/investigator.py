import streamlit as st


def render_investigator_page():

    st.title("Investigator Workspace")

    st.success("Login successful")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()