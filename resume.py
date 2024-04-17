import requests
from streamlit_lottie import st_lottie
import streamlit as st
import sys
# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#local_css("r_style/style.css")


with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.image('images/python.png', use_column_width = 'auto')
    with col2:
        st.image('python.png', use_column_width = 'auto')
    with col3:
        st.image('python.png', use_column_width = 'auto')
    with col4:
        st.image('python.png', use_column_width = 'auto')
    with col5:
        st.image('python.png', use_column_width = 'auto')
    with col1:
        st.image('python.png', use_column_width = 'auto')
    with col2:
        st.image('python.png', use_column_width = 'auto')
    with col3:
        st.image('python.png', use_column_width = 'auto')
    
    