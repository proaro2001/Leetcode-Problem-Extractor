import time
# import the keys module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By # to search for things using specific parameters
from selenium.webdriver.common.keys import Keys # to use the enter key like Enter, ESC, etc.

# wait for the page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager # helps to avoid adding to PATH


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Link to the website we are searching
LINK = 'https://www.google.com'

# open the browser and visit the website
driver.get(LINK)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf')))

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.clear() # clear the input field, otherwise the text will be appended to the existing text

# same as input_element.send_keys('leetcode' + Keys.ENTER)
input_element.send_keys('leetcode')
input_element.send_keys(Keys.ENTER)


time.sleep(5)

# cloase the browser
driver.quit()