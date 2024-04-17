import requests
import streamlit as st
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("r_style/style.css")
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,2])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
with col2:
    st.image('images/profile.PNG', use_column_width = 'auto')
    
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1,0.1, 1, 0.1, 1, 0.1, 1, 0.1])
    with col1:
        st.image('images/python.png', use_column_width = 'auto')
    with col3:
        st.image('images/ai.PNG', use_column_width = 'auto')
    with col5:
        st.image('images/ml.PNG', use_column_width = 'auto')
    with col7:
        st.image('images/oracle.PNG', use_column_width = 'auto')
    with col1:
        st.image('images/snowflake.PNG', use_column_width = 'auto')
    with col3:
        st.image('images/datalake.PNG', use_column_width = 'auto')
    with col5:
        st.image('images/powerbi.PNG', use_column_width = 'auto')
    with col7:
        st.image('images/github.png', use_column_width = 'auto')
    
    
