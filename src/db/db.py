import pymongo
from pymongo import MongoClient


def getConnection() -> pymongo.collection.Collection:
    """
    Establishes a connection to the MongoDB cluster and returns the 'problem list' collection.

    Returns:
        pymongo.collection.Collection: The 'problem list' collection object.
    """
    cluster = MongoClient(
        "mongodb+srv://Admin:WMggmanEJgUxzBgZ@leetcodeextractorcluste.ujs631j.mongodb.net/?retryWrites=true&w=majority&appName=LeetcodeExtractorCluster"
    )

    db = cluster["LeetcodeExtractor"]

    collection = db["problem list"]
    return collection


def insert_problem_list_to_db(problem_list):
    """
    Inserts or updates a list of problems in the MongoDB collection.

    Args:
        problem_list (list): A list of problem objects to be inserted or updated.

    Returns:
        dict: A dictionary containing the number of inserted and updated problems.
    Raises:
        ValueError: If the problem_list is empty or None.
    """
    if (problem_list == None) or (len(problem_list) == 0):
        raise ValueError("problem_list is empty or None")
    collection = getConnection()
    insertCount = 0
    updateCount = 0
    for problem in problem_list:
        if collection.find_one({"_id": problem["_id"]}) is None:
            collection.insert_one(problem)
            insertCount += 1
        else:
            # update the problem if it already exists
            collection.update_one({"_id": problem["_id"]}, {"$set": problem})
            updateCount += 1
    return {"inserted": insertCount, "updated": updateCount}
