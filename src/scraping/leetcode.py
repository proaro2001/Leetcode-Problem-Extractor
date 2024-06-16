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

from utils.humanBehavior import random_delay
from utils.leetcode_extractor import extract_leetcode_info
from fake_useragent import UserAgent


def extract_from_leetcode_page(pageNum, headless=True):
    """
    Extracts Leetcode problems information from a specific page number.

    Args:
        pageNum (int): The page number to extract information from.

    Returns:
        list: A list of dictionaries containing the extracted information.
    """

    # Link to the website we are searching
    LINK = f"https://leetcode.com/problemset/?page={pageNum}"

    # driver that gets the page
    driver = get_driver(LINK, headless=headless)

    # Extract the rows from the page
    rows = extract_rows(driver)

    # output data List object
    output = [extract_leetcode_info(row.text) for row in rows]
    assert output is not None, "Error in Leetcode: No data found"

    # wait for a random time before closing the browser
    random_delay(2, 5, True)
    # close the browser
    driver.quit()
    return output


def get_driver(LINK, headless=True):
    """
    Initializes and returns a Chrome WebDriver instance with the specified options.

    Parameters:
        LINK (str): The URL to navigate to after initializing the driver.
        headless (bool): Whether to run Chrome in headless mode. Defaults to True.

    Returns:
        WebDriver: The initialized Chrome WebDriver instance.
    """
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    if headless:
        options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"user-agent={userAgent}")

    # Set up Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(LINK)
    return driver


def extract_rows(driver):
    """
    Extracts rows from a web page using the provided Selenium WebDriver.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        A list of WebElement objects representing the extracted rows.
    """
    SETTINGS_BUTTON_XPATH = '//*[@id="headlessui-popover-button-:r7:"]'
    SHOW_TAG_TOGGLE_XPATH = "/html/body/div[1]/div[1]/div[4]/div[2]/div[1]/div[4]/div[1]/div/div[5]/div[2]/div/div[1]"
    ROW_GROUP_XPATH = (
        '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]'
    )
    ROWS_XPATH = '//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]//div[@role="row"]'

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

    # find all the rows in the row group
    rows = row_group.find_elements(
        By.XPATH,
        ROWS_XPATH,
    )

    return rows


# TODO: Create a function to extract the output data from the rows extracted by the previous function
