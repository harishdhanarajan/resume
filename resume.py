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
        st.image('images/python.png', use_column_width = 'auto')
    with col2:
        st.image('images/ai.PNG', use_column_width = 'auto')
    with col3:
        st.image('images/ml.PNG', use_column_width = 'auto')
    with col4:
        st.image('images/oracle.PNG', use_column_width = 'auto')
    with col1:
        st.image('images/snowflake.PNG', use_column_width = 'auto')
    with col2:
        st.image('images/datalake.PNG', use_column_width = 'auto')
    with col3:
        st.image('images/powerbi.PNG', use_column_width = 'auto')
    with col4:
        st.image('images/github.png', use_column_width = 'auto')
    
    
