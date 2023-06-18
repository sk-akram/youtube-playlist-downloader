from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
from selenium.webdriver.chrome.options import Options


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# chrome_options.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service,options=chrome_options)

chrome_driver_path = 'C:\Development\chromedriver.exe'
opt = Options()

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=opt)

driver.get('https://www.youtube.com/playlist?list=PLnJ9JNvWu7J93useefWQItMIeAi1d4MDc')

data = []
a_tags = driver.find_elements("css selector", "a#video-title")
for a_tag in a_tags:
    href = a_tag.get_attribute("href")
    text = a_tag.text
    print(f"Link: {href}, Text: {text}")
    data.append((href, text))

csv_file = "anchors.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Link", "Text"])  # Write the header row
    writer.writerows(data) 


driver.quit()