import requests
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("r_style/style.css")

with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.image('images/python.png', width = 100)
    with col2:
        st.image('images/ai.png', width = 100)
    with col3:
        st.image('images/ml.png', width = 100)
    with col4:
        st.image('images/oracle.png', width = 100)
    with col5:
        st.image('images/snowflake.png', width = 100)
    with col1:
        st.image('images/datalake.png', width = 100)
    with col2:
        st.image('images/powerbi.png', width = 100)
    with col3:
        st.image('images/github.png', width = 100)
    
    
