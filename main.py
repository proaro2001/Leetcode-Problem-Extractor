from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager # helps to avoid adding to PATH


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Link to the website we are searching
LINK = 'https://www.google.com'

# open the browser and visit the website
driver.get(LINK)

time.sleep(5)

# cloase the browser
driver.quit()