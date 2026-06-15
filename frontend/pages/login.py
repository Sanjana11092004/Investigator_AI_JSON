import streamlit as st
from auth.auth import login


def render_login_page():

    left, right = st.columns([1, 1.6], gap="large")

    with left:

        st.markdown(
            """
            <div style="
                background:#EAF3DE;
                padding:30px;
                border-radius:16px;
                min-height:650px;
                border:0.5px solid #C0DD97;
            ">
                <h1 style="color:#27500A;">
                    Investigator AI
                </h1>

                <p style="color:#3B6D11;">
                    AI-powered Clinical Investigation Platform
                </p>

                <br>

                <div style="
                    background:white;
                    padding:12px;
                    border-radius:12px;
                    border:0.5px solid #C0DD97;
                    margin-bottom:10px;
                ">
                    Clinical Study Analysis
                </div>

                <div style="
                    background:white;
                    padding:12px;
                    border-radius:12px;
                    border:0.5px solid #C0DD97;
                    margin-bottom:10px;
                ">
                    SDTM Subject Intelligence
                </div>

                <div style="
                    background:white;
                    padding:12px;
                    border-radius:12px;
                    border:0.5px solid #C0DD97;
                ">
                    Investigator Reasoning Engine
                </div>

                <br><br>

                <div style="
                    background:#F4FAE8;
                    padding:16px;
                    border-radius:12px;
                    border:0.5px solid #C0DD97;
                ">
                    <b>110</b> Patients<br>
                    <b>258</b> Adverse Events<br>
                    <b>11</b> Studies
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="
                background:white;
                border:0.5px solid #E8E6DF;
                border-radius:16px;
                padding:30px;
            ">
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <h1 style="
                text-align:center;
                color:#1A1A1A;
            ">
                Welcome Back
            </h1>
            """,
            unsafe_allow_html=True
        )

        email = st.text_input(
            "Work Email",
            placeholder="name@company.com"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Continue",
            use_container_width=True,
            type="primary"
        ):
            login(email)
            st.rerun()

        st.markdown(
            """
            <p style="
                text-align:center;
                color:#777;
                font-size:12px;
            ">
                Investigator AI Platform
            </p>
            """,
            unsafe_allow_html=True
        )