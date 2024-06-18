from db.db import getCollection
from scraping.scrapy_workflow import scrape_with_queue
import time

from queue import Queue


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
