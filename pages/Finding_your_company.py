import streamlit as st
from H1B import work_data,find_jobs
st.title("Check if your prospect employer sponsored any H1Bs")
search = st.text_input("Enter the company in the below box")
title = st.text_input("Enter the job title you're looking for.. eg: analyst")
if st.button("submit"):
    if len(search) > 1:
        look = search.upper()
        st.subheader('Companies matching with ' + look)
        display_data = work_data[work_data['Employer'].str.contains(look)]
        display_data.reset_index(drop=True,inplace=True)
        st.dataframe(display_data)
        find_jobs(search,title)
