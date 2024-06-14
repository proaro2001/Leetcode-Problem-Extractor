import time

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

from utils.leetcode_extractor import extract_leetcode_info

from fake_useragent import UserAgent


def extract_from_leetcode_page(pageNum):
    """
    Extracts Leetcode problems information from a specific page number.

    Args:
        pageNum (int): The page number to extract information from.

    Returns:
        list: A list of dictionaries containing the extracted information.
    """
    # Set Chrome options
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f"user-agent={userAgent}")
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")

    # Set up Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    SETTINGS_BUTTON_XPATH = '//*[@id="headlessui-popover-button-:r7:"]'
    SHOW_TAG_TOGGLE_XPATH = "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div/div[5]/div[2]/div/div[1]"
    ROW_GROUP_XPATH = (
        '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]'
    )
    ROWS_XPATH = '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]//div[@role="row"]'

    # Link to the website we are searching
    LINK = f"https://leetcode.com/problemset/?page={pageNum}"

    # open the browser and visit the website
    driver.get(LINK)

    # implicitly wait for 10 seconds
    driver.implicitly_wait(10)

    # find and click on the settings button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, SETTINGS_BUTTON_XPATH))
    )
    settings_button = driver.find_element(By.XPATH, SETTINGS_BUTTON_XPATH)
    assert settings_button is not None, "Error in Leetcode: Settings button not found"
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
    assert (
        show_tag_toggle is not None
    ), "Error in Leetcode: Show tag toggle button not found"
    show_tag_toggle.click()

    # Indicator that the show tag button was clicked, can be removed for performance purposes
    print("Show tag button clicked")

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
    assert row_group is not None, "Error in Leetcode: Row group not found"

    # find all the rows in the row group
    rows = row_group.find_elements(
        By.XPATH,
        ROWS_XPATH,
    )
    assert rows is not None, "Error in Leetcode: Rows not found"

    # wait for 2 seconds to allow the page to load and prevent crashing the program and browser
    time.sleep(2)

    # output data List object
    output = [extract_leetcode_info(row.text) for row in rows]
    assert output is not None, "Error in Leetcode: No data found"

    # close the browser
    driver.quit()
    return output


# TODO: Create a getDriver to return the driver object
# The driver object should be quit by the user once user is done with it

# TODO: Create a function to extract the targeted information from the leetcode page
# the rows to be specific

# TODO: Create a function to extract the output data from the rows extracted by the previous function
