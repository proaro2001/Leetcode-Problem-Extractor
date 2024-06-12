from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager # helps to avoid adding to PATH


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Link to the website we are searching
LINK = 'https://www.google.com'

# open the browser and visit the website
driver.get(LINK)

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')

# same as input_element.send_keys('leetcode' + Keys.ENTER)
input_element.send_keys('leetcode')
input_element.send_keys(Keys.ENTER)


time.sleep(5)

# cloase the browser
driver.quit()