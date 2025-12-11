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

## 3. Installation & Setup

### 3.1 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 3.2 Install Dependencies

This project uses **CustomTkinter** for a modern GUI interface. Install it using:
```bash
pip install customtkinter
```

### 3.3 Running the Application

After installing the dependencies, run the application with:
```bash
python main.py
```

Or alternatively:
```bash
python3 main.py
```

The GUI will launch, where you can:

- Create a new student account
- Log in with accounts created during this session

*All data is temporary because the system does not use a database.*


## 4. Key Features

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

## 5. System Design

The system follows basic **object-oriented design** and separates UI, entities, and controllers.

### 5.1 Entity Classes

- **`Student`**  
  Contains student information (`student_id`, `name`, `password`) and maintains a list of courses the student has registered for.

- **`Course`**  
  Stores course-related data (`course_id`, `title`, `instructor`, `credits`, `capacity`) and keeps track of currently enrolled students.

### 5.2 Controller / Manager Classes

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

### 5.3 UI Class

- `MainGUI`
  - The main graphical interface of the system built with CustomTkinter.
  - Provides:
    - login / registration window,
    - panels to show course list and course details,
    - buttons or menus to register / drop courses,
    - view current schedule.

## 6. Usage Guide

### First Time Setup
1. Install Python 3.8+
2. Install CustomTkinter: `pip install customtkinter`
3. Run the application: `python main.py`

### Creating an Account
1. Click **"Sign Up"** on the login screen
2. Enter your Student ID, Name, and Password
3. Click **"Create Account"**

### Logging In
1. Enter your Student ID and Password
2. Click **"Login"**

### Browsing and Registering for Courses
1. From the main menu, click **"Browse Courses"**
2. View the list of available courses
3. Click **"Register"** next to any course to enroll
4. Check your remaining credits in the top-right corner

### Viewing Your Schedule
1. Click **"My Schedule"** from the main menu
2. View all courses you're enrolled in
3. Click **"Drop"** to remove a course from your schedule

### Logging Out
- Click the **"Logout"** button in the top navigation bar

## 7. Notes

- All data is stored in memory and will be reset when the application closes.
- The system includes pre-populated sample courses for testing.
- Students have a maximum credit limit that cannot be exceeded when registering.
- The original project proposal included a separate `Registration` class to explicitly model the relationship between a `Student` and a `Course`.  
  During implementation, we refactored the design and determined that this additional class was unnecessary.

  The relationship is fully captured through:
  - `student.registered_courses`
  - `course.enrolled_students`

  This bidirectional structure allows the system to track enrollments effectively without introducing extra complexity.  
  Therefore, the `Registration` entity was intentionally omitted in the final implementation.

---

**Version:** 1.0  
**Last Updated:** Dec 11 2025

