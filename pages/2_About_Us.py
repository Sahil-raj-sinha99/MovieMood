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
        div[data-testid="column"]
        {
            text-align: center;
        } 
        div[data-testid="stLinkButton"] p
        {
            font-size: 0.9rem !important;
        } 
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"] {
            text-align: left;
        }
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
    st.write(f' <p style="font-size:2.75rem;font-weight:700;padding-top:15px"> About Us </p>',unsafe_allow_html=True)
with col2:
    st.image("images/logo.jpg")

"""
We are a group of grad students at UC Berkeley in the Master of Information and Data Science (MIDS) program. 

MovieMood was founded as part of our capstone class, where we had to develop a data science application, of our choice, from the ground up. 

Our team has a wide/diverse background ranging from data engineering / science to software engineering and UX design. 
"""

st.write(f'<br><br>',unsafe_allow_html=True)

col1,col2,col3,col4,col5=st.columns(5)
cols=[col1,col2,col3,col4,col5]

member_names = ["Neta Tartakovsky", "Sumedh Shah", "Josie Ruggieri", "Neil Prabhu", "Will Dudek"]
member_photos = ['Neta.jpeg', 'Sumedh.jpeg', 'Josie.jpeg', 'Neil.jpeg', 'Will.jpeg']
member_links = ['https://www.linkedin.com/in/neta-tartakovsky/',
                'https://www.linkedin.com/in/sumedhshah/',
                'https://www.linkedin.com/in/josefina-ruggieri-653050156/',
                'https://www.linkedin.com/in/neil-prabhu-9413b1ba/',
                'https://www.linkedin.com/in/will-dudek/']

for i in range(0,5):    
    with cols[i]:
        st.image('images/'+member_photos[i], use_column_width="always")
        st.write(f' <p style="font-size: 1.1rem;font-weight: 600;"> {member_names[i]} </p>',unsafe_allow_html=True)
        st.link_button("LinkedIn →", member_links[i])