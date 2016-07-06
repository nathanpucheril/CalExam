import pymongo
import ExamScraper
from pymongo import MongoClient
#
client = MongoClient()
#
exam_db = client.exam_db
#
all_exams = exam_db.all_exams
#
#
# print(exams)
# a = all_exams.find_one({"dept": "CS"})
# print(a)
#
# ################################################################################
# ############################      EXAM DATA      ###############################
# ################################################################################
exam_data = ExamScraper.scrape()


for i, course_page in enumerate(exam_data):
    toAdd = [exam_item.getDict() for exam_item in course_page]
    if toAdd:
        print(str(len(toAdd)) + " entries added to class " + toAdd[0]['course'] )
        all_exams.insert_many(toAdd)
#
