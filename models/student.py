class Student:
    MAX_CREDITS = 16

    def __init__(self, student_id: str, name: str, password: str):
        self.student_id = student_id
        self.name = name
        self.password = password
        self.registered_courses = []  # list of Course

    def get_registered_courses(self):
        return self.registered_courses

    def total_credits(self) -> int:
        return sum(c.credits for c in self.registered_courses)

    def credits_remaining(self) -> int:
        return Student.MAX_CREDITS - self.total_credits()

    def __repr__(self) -> str:
        return f"Student({self.student_id}, {self.name})"
