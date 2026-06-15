import streamlit as st


def render_topbar():

    col1, col2 = st.columns(
        [4, 2]
    )

    with col1:

        st.markdown(
            "## Investigator AI Assistant"
        )

        st.caption(
            "Clinical Trial Investigation Platform"
        )

    with col2:

        st.success(
            "Backend Connected"
        )