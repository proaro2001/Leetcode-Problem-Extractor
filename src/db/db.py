import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from pymongo import InsertOne


def getCollection() -> pymongo.collection.Collection:
    """
    Establishes a connection to the MongoDB client and returns the 'problem list' collection.
    This function should be called before calling the insert_problem_list_to_db function.

    Returns:
        pymongo.collection.Collection: The 'problem list' collection object.
    """
    uri = "mongodb+srv://Admin:WMggmanEJgUxzBgZ@leetcodeextractorcluste.ujs631j.mongodb.net/?retryWrites=true&w=majority&appName=LeetcodeExtractorCluster"
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Connect to the 'LeetcodeExtractor' database and the 'problem list' collection
    try:
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
    if (problem_list == None) or (len(problem_list) == 0):
        raise ValueError("problem_list is empty or None")
    insertCount = 0
    updateCount = 0
    for problem in problem_list:
        if collection.find_one({"_id": problem["_id"]}) is None:
            collection.InsertOne(problem)
            insertCount += 1
        else:
            # update the problem if it already exists
            collection.update_one({"_id": problem["_id"]}, {"$set": problem})
            updateCount += 1
    return {"inserted": insertCount, "updated": updateCount}
