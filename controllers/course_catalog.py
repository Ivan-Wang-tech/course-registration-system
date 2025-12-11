from models import Course

class CourseCatalog:
    """
    Controller for course-related operations:
    - add courses
    - list courses
    - find course by ID
    """

    def __init__(self):
        self.courses = []  # list of Course

    def add_course(self, c: Course):
        self.courses.append(c)

    def get_all_courses(self):
        return self.courses

    def find_course(self, cid: str):
        for c in self.courses:
            if c.course_id == cid:
                return c
        return None
