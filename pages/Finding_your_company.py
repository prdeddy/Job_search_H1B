import streamlit as st
from Home_page import work_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os, sys

def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

def find_jobs(comp,role) :
    _ = installff()
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
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
                st.caption('Opsie, looks like these jobs forgot to mention whether they offer H1B sponsorship')
                st.write(f"check the jobs   [click]({link})")
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
        st.write(f"check the jobs   [click]({link})")
        for job in jobs:
            if comp in job:
                with st.container():
                    st.write(job.text + "\n")
            else:
                continue
        driver.quit()

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
