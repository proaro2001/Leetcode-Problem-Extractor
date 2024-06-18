import time
from db.db import insert_problem_list_to_db, getCollection
from scraping.leetcode import extract_from_leetcode_page
from utils.humanBehavior import random_delay


def scrape_with_queue(queue=None, db_collection=None, headless=True):
    if queue is None or db_collection is None:
        raise ValueError("queue and db_collection, must be provided")

    error_count = 0
    while not queue.empty() and error_count < 20:
        try:
            i = queue.get()
            print("=====================================")
            print(f"Extracting data from LeetCode page {i}...")
            data = extract_from_leetcode_page(i, headless=headless)
            print(f"Inserting data into the database...")
            count = insert_problem_list_to_db(data, collection=db_collection)
            print(count)
            # random_delay(2 + error_count / 10, 5 + error_count, True)

        except Exception as e:
            print(f"Error: {e}")
            queue.put(i)
            error_count += 1
            print(f"Error count: {error_count}")
            print(f"Pushed page number {i} back to the queue")
