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
st.write(":violet[Hello! I'm an Eager learner with a strong interest in Artificial Intelligence and Machine Learning. Enthusiastic about diving into the field and gaining real-time experience with Phenomenal learning models like Bigram, GPTs and Deep Learning. Ready to contribute to innovative projects and eager to expand knowledge through dedicated learning and collaboration with experts in the field!]")

with col2:
    st.image('images/profile.PNG', use_column_width = 'auto')

st.info("[Click Here to Chat about me](https://askmeaboutharish.streamlit.app/) !", icon="🤖")

st.subheader("📊:rainbow[Technical Intivatives]", divider='rainbow')
col20,col21 = st.columns([1,1])
with col20:
    st.write(
            """
        - Introduced a strategic initiative to **_Automate Quality Assurance_** tasks, resulting in a notable boost in overall employee productivity by saving 6-7 hours of work per week.
        - Led the development of a Semantic Search Engine utilizing advanced **_BERT/NLTK models_**, leveraging the Bank's Confluence knowledge base to streamline the retrieval of pertinent documentation.
        - Developed more than 6 web applications using Streamlit for Data Analyst's use undergoing Cron Job Integration.        
        """
        )
with col21:
    st.write(
            """
        - Single-handedly spearheading the development of a ChatBot for the data team, harnessing the power of the **_GPT 3.5 Turbo model_**. This initiative aims to empower customers to save time and enhance their knowledge autonomously, without the need for direct assistance from others.
        - Created **_Data Catalogs_** across all the databases in the Bank for analytic purposes such high memory consumptions, processing speed of queries, etc.
        """
        )

st.markdown("<p style = 'text-align:center;'><b>Created a personalized ChatBot, designed to answer questions about me! This innovative project involves training the ChatBot with my very own custom knowledge base, incorporating the powerful capabilities of GPT 3.5 Turbo and LlamaIndex, The links is above!</b></p>", unsafe_allow_html = True)

st.subheader("💼:rainbow[Professional Experience]", divider='rainbow')
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

st.subheader("📚:rainbow[Education]", divider='rainbow')
col18, col28 = st.columns([1,1])
with col18:
    st.write("**National College of Ireland - M.S in Data Analytics**")
    st.write("2015-2016")
with col28:
    st.write("**Jaya Engineering College - BE. Electronics and Telecommunication**")
    st.write("2011-2015")

with st.container():
    st.subheader("⚒️:rainbow[Skills]", divider='rainbow')
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

st.subheader(":rainbow[Other Activities]", divider='rainbow')
st.write(" - Currently Developing a AI model for use of Solar Irradiance Prediction, Fault Diagnosis and Troubleshooting of Solar Power Systems.")
st.write(" - Taken Initivative to find parameters that impacts Nifty 50 by performing sentiment analysis using X with open/close points and cross comparing the performance in realtime.")

st.subheader("📨:rainbow[Contact Me]", divider='rainbow')
st.write(info['Email'])
st.write(info['Phone'])
st.write(info['City'])

st.subheader(" ", divider='rainbow')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
