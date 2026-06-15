import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            "## Investigator AI"
        )

        st.caption(
            "Clinical Investigation Assistant"
        )

        st.divider()

        st.button(
            "➕ New Investigation",
            use_container_width=True
        )

        st.markdown(
            "##### History"
        )

        st.markdown(
            """
            - Investigation 001
            - Investigation 002
            - Investigation 003
            """
        )

        st.divider()

        st.markdown(
            "##### Documents"
        )

        st.markdown(
            """
            - PHVIGIL2024_DM.json
            - PHVIGIL2024_LB.json
            - PHVIGIL2024_AE.json
            """
        )

        st.divider()

        st.markdown(
            "##### Upload"
        )

        uploaded = st.file_uploader(
            "",
            type=[
                "pdf",
                "csv",
                "xlsx",
                "json"
            ]
        )

        if uploaded:

            st.success(
                uploaded.name
            )

            st.button(
                "Ingest File",
                use_container_width=True
            )