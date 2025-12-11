class Course:
    def __init__(self, course_id: str, title: str,
                 instructor: str, credits: int, capacity: int):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.credits = credits
        self.capacity = capacity
        self.enrolled_students = []  # list of Student

    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.capacity

    def enroll_student(self, student) -> bool:
        if not self.is_full():
            self.enrolled_students.append(student)
            return True
        return False

    def remove_student(self, student) -> bool:
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            return True
        return False

    def __repr__(self) -> str:
        return f"Course({self.course_id}, {self.title})"
