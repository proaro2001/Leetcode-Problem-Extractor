# import the keys module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By # to search for things using specific parameters
from selenium.webdriver.common.keys import Keys # to use the enter key like Enter, ESC, etc.
from selenium.webdriver.chrome.options import Options

# wait for the page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager # helps to avoid adding to PATH
from util import extract_leetcode_info, print_leetcode_info

def extract_from_leetcode_page(pageNum):
    """
    Extracts and prints out the LeetCode information from a specific page.

    Args:
        pageNum (int): The page number to extract information from.

    Returns:
        None
    """
    # some necessary variables
    # options = Options()
    # options.headless = True # headless means without a UI
    service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(service=service)
    
    try:
        # Link to the website we are searching
        LINK = f'https://leetcode.com/problemset/?page={pageNum}'

        # open the browser and visit the website
        driver.get(LINK)

        # find and click on the settings button
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="headlessui-popover-button-:r7:"]'
        )))
        settings_button = driver.find_element(By.XPATH, '//*[@id="headlessui-popover-button-:r7:"]')
        settings_button.click()

        # find and click on the show tag button
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, '/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div/div[5]/div[2]/div/div[1]'
        )))
        show_tag_toggle = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div/div[5]/div[2]/div/div[1]')
        show_tag_toggle.click()

        # find the div tag by role called rowgroup
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]'
        )))
        row_group = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]')
        rows = row_group.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]//div[@role="row"]')
        
        # extract and print out the leetcode info
        for row in rows:
            extracted_leetcode_info = extract_leetcode_info(row.text)
            print_leetcode_info(extracted_leetcode_info)

    except Exception as e:
        # handle the exception
        print(f"An error occurred: {str(e)}")
    finally:
        # code to be executed regardless of whether an exception occurred or not
        driver.quit()