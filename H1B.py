import pandas as pd
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


raw_data = pd.read_csv('h1b_datahubexport-2022.csv')
sorted_data = raw_data.sort_values(by='Initial Approval',ascending=False)
cols = ['Employer','Initial Approval','Initial Denial','Continuing Approval','Continuing Denial','City']
work_data = sorted_data.reset_index().loc[:,cols] #selecting required cols
work_data = work_data[work_data['Employer'].notna()]


def find_jobs(comp,role) :
    driver = webdriver.Firefox()
    driver.get('https://www.google.com/')
    driver.implicitly_wait(30)
    driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(role + " job openings in " + comp + Keys.ENTER)
    try:
        temp = driver.find_element(By.CSS_SELECTOR, 'a[href*=";jobs&"]')
        link = temp.get_attribute('href')
        driver.get(link)
        driver.maximize_window()
        job_list = driver.find_elements(By.TAG_NAME, "li")
        if len(job_list) > 0:
            with st.container():
                st.subheader('Some of the jobs found')
                st.caption('Oopsie, looks like these jobs forgot to mention whether they offer H1B sponsorship')
                for job in job_list:
                    st.write(job.text + "\n")
        driver.quit()

    except:
        driver.get('https://www.indeed.com/jobs?q=' + comp + '+' + key_word)
        job_list = driver.find_elements(By.TAG_NAME, "li")
        jobs = []
        for job in job_list:
            try:
                jobs.append(job.text)
            except:
                continue
        st.subheader('Some of the jobs found')
        st.caption('Oopsie, looks like these jobs forgot to mention whether they offer H1B sponsorship')
        for job in jobs:
            if comp in job:
                with st.container():
                    st.write(job.text + "\n")
            else:
                continue
        driver.quit()


