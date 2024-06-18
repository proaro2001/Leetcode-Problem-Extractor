import os
import time
from dotenv import load_dotenv

# import the keys module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# to use the enter key like Enter, ESC, etc.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# helps to avoid adding to PATH
from webdriver_manager.chrome import ChromeDriverManager

# Bright Data
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
import os
from dotenv import load_dotenv

# Undetected_chromedriver
import undetected_chromedriver as uc


def get_driver(LINK, headless=True):
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


def get_BD_driver(LINK, headless=True):
    print("Connecting to Scraping Browser...")
    load_dotenv()
    SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    chrome_options = ChromeOptions()

    with Remote(sbr_connection, options=chrome_options) as driver:
        print(f"Connecting to {LINK}...")
        driver.get(LINK)
        print("Connected successfully!")
        time.sleep(5)
        driver.get_screenshot_as_file("screenshot.png")
        return driver


def get_undetected_driver(LINK, headless=True):
    options = uc.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.random
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome limited resource problems
    options.add_argument(f"user-agent={userAgent}")  # Set the user-agent
    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )  # Disable automation control which can be detected by websites
    options.add_argument("--disable-web-security")  # Disable web security
    options.add_argument("--disable-gpu")  # Disable GPU
    options.add_argument(
        "--disable-features=WebRTC"
    )  # Disable WebRTC, WebRTC is used for video calls

    driver = uc.Chrome(options=options, headless=headless)
    driver.get(LINK)
    time.sleep(5)
    print("Link opened successfully! Printing the screenshot...")
    driver.get_screenshot_as_file("screenshot.png")
    print("Screenshot printed successfully!")
    time.sleep(10)
    driver.get_screenshot_as_file("screenshot_10s.png")
    return driver
