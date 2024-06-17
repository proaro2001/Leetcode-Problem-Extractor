from scraping.leetcode import extract_from_leetcode_page
from utils.leetcode_parser import print_leetcode_info
from db.db import insert_problem_list_to_db, getCollection
import time

from queue import Queue


def main():

    # TODO: Figure out what the range should be
    # TODO: Instead of keep calling for each page, try to press the next button
    last_page = 64

    db_collection = getCollection()
    # scrape_with_range(db_collection, last_page)
    scrape_with_queue(db_collection, last_page)


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


def scrape_with_queue(db_collection, last_page, headless=True):
    queue = Queue()

    for i in range(1, last_page + 1):
        queue.put(i)

    while not queue.empty():
        try:
            i = queue.get()
            print("=====================================")
            print(f"Extracting data from LeetCode page {i}...")
            data = extract_from_leetcode_page(i, headless=headless)
            print("Inserting data into the database...")
            count = insert_problem_list_to_db(data, collection=db_collection)
            print(count)
            print("Data inserted into the database successfully!")

        except Exception as e:
            print(f"Error: {e}")
            queue.put(i)
            print(f"Pushed page number {i} back to the queue")

    print("All pages have been scraped!")


if __name__ == "__main__":
    main()
