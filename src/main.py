from scraping.leetcode import extract_from_leetcode_page
from utils.leetcode_extractor import print_leetcode_info
from db.db import insert_problem_list_to_db, getCollection
from utils.humanBehavior import random_delay
import time


def main():
    start_time = time.time()
    # TODO: Figure out what the range should be
    # TODO: Instead of keep calling for each page, try to press the next button
    last_page = 64
    all_data = []

    db_collection = getCollection()
    try:
        for i in range(1, last_page + 1):
            print("=====================================")
            print(f"Extracting data from LeetCode page {i}...")
            data = extract_from_leetcode_page(i, headless=True)
            all_data.extend(data)
            print(f"Extracted {len(data)} problems from page {i}")
            random_delay(1, 5, True)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Inserting data into the database...")
        insert_problem_list_to_db(all_data, collection=db_collection)
        print("Data inserted into the database successfully!")
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
