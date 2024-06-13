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
    options = Options()
    # options.headless = True  # headless means without a UI
    # options.add_argument("--headless")  # Run Chrome in headless mode
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(service=service)

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
    rows = row_group.find_elements(
        By.XPATH,
        ROWS_XPATH,
    )
    assert rows is not None, "Error in Leetcode: Rows not found"

    time.sleep(2)

    output = [extract_leetcode_info(row.text) for row in rows]
    assert output is not None, "Error in Leetcode: No data found"
    driver.quit()
    return output
