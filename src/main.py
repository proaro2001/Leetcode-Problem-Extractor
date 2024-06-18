from scraping.leetcode import extract_from_leetcode_page
from utils.leetcode_parser import print_leetcode_info
from db.db import insert_problem_list_to_db, getCollection
from scraping.scrapy_workflow import scrape_with_range, scrape_with_queue
import time

from queue import Queue
import threading as th


def main():

    # TODO: Figure out what the range should be
    # TODO: Instead of keep calling for each page, try to press the next button
    last_page = 64

    db_collection = getCollection()
    queue = Queue()
    # Add all pages to the queue
    for i in range(1, last_page + 1):
        queue.put(i)

    scrape_with_queue(queue, db_collection, headless=True)

    print("All pages have been scraped!")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
