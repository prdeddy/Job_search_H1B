import streamlit as st
from Home_page import work_data
st.title("Top companies which sponsored H1bs in 2022")
st.caption("Explore top H1B sponsors ")
n = st.number_input("Enter the number of comapanies you want to look at eg : 10 ",min_value=1)
if st.button("submit"):
    st.dataframe(work_data.head(n))



