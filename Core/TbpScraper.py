from lxml import html
import requests
from Core.utils import xpath_safe_assignment as safe_assign, ExamItem

TBP_BASE_CRAWL_URL = "https://tbp.berkeley.edu" #Contains the departments


def scrape():

    page = requests.get(TBP_BASE_CRAWL_URL + "/courses")
    tree = html.fromstring(page.content)

    # with open("tbpdepts.html", "r") as f:
    #     page = f.read()
    # tree = html.fromstring(page)
    # print(tree)
    dept_urls = tree.xpath('//*[@id="content"]/ul/li/a/@href')
    for dept_url in dept_urls:
        dept_page = requests.get(TBP_BASE_CRAWL_URL + dept_url)
        # print(TBP_BASE_CRAWL_URL + dept_url)
        dept_tree = html.fromstring(dept_page.content)
        # with open("tbpdept.html", "r") as f:
        #     dept_page = f.read()
        # dept_tree = html.fromstring(dept_page)
        course_urls = dept_tree.xpath('//*[@id="content"]/ul/li/a/@href')
        for course_url in course_urls:
            url_split = course_url.split("/")
            dept = url_split[-3].upper()
            course = " ".join(url_split[-3:]).lower().strip()
            yield scrape_course_page(dept, course, course_url)


def scrape_course_page(dept, course, course_url):

    # with open("tbpcs61a.html", "r") as f:
    #     page = f.read()
    # tree = html.fromstring(page)
    page = requests.get(TBP_BASE_CRAWL_URL + course_url)
    tree = html.fromstring(page.content)

    rows = tree.xpath("//*[@id='content']/table[1]/tbody/tr")

    # print(TBP_BASE_CRAWL_URL + course_url)
    for row in rows:
        prof = safe_assign(row, "td[1]/a/text()")
        exam_type = safe_assign(row, "td[2]/text()")
        year = safe_assign(row, "td[3]/text()")
        exam_url = TBP_BASE_CRAWL_URL + safe_assign(row, "td[4]/a/@href")
        sol_url = TBP_BASE_CRAWL_URL + safe_assign(row, "td[5]/a/@href")


        # print(ExamItem(dept, course, prof, year, exam_type, exam_url, sol_url).getDict())
        yield ExamItem(dept, course, prof, year, exam_type, exam_url, sol_url)

# print(list(scrape_course_page("CS 61A", "")))]
