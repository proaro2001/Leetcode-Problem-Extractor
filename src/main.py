from scraping.leetcode import extract_from_leetcode_page
from utils.leetcode_extractor import print_leetcode_info
from db.db import insert_problem_list_to_db, getCollection
import time


def main():
    start_time = time.time()
    # TODO: Figure out what the range should be
    # TODO: Instead of keep calling for each page, try to press the next button
    last_page = 64
    all_data = []

    db_collection = getCollection()

    for i in range(1, last_page + 1):
        print("=====================================")
        print(f"Extracting data from LeetCode page {i}...")
        data = extract_from_leetcode_page(i, headless=True)
        all_data.extend(data)
        print(f"Extracted {len(data)} problems from page {i}")

    print("Inserting data into the database...")
    updated_count, insert_count = insert_problem_list_to_db(
        all_data, collection=db_collection
    )
    print(
        f"Updated {updated_count} existing problems and inserted {insert_count} new problems into the database."
    )
    print("Data inserted into the database successfully!")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
