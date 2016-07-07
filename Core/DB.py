import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps
import os

from Core.ExamScraper import scrape


DB_URI = os.environ.get('MONGODB_URI', None)
client = None
exams = None


if DB_URI:
    client = MongoClient(os.environ.get('MONGODB_URI'))
    db = client.get_default_database()
else:
    client = MongoClient()
    db = client.exams


print("-> INIT DB")
print("---> DB URI: " + str(DB_URI))
print()


all_exams = db.exams

# ################################################################################
# ##############################      UPDATE      ########################
# ################################################################################


def update_db():
    print("-> Updating Database")
    print("---> Deleted: " + str(db.exams.delete_many({}).deleted_count))

    exam_data = scrape()
    print("---> Scraping Generators")
    for i, course_page in enumerate(exam_data):
        toAdd = [exam_item.getDict() for exam_item in course_page]
        if toAdd:
            print("-----> " + str(len(toAdd)) + " entries added to class " +
                  toAdd[0]['course'])
            all_exams.insert_many(toAdd)

# ################################################################################
# ##############################      SEARCH      ################################
# ################################################################################


def search_class(query):
    print("-> Searching for Class: " + str(query))
    return dumps(list(all_exams.find({"course": query})))

def get_courses():
    # print(dumps(list(all_exams.find({}))))
    return list(all_exams.find({}).distinct("course"))

#
