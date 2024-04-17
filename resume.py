import requests
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("r_style/style.css")

with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image('images/python.png', width = 100)
    with col2:
        st.image('images/ai.PNG', width = 100)
    with col3:
        st.image('images/ml.PNG', width = 100)
    with col4:
        st.image('images/oracle.PNG', width = 100)
    with col1:
        st.image('images/snowflake.PNG', width = 100)
    with col2:
        st.image('images/datalake.PNG', width = 100)
    with col3:
        st.image('images/powerbi.PNG', width = 100)
    with col4:
        st.image('images/github.png', use_column_width = 'auto')
    
    
