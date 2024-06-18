import time
from queue import Queue
from db.db import insert_problem_list_to_db, getCollection
from scraping.leetcode import extract_from_leetcode_page


def scrape_with_range(db_collection, last_page, headless=True):
    for i in range(1, last_page + 1):
        start_time = time.time()
        print("=====================================")
        print(f"Extracting data from LeetCode page {i}...")
        data = extract_from_leetcode_page(i, headless=headless)
        print("Inserting data into the database...")
        count = insert_problem_list_to_db(data, collection=db_collection)
        print(count)
        print("Data inserted into the database successfully!")

        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")


def scrape_with_queue(queue=None, db_collection=None, headless=True):
    if queue is None or db_collection is None:
        raise ValueError("queue and db_collection, must be provided")

    while not queue.empty():
        try:
            i = queue.get()
            print("=====================================")
            print(f"Extracting data from LeetCode page {i}...")
            data = extract_from_leetcode_page(i, headless=headless)
            print(f"Inserting data into the database...")
            count = insert_problem_list_to_db(data, collection=db_collection)
            print(count)
            print(f"Data inserted into the database successfully!")

        except Exception as e:
            print(f"Error: {e}")
            queue.put(i)
            print(f"Pushed page number {i} back to the queue")
