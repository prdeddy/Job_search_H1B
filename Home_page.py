import pandas as pd
import streamlit as st



## Load data for H1B approvals and sort it
raw_data = pd.read_csv('h1b_datahubexport-2022.csv')
sorted_data = raw_data.sort_values(by='Initial Approval',ascending=False)
cols = ['Employer','Initial Approval','Continuing Approval','City']
work_data = sorted_data.reset_index().loc[:,cols] #selecting required cols
work_data = work_data[work_data['Employer'].notna()]


st.set_page_config(
    page_title="H1B job_search",
    page_icon="💼",)

st.title("Chasing the H1B Unicorn: ")
st.caption("The Elusive Search for a Sponsor in the USA ")
st.write("Navigating the complex maze of H1B sponsorship requirements and competition "
         "can be a daunting task for job seekers hoping to work in the USA. Here are my two cents to help in this process")
st.header("How to use this")

st.sidebar.success('Select a tab above')
