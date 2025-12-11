from models import Course
from controllers import RegistrationSystem


def seed_courses(system: RegistrationSystem):
    # Computer Science-ish courses
    system.course_catalog.add_course(Course("CSCI-UA 101", "Intro to Computer Science", "Prof. Smith", 4, 50))
    system.course_catalog.add_course(Course("CSCI-UA 102", "Data Structures", "Prof. Allen", 4, 45))
    system.course_catalog.add_course(Course("CSCI-UA 201", "Computer Systems Organization", "Prof. Lee", 4, 40))
    system.course_catalog.add_course(Course("CSCI-UA 202", "Operating Systems", "Prof. Kumar", 4, 35))
    system.course_catalog.add_course(Course("CSCI-UA 310", "Basic Algorithms", "Prof. Chen", 4, 40))
    system.course_catalog.add_course(Course("CSCI-UA 321", "Programming Languages", "Prof. Davis", 4, 30))
    system.course_catalog.add_course(Course("CSCI-UA 330", "Databases", "Prof. Martinez", 4, 35))
    system.course_catalog.add_course(Course("CSCI-UA 340", "Computer Networks", "Prof. Nguyen", 4, 35))
    system.course_catalog.add_course(Course("CSCI-UA 350", "Software Engineering", "Prof. Patel", 4, 40))
    system.course_catalog.add_course(Course("CSCI-UA 360", "Machine Learning", "Prof. Zhao", 4, 30))
    system.course_catalog.add_course(Course("CSCI-UA 370", "Artificial Intelligence", "Prof. Roberts", 4, 30))
    system.course_catalog.add_course(Course("CSCI-UA 380", "Computer Graphics", "Prof. Thompson", 4, 30))
    system.course_catalog.add_course(Course("CSCI-UA 390", "Theory of Computation", "Prof. Gupta", 4, 25))
    system.course_catalog.add_course(Course("CSCI-UA 400", "Numerical Computing", "Prof. O'Brien", 4, 30))
    system.course_catalog.add_course(Course("CSCI-UA 410", "Parallel Computing", "Prof. Yang", 4, 30))

    # Mathematics
    system.course_catalog.add_course(Course("MATH-UA 121", "Calculus I", "Prof. Stewart", 4, 60))
    system.course_catalog.add_course(Course("MATH-UA 122", "Calculus II", "Prof. Stewart", 4, 60))
    system.course_catalog.add_course(Course("MATH-UA 123", "Calculus III", "Prof. Huang", 4, 60))
    system.course_catalog.add_course(Course("MATH-UA 140", "Linear Algebra", "Prof. Lopez", 4, 50))
    system.course_catalog.add_course(Course("MATH-UA 150", "Discrete Mathematics", "Prof. Kim", 4, 50))
    system.course_catalog.add_course(Course("MATH-UA 160", "Probability & Statistics", "Prof. Wilson", 4, 50))
    system.course_catalog.add_course(Course("MATH-UA 200", "Ordinary Differential Equations", "Prof. Baker", 4, 45))
    system.course_catalog.add_course(Course("MATH-UA 210", "Real Analysis I", "Prof. Zhao", 4, 40))
    system.course_catalog.add_course(Course("MATH-UA 220", "Abstract Algebra I", "Prof. Singh", 4, 35))
    system.course_catalog.add_course(Course("MATH-UA 230", "Topology I", "Prof. Garcia", 4, 30))
    system.course_catalog.add_course(Course("MATH-UA 240", "Complex Variables", "Prof. Tran", 4, 30))
    system.course_catalog.add_course(Course("MATH-UA 250", "Probability Theory", "Prof. O'Connor", 4, 40))
    system.course_catalog.add_course(Course("MATH-UA 260", "Statistics & Data Analysis", "Prof. Martinez", 4, 50))
    system.course_catalog.add_course(Course("MATH-UA 270", "Numerical Methods", "Prof. Chen", 4, 40))

    # Electives
    system.course_catalog.add_course(Course("CSCI-UA 420", "Machine Learning & Data Mining", "Prof. Gupta", 4, 30))
    system.course_catalog.add_course(Course("CSCI-UA 430", "Cryptography and Security", "Prof. Roy", 4, 25))
    system.course_catalog.add_course(Course("CSCI-UA 440", "Operating Systems II", "Prof. Kumar", 4, 20))
    system.course_catalog.add_course(Course("CSCI-UA 450", "Advanced Algorithms", "Prof. Lee", 4, 20))
    system.course_catalog.add_course(Course("MATH-UA 300", "Real Analysis II", "Prof. White", 4, 25))
    system.course_catalog.add_course(Course("MATH-UA 310", "Functional Analysis", "Prof. Zhao", 4, 20))
    system.course_catalog.add_course(Course("MATH-UA 320", "Probability & Stochastic Processes", "Prof. Johnson", 4, 25))
    system.course_catalog.add_course(Course("MATH-UA 330", "Partial Differential Equations", "Prof. Green", 4, 20))
    system.course_catalog.add_course(Course("MATH-UA 340", "Numerical Linear Algebra", "Prof. Chen", 4, 25))
    system.course_catalog.add_course(Course("MATH-UA 350", "Graph Theory & Combinatorics", "Prof. Kim", 4, 25))
    system.course_catalog.add_course(Course("MATH-UA 360", "Mathematical Statistics", "Prof. Lee", 4, 25))
    system.course_catalog.add_course(Course("MATH-UA 370", "Topology II", "Prof. Garcia", 4, 20))
    system.course_catalog.add_course(Course("MATH-UA 380", "Differential Geometry", "Prof. Tran", 4, 20))
