import streamlit as st
from pathlib import Path

from session_state import initialize_session

from pages.login import render_login_page
from pages.investigator import render_investigator_page


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Investigator AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# SESSION INITIALIZATION
# --------------------------------------------------

initialize_session()


# --------------------------------------------------
# LOAD GLOBAL CSS
# --------------------------------------------------

css_file = (
    Path(__file__).parent
    / "styles"
    / "main.css"
)

if css_file.exists():

    with open(
        css_file,
        "r",
        encoding="utf-8"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# --------------------------------------------------
# HIDE STREAMLIT DEFAULT UI
# --------------------------------------------------

st.markdown(
    """
    <style>

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }

    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# APPLICATION ROUTING
# --------------------------------------------------

if st.session_state.logged_in:

    render_investigator_page()

else:

    render_login_page()