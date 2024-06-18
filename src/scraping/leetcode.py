# to search for things using specific parameters
from selenium.webdriver.common.by import By

# wait for the page to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.humanBehavior import random_delay
from utils.leetcode_parser import parse_leetcode_info

from scraping.driver import get_driver


def extract_from_leetcode_page(pageNum, headless=True):
    # Link to the website we are searching
    LINK = f"https://leetcode.com/problemset/?page={pageNum}"

    # driver that gets the page
    driver = get_driver(LINK, headless=headless)

    # Extract the rows from the page
    rows = extract_rows(driver)

    # output data List object
    output = [parse_leetcode_info(row.text) for row in rows]
    assert output is not None, "Error in Leetcode: No data found"

    # wait for a random time before closing the browser
    random_delay(2, 5, True)
    # close the browser
    driver.quit()
    return output


def extract_rows(driver):
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
    print("Settings button clicked")

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
