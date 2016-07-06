import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps
import os

import Core.ExamScraper



DB_URI = os.environ.get('MONGODB_URI',None)
client = None
exams = None

if DB_URI:
    client = MongoClient(os.environ.get('MONGODB_URI'))
else:
    client = MongoClient()


exams = client.exams
all_exams = exams.all_exams

# ################################################################################
# ##############################      UPDATE      ################################
# ################################################################################
def update_db():
    exam_data = ExamScraper.scrape()


    for i, course_page in enumerate(exam_data):
        toAdd = [exam_item.getDict() for exam_item in course_page]
        if toAdd:
            print(str(len(toAdd)) + " entries added to class " + toAdd[0]['course'] )
            all_exams.insert_many(toAdd)

# ################################################################################
# ##############################      SEARCH##     ###############################
# ################################################################################
def search_class(query):
    return dumps(list(all_exams.find({"course": query})))

#
