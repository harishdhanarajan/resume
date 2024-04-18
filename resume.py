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
st.subheader("Technical Intivatives")
col20,col21 = st.columns([1,1])
with col20:
    st.write(
            """
        - ✔️ Increased the productivity of employees by **_Automating QA_** tasks that saves 6-7 hours of work per week.
        - ✔️ Developed Semantic Search Engine using **_BERT/NLTK model_** using Confluence knowledge base of the Bank to find relevant documentations.
        - ✔️ Developed more than 6 web applications using Streamlit for Data Teams own use that are ready for Deployment (Cron Job).        
        """
        )
with col21:
    st.write(
            """
        - ✔️ Currently developing a ChatBot for the data-team using **_GPT 3.5 Turbo model_** that will help the customers save time and gain better knowledge without our assitance.
        - ✔️ Created **_Data Catalogs_** using Streamlit (Python) across all the databases in the Bank for analytic purposes such high memory consumptions, processing speed of queries, etc.
        """
        )
    

st.markdown("---")
st.subheader("Experience & Qualification")
col1, col2, col3 = st.columns([4,0.5,0.5])
col4, col5, col6 = st.columns([4,0.5,0.5])
col7, col8, col9 = st.columns([4,0.5,0.5])
with col1:
    with st.expander("Bank of New York Mellon as Senior Technical Consultant (June 2020 - Present)"):
        col10, col11, col12 = st.columns([0.25,4,0.5])
        with col11:
            st.image('images/bnym_jd.png', width = 750)

with col2:
    st.image('images/bnym.PNG', use_column_width = 'auto')
with col3:
    st.image('images/prft.png', use_column_width = 'auto')

with col4:
    with st.expander("Innominds - Bangalore as Junior Machine Learning Engineer (August 2019 - June 2020)"):
        st.write(
            """
        - ✔️ Proficient in diverse machine learning algorithms, specializing in deep learning and ensemble methods.
        - ✔️ Skilled in data preprocessing techniques, feature engineering, and thorough model evaluation to ensure optimal performance
        - ✔️ Redesigned data model through iterations that improved predictions by 54%
        - ✔️ Demonstrated ability to deploy machine learning models effectively in production environments, ensuring seamless integration with existing systems.
        - ✔️ Frequently communicated with non-technical stakeholders directly
        """
        )
with col5:
    st.image('images/innominds.PNG', use_column_width = 'auto')
with col7:
    with st.expander("EIR - Ireland as Reporting Analyst (August 2016 - June 2019)"):
        st.write(
            """
        - ✔️ Presented Forecasting Ideas for Dashboard
        - ✔️ PowerBI Dashboard Maintenance
        - ✔️ Integration of Python with PowerBI Dev.
        - ✔️ Proactively involved in database management
        """
        )
with col8:
    st.image('images/eir.png', use_column_width = 'auto')
with col9:
    st.image('images/hcl.png', use_column_width = 'auto')
    
    

    
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
st.subheader("Other Activities")
st.write(" - Currently Developing a AI model for use of Solar Irradiance Prediction, Fault Diagnosis and Troubleshooting of Solar Power Systems")
st.write(" - Taken Initivative to find parameters that impacts Nifty 50 by performing sentiment analysis using X with open/close points and cross comparing the performance in realtime")

st.markdown("---")
st.subheader("📨 Contact Me")
st.write(info['Email'])
st.write(info['Phone'])
st.write(info['City'])
st.markdown("---")
