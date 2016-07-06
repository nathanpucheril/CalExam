from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

URL = "https://tbp.berkeley.edu/courses"

html = urlopen(URL)
soup = bs(html, "lxml")
a = soup.find("a", string="Computer Science")
print(a)


URL2 = "https://hkn.eecs.berkeley.edu/exams/"
html = urlopen(URL2)
soup = bs(html, "lxml")
a = soup.find_all("div", class_="exam_table")
b = a[1].next_sibling

print(b)
