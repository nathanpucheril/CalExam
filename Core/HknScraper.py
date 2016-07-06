from lxml import html
import requests
from Core.utils import xpath_safe_assignment as safe_assign, ExamItem

HKN_BASE_CRAWL_URL = "https://hkn.eecs.berkeley.edu" #Contains the Course List


def scrape():
    page = requests.get(HKN_BASE_CRAWL_URL + "/exams")
    tree = html.fromstring(page.content)

    # with open("hknexams.html", "r") as f:
    #     page = f.read()
    # tree = html.fromstring(page)
    # print(tree)
    course_urls = tree.xpath('//*[@id="container"]/div/table/tbody/tr/td/a/@href')
    # print(course_urls)
    for course_url in course_urls:
        url_split = course_url.split("/")
        dept = url_split[-2].upper()
        course = " ".join(url_split[-2:]).lower()
        # scrape_course_page(dept, course, course_url)
        yield scrape_course_page(dept, course,  course_url)

    # rows = tree.xpath("//*[@id='exams']/tr")
    # print(rows)


def scrape_course_page(dept, course, course_url):

    # with open("hkncs3.html", "r") as f:
    #     page = f.read()
    # tree = html.fromstring(page)
    page = requests.get(HKN_BASE_CRAWL_URL + course_url)
    tree = html.fromstring(page.content)

    rows = tree.xpath("//*[@id='exams']/tr")

    exam_types = ["Midterm 1", "Midterm 2", "Midterm 3", "Final"]
    for i, exam_type in enumerate(exam_types): # for each mt
        i = i + 1 #zero indexing not for xpath
        for row in rows[1:]: # IGNORE FIRST ROW OF TABLE (HEADER) FIND BETTER WAY?
            prof = safe_assign(row, "td[2]/a/text()")
            year = safe_assign(row, "td[1]/text()")

            exam_file_loc = 3 + i #td [3 + i]
            exam_url = HKN_BASE_CRAWL_URL + safe_assign(row, "td[3]/a[1]/@href")
            sol_url = HKN_BASE_CRAWL_URL + safe_assign(row, "td[3]/a[2]/@href")
            # print(exam_url)
            yield ExamItem(dept, course, prof, year, exam_type, exam_url, sol_url)

# scrape()
