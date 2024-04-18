import requests
import streamlit as st
from myprofile import *

PAGE_TITLE = "Digital CV | Harish"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#local_css("r_style/style.css")

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:50px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,1.5])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
st.write(info['About'])

with col2:
    st.image('images/profile.PNG', use_column_width = 'auto')

st.markdown("---")
st.subheader("Experience & Qulifications")
col1, col2, col3 = st.columns([4,0.5,0.5])
col4, col5, col6 = st.columns([4,0.5,0.5])
with col1:
    with st.expander("Bank of New York Mellon (June 2020 - Present)"):
        st.image('images/bnym_jd.png', use_column_width = 'auto')
        st.write(
            """
        - ✔️ 7 Years expereince extracting actionable insights from data
        - ✔️ Strong hands on experience and knowledge in Python and Excel
        - ✔️ Good understanding of statistical principles and their respective applications
        - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
        - ► Redesigned data model through iterations that improved predictions by 12%
        """
        )
with col2:
    st.image('images/bnym.PNG', use_column_width = 'auto')
with col3:
    st.image('images/prft.png', use_column_width = 'auto')

with col4:
    with st.expander("Innominds - Bangalore (August 2019 - June 2020)"):
        st.write(
            """
        - ✔️ 7 Years expereince extracting actionable insights from data
        - ✔️ Strong hands on experience and knowledge in Python and Excel
        - ✔️ Good understanding of statistical principles and their respective applications
        - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
        - ► Redesigned data model through iterations that improved predictions by 12%
        """
        )
with col5:
    st.image('images/innominds.PNG', use_column_width = 'auto')

    
st.markdown("---")
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

st.markdown("---")
st.subheader("📨 Contact Me")
st.write(info['Email'])
st.write("")
st.write(info['Phone'])
st.write("")
st.write(info['City'])
st.markdown("---")
