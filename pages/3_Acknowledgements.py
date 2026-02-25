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
We wanted to thank our instructors, Joyce Shen and Todd Holloway, for their guidance and ongoing support for this project. We then wanted to thank fellow classmate, Max Eagle, for providing us with our data source and data gathering technique for all of the movies we used in the project. Finally, we want to thank Chris Volinsky, NYU Professor/Netflix Prize winner who used to work at AT&T’s Chief Data Office with Sumedh, for his guidance and insightful comments on our modeling approach for MovieMood.

"""