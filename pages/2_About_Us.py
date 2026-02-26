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
Sahil Raj Sinha is an aspiring Artificial Intelligence and Machine Learning professional with a strong foundation in Computer Science and Data Analytics.

He is passionate about building intelligent, data-driven applications that combine analytical precision with user-focused design. His expertise includes machine learning model development, data preprocessing, recommendation systems, and interactive web deployment using Streamlit.

Through projects like MovieMood, Sahil demonstrates his ability to design, develop, and deploy end-to-end AI solutions that solve real-world problems efficiently and effectively.

He is committed to continuous learning, innovation, and applying advanced technologies to create scalable and impactful software solutions.
"""

st.write(f'<br><br>',unsafe_allow_html=True)

col1,col2,col3,col4,col5=st.columns(5)
cols=[col1,col2,col3,col4,col5]

member_names = ["Sahil Raj Sinha"]
member_photos = ['sahil.jpeg']
member_links = ['https://www.linkedin.com/in/sahil-raj-sinha-43708626a']

for i in range(0,1):    
    with cols[i]:
        st.image('images/'+member_photos[i], use_column_width="always")
        st.write(f' <p style="font-size: 1.1rem;font-weight: 600;"> {member_names[i]} </p>',unsafe_allow_html=True)
        st.link_button("LinkedIn →", member_links[i])
