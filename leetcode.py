# import the keys module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# to search for things using specific parameters
from selenium.webdriver.common.by import By

# to use the enter key like Enter, ESC, etc.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# wait for the page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# helps to avoid adding to PATH
from webdriver_manager.chrome import ChromeDriverManager
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

    SETTINGS_BUTTON_XPATH = '//*[@id="headlessui-popover-button-:r7:"]'
    SHOW_TAG_TOGGLE_XPATH = "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div/div[5]/div[2]/div/div[1]"
    ROW_GROUP_XPATH = (
        '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]'
    )
    ROWS_XPATH = '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]//div[@role="row"]'
    try:
        # Link to the website we are searching
        LINK = f"https://leetcode.com/problemset/?page={pageNum}"

        # open the browser and visit the website
        driver.get(LINK)

        # find and click on the settings button
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SETTINGS_BUTTON_XPATH))
        )
        settings_button = driver.find_element(By.XPATH, SETTINGS_BUTTON_XPATH)
        settings_button.click()

        # find and click on the show tag button
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    SHOW_TAG_TOGGLE_XPATH,
                )
            )
        )
        show_tag_toggle = driver.find_element(
            By.XPATH,
            SHOW_TAG_TOGGLE_XPATH,
        )
        show_tag_toggle.click()

        # find the div tag by role called rowgroup
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    ROW_GROUP_XPATH,
                )
            )
        )
        row_group = driver.find_element(
            By.XPATH,
            ROW_GROUP_XPATH,
        )
        rows = row_group.find_elements(
            By.XPATH,
            ROWS_XPATH,
        )

        # extract and print out the leetcode info
        for row in rows:
            extracted_leetcode_info = extract_leetcode_info(row.text)
            print_leetcode_info(extracted_leetcode_info)
        # output = [extract_leetcode_info(row.text) for row in rows]
        # return output

    except Exception as e:
        # handle the exception
        print(f"An error occurred: {str(e)}")
    finally:
        # code to be executed regardless of whether an exception occurred or not
        driver.quit()
