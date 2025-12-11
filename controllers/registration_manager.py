from models import Student, Course


class RegistrationManager:
    """
    Controller for registration operations:
    - register
    - drop
    - enforce business rules (duplicate, capacity, credit limit)
    """

    def check_duplicate(self, student: Student, course: Course) -> bool:
        return course in student.registered_courses

    def check_capacity(self, course: Course) -> bool:
        return not course.is_full()

    def check_credit_limit(self, student: Student, course: Course) -> bool:
        return student.total_credits() + course.credits <= Student.MAX_CREDITS

    def register(self, student: Student, course: Course):
        if self.check_duplicate(student, course):
            return False, "Already registered."

        if not self.check_capacity(course):
            return False, "Course is full."

        if not self.check_credit_limit(student, course):
            return False, "You have exceeded the maximum credits for the semester."

        student.registered_courses.append(course)
        course.enroll_student(student)

        remaining = student.credits_remaining()
        return True, f"Registration successful. Credits remaining: {remaining}."

    def drop(self, student: Student, course: Course):
        if course not in student.registered_courses:
            return False, "You are not enrolled in this course."

        student.registered_courses.remove(course)
        course.remove_student(student)

        remaining = student.credits_remaining()
        return True, f"Course dropped. Credits remaining: {remaining}."
