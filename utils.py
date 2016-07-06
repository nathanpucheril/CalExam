xpath_exists = lambda selector, xpath: selector.xpath("boolean(" + xpath + ")")


def xpath_safe_assignment(selector, xpath, assignment_prefix=""):
    return (assignment_prefix + selector.xpath(xpath)[0]).strip() if xpath_exists(selector, xpath) else "n/a"


class ExamItem(object):
    """docstring for ExamItem"""

    def __init__(self, dept, course, prof, yr, exam_type, exam_url, sol_url):
        super(ExamItem, self).__init__()
        self.dept = dept
        self.course = course
        self.prof = prof
        self.yr = yr
        self.exam_type = exam_type
        self.exam_url = exam_url
        self.sol_url = sol_url
        self.dict = {
            "dept": dept,
            "course": course,
            "professor(s)": prof,
            "term": yr,
            "examType": exam_type,
            "examUrl": exam_url,
            "solutionUrl": sol_url
        }

    def getDict(self):
        return self.dict
