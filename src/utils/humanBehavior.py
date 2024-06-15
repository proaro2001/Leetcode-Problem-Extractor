import time
import random


# Function to introduce a random delay
def random_delay(min_time=0, max_time=5, usePrint=True):
    delay_time = random.uniform(min_time, max_time)
    if usePrint:
        print(f"Random delay for {delay_time} seconds")
    time.sleep(delay_time)


# Function to scroll the webpage
def human_scroll(driver, scroll_height):
    for i in range(0, scroll_height, 20):
        driver.execute_script(f"window.scrollTo(0, {i});")
        if random.choice([0, 1, 2, 3, 4]) == 1:
            random_delay(0, 0.02, False)
    print("Scrolling done")
    random_delay(0.1, 2)


# Function to get the total height of the webpage
def get_page_height(driver):
    return driver.execute_script("return document.body.scrollHeight")
