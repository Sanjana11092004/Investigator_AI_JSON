import streamlit as st


def render_stat_cards():

    cols = st.columns(6)

    cards = [

        ("Patients", "110"),
        ("Adverse Events", "566"),
        ("Labs", "16979"),
        ("Medications", "722"),
        ("Studies", "416"),
        ("Documents", "7")

    ]

    for col, card in zip(cols, cards):

        with col:

            st.metric(
                card[0],
                card[1]
            )