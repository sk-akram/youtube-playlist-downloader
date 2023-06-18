from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os



opt = Options()
chrome_driver_path = 'C:\Development\chromedriver.exe'

service = Service(executable_path=chrome_driver_path)
opt.add_experimental_option("debuggerAddress", "localhost:8080")
driver = webdriver.Chrome(options=opt)

driver.get('https://yt1s.com/')



data = pd.read_csv('anchors.csv')
data = pd.read_csv('anchors.csv')
links = [d for d in data['Link']]

unsuccess = set()
success = set()

def dothings(links1):
    if not links1:
        return

    for link in links1:
        if link in success:
            continue

        try:
            search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="s_input"]')))
            search_input.send_keys(link)
            search_input.send_keys(Keys.ENTER)

            getLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-action"]')))
            getLink.click()

            download_vid = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="asuccess"]')))
            download_vid.click()

            success.add(link)

            convert_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cnext"]')))
            convert_next.click()
        except Exception as e:
            unsuccess.add(link)
    
    links1 = unsuccess.copy()
    unsuccess.clear()
    dothings(links1)

dothings(links)

if os.path.exists('anchors.csv'):
    os.remove('anchors.csv')
    print("Deleted anchors.csv")
else:
    print("anchors.csv does not exist")
