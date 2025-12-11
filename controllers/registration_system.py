from .authentication_service import AuthenticationService
from .course_catalog import CourseCatalog
from .registration_manager import RegistrationManager


class RegistrationSystem:
    """
    High-level controller (Facade):
    Coordinates AuthenticationService, CourseCatalog, RegistrationManager.
    UI only interacts with this class.
    """

    def __init__(self):
        self.auth_service = AuthenticationService()
        self.course_catalog = CourseCatalog()
        self.reg_manager = RegistrationManager()
        self.current_user = None  # currently logged-in Student

    # ---------- Student auth ----------
    def register_student(self, sid, name, pwd):
        return self.auth_service.sign_up(sid, name, pwd)

    def login(self, sid, pwd):
        stu, msg = self.auth_service.login(sid, pwd)
        if stu:
            self.current_user = stu
        return stu, msg

    def logout(self):
        self.current_user = None

    # ---------- Course operations ----------
    def get_all_courses(self):
        return self.course_catalog.get_all_courses()

    def get_course_details(self, cid):
        return self.course_catalog.find_course(cid)

    def register_course(self, cid):
        if not self.current_user:
            return False, "You must be logged in."
        c = self.course_catalog.find_course(cid)
        if not c:
            return False, "Course not found."
        return self.reg_manager.register(self.current_user, c)

    def drop_course(self, cid):
        if not self.current_user:
            return False, "You must be logged in."
        c = self.course_catalog.find_course(cid)
        if not c:
            return False, "Course not found."
        return self.reg_manager.drop(self.current_user, c)

    def get_my_schedule(self):
        if not self.current_user:
            return []
        return self.current_user.get_registered_courses()

    def get_current_user_credit_remaining(self):
        if not self.current_user:
            return None
        return self.current_user.credits_remaining()
