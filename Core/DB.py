import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps

import Core.ExamScraper


DEPLOY = False

if DEPLOY:
    client = None
else:
    client = MongoClient()


exam_db = client.exam_db
all_exams = exam_db.all_exams

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
