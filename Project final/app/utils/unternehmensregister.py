from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy import Selector
from googletrans import Translator
import pandas as pd
import os
import time

# Function to initialize Selenium and get page source
def get_html(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html


def get_info():
    return 0

def convert_to_df():
    return 0



def save_to_excel_unternehmensregister():
    
    return 0 

def unter(keywords,others):
    base_url = ""
    all_data = pd.DataFrame()

    while True:
        url = base_url.format(keywords, others)
        html = get_html(url)
        selector = Selector(text=html)
        infos = get_info(selector)
        df = convert_to_df(infos)
        all_data = pd.concat([all_data, df], ignore_index=True)
        
        
    return all_data
