import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from pymongo import InsertOne, UpdateOne

# from dotenv import load_dotenv # this is for local development
import os


def getCollection() -> pymongo.collection.Collection:
    """
    Establishes a connection to the MongoDB client and returns the 'problem list' collection.
    This function should be called before calling the insert_problem_list_to_db function.

    Returns:
        pymongo.collection.Collection: The 'problem list' collection object.
    """
    # load_dotenv() # this is for local development
    uri = os.getenv("MONGODB_URI")
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    try:
        # Try to connect to the MongoDB client
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")

        # Connect to the 'LeetcodeExtractor' database and the 'problem list' collection
        db = client["LeetcodeExtractor"]
        collection = db["problem list"]
        return collection
    except ServerSelectionTimeoutError as e:
        print("Error: Could not connect to the MongoDB client")
        print(e)
        return None


def insert_problem_list_to_db(problem_list, collection):
    """
    Inserts or updates a list of problems in the MongoDB collection.
    User should call getConnection() before calling this function.

    Args:
        problem_list (list): A list of problem objects to be inserted or updated.

    Returns:
        dict: A dictionary containing the number of inserted and updated problems.
    Raises:
        ValueError: If the problem_list is empty or None.
    """

    if not problem_list:
        raise ValueError("problem_list is empty or None")

    operations = []
    insert_count = 0
    update_count = 0

    for problem in problem_list:
        if collection.find_one({"_id": problem["_id"]}) is None:
            # Add InsertOne operation
            operations.append(InsertOne(problem))
            insert_count += 1
        elif collection.find_one({"_id": problem["_id"]}) != problem:
            # Add UpdateOne operation
            operations.append(UpdateOne({"_id": problem["_id"]}, {"$set": problem}))
            update_count += 1
        # If the problem is already in the collection and nothing changed, do nothing

    if operations:
        collection.bulk_write(operations)
        return {"inserted": insert_count, "updated": update_count}
    else:
        return {"inserted": 0, "updated": 0}
