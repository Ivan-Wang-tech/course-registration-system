# Course Registration System

## 1. Overview

This project is a **Python GUI-based Course Registration System**.  
It allows students to:

- browse all available courses,
- view detailed course information,
- register for courses (if capacity allows),
- drop previously registered courses, and
- view their current schedule.

All data (students, courses, registrations) is stored in **in-memory Python lists** to keep the system simple and focused on object-oriented design rather than database code.

## 2. Team Members

- Ivan Wang (NetID: yw6505)
- Zhengxuan Tian (NetID: zt2254)
- Hanlin Yan (NetID: hy2484)

## 3. Key Features

1. **Student Registration & Login**
   - Students can create an account.
   - Students must log in before accessing other features.

2. **View Course List**
   - Display all available courses in the system.

3. **View Course Details**
   - Show selected course details, including:
     - course title
     - instructor
     - credits
     - capacity
     - current number of enrolled students

4. **Register for a Course**
   - A student can register for a course if:
     - the course is not full, and
     - the student is not already registered for this course.

5. **Drop a Course**
   - A student can drop a course that they previously registered for.

6. **View My Courses**
   - A student can view all courses they are currently enrolled in.

## 4. System Design

The system follows basic **object-oriented design** and separates UI, entities, and controllers.

### 4.1 Entity Classes

- `Student`
  - Attributes such as: `student_id`, `name`, `password`, `registered_courses`, etc.
- `Course`
  - Attributes such as: `course_id`, `title`, `instructor`, `credits`, `capacity`, `enrolled_students`, etc.
- `Registration`
  - Represents a relationship between a `Student` and a `Course`.

### 4.2 Controller / Manager Classes

- `RegistrationSystem`
  - High-level coordinator that connects the UI with the managers below.
- `CourseCatalog`
  - Manages all `Course` objects:
    - add / remove courses (if needed),
    - find course by id,
    - list all available courses.
- `RegistrationManager`
  - Responsible for:
    - registering a student into a course,
    - dropping a course for a student,
    - enforcing rules such as capacity and duplicate registration.
- `AuthenticationService`
  - Handles:
    - student sign-up,
    - login / logout,
    - basic credential checking.

### 4.3 UI Class

- `MainGUI`
  - The main graphical interface of the system.
  - Provides:
    - login / registration window,
    - panels to show course list and course details,
    - buttons or menus to register / drop courses,
    - view current schedule.

(Implementation details: we plan to use a Python GUI library such as `tkinter`.)

## 5. Project Structure (planned)

```text
course-registration-system/
├── src/
│   ├── main.py              # entry point, create RegistrationSystem + MainGUI
│   ├── entities/
│   │   ├── student.py
│   │   ├── course.py
│   │   └── registration.py
│   ├── controllers/
│   │   ├── registration_system.py
│   │   ├── course_catalog.py
│   │   ├── registration_manager.py
│   │   └── authentication_service.py
│   └── ui/
│       └── main_gui.py
├── docs/
│   └── proposal.pdf         # original project proposal
└── README.md
