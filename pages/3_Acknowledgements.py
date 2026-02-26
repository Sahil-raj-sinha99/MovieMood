import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 30px;
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="stStyledFullScreenFrame"] div {
            justify-content: right;
        }
    </style>
    """,
    unsafe_allow_html=True
)

col1,col2 = st.columns([3, 1])
with col1:
    st.write(f' <p style="font-size:2.75rem;font-weight:700;padding-top:15px"> Acknowledgements </p>',unsafe_allow_html=True)
with col2:
    st.image("images/logo.jpg")

"""
We are sincerely grateful to our AIML internship trainer for their invaluable guidance, which enabled us to successfully develop MovieMood, an AI-based movie recommendation system built using Spotify playlist analysis
"""
