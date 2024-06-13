import pymongo
from pymongo import MongoClient


def getConnection() -> pymongo.collection.Collection:
    cluster = MongoClient(
        "mongodb+srv://Admin:WMggmanEJgUxzBgZ@leetcodeextractorcluste.ujs631j.mongodb.net/?retryWrites=true&w=majority&appName=LeetcodeExtractorCluster"
    )

    db = cluster["LeetcodeExtractor"]

    collection = db["problem list"]
    return collection


def insert_problem_list_to_db(problem_list):
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
