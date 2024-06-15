from scraping.leetcode import extract_from_leetcode_page
from utils.leetcode_extractor import print_leetcode_info
from db.db import insert_problem_list_to_db, getCollection
from utils.humanBehavior import random_delay
import time


def main():
    # TODO: Figure out what the range should be
    last_page = 64

    db_collection = getCollection()
    for i in range(1, last_page + 1):
        print("=====================================")
        print(f"Extracting data from LeetCode page {i}...")
        page1 = extract_from_leetcode_page(i)
        print("Inserting data into the database")
        insert_problem_list_to_db(page1, collection=db_collection)
        print(f"Data in page{i} inserted successfully!")
        random_delay(0, 2, True)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
