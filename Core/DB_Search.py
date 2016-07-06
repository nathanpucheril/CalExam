import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps
#
client = MongoClient()
#
exam_db = client.exam_db
#
all_exams = exam_db.all_exams


def search_class(query):
    return dumps(list(all_exams.find({"course": query})))

    # print("found")
    # return all_exams.find({"course": query})
