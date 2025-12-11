from models import Student

class AuthenticationService:
    """
    Controller for Student-related operations:
    - sign up
    - login
    """

    def __init__(self):
        self.students = []  # in-memory list of Student

    def check_if_exists(self, student_id: str) -> bool:
        return any(s.student_id == student_id for s in self.students)

    def sign_up(self, student_id: str, name: str, password: str):
        if self.check_if_exists(student_id):
            return None, "Student ID already exists."

        new_student = Student(student_id, name, password)
        self.students.append(new_student)
        return new_student, "Sign-up success."

    def login(self, student_id: str, password: str):
        for s in self.students:
            if s.student_id == student_id and s.password == password:
                return s, "Login success."
        return None, "Invalid credentials."
