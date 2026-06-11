# 📚 Student Attendance Management System

## 1. Introduction

The **Student Attendance Management System** is a Python-based mini project developed using **SQLite** for database management. The system helps educational institutions maintain student attendance records efficiently and accurately. It provides functionalities for student registration, course management, attendance marking, and attendance analysis.

---

## 2. Objectives

* To automate student attendance management.
* To reduce manual errors in attendance tracking.
* To store attendance records securely in a database.
* To generate attendance statistics quickly and efficiently.

---

## 3. Features

### 👨‍🎓 Student Registration

* Add new students to the system.
* Store student details such as name, email, and phone number.

### 📖 Course Management

* Create and manage courses.
* Assign unique course codes.

### 📝 Student Enrollment

* Enroll students into selected courses.
* Maintain enrollment records.

### ✅ Attendance Marking

* Mark students as Present or Absent.
* Store attendance records with date and course details.

### 📅 Attendance History

* View attendance records of students.
* Retrieve attendance information based on course and date.

### 📊 Attendance Percentage Calculation

* Calculate attendance percentage for each student.
* Generate attendance reports.

---

## 4. Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Application Development |
| SQLite     | Database Management     |
| SQL        | Database Queries        |

---

## 5. Project Structure

```text
Student-Attendance-Management-System/
│
├── attendance_system.py
├── attendance.db
├── README.md
└── requirements.txt
```

---

## 6. Database Design

### Students Table

| Field        | Description       |
| ------------ | ----------------- |
| student_id   | Unique Student ID |
| student_name | Student Name      |
| email        | Email Address     |
| phone        | Contact Number    |

### Courses Table

| Field       | Description        |
| ----------- | ------------------ |
| course_id   | Unique Course ID   |
| course_name | Course Name        |
| course_code | Unique Course Code |

### Enrollments Table

| Field         | Description          |
| ------------- | -------------------- |
| enrollment_id | Unique Enrollment ID |
| student_id    | Student Reference ID |
| course_id     | Course Reference ID  |

### Attendance Table

| Field           | Description          |
| --------------- | -------------------- |
| attendance_id   | Unique Attendance ID |
| student_id      | Student Reference ID |
| course_id       | Course Reference ID  |
| attendance_date | Attendance Date      |
| status          | Present / Absent     |

---

## 7. System Workflow

1. Register Students.
2. Create Courses.
3. Enroll Students in Courses.
4. Mark Daily Attendance.
5. Store Attendance Records.
6. View Attendance History.
7. Calculate Attendance Percentage.

---

## 8. How to Run the Project

### Prerequisites

* Python 3.x installed.
* SQLite database support.

### Steps

**Step 1:** Clone the repository

```bash
git clone https://github.com/your-username/student-attendance-management-system.git
```

**Step 2:** Navigate to the project folder

```bash
cd student-attendance-management-system
```

**Step 3:** Run the application

```bash
python attendance_system.py
```

---

## 9. Advantages

* Easy to use.
* Reduces paperwork.
* Fast attendance tracking.
* Accurate record management.
* Low storage requirements.
* Lightweight SQLite database.

---

## 10. Future Enhancements

* Graphical User Interface (GUI) using Tkinter.
* User Authentication and Login System.
* Export Reports to Excel/PDF.
* Email Notifications.
* Attendance Dashboard.
* Web-Based Deployment using Flask or Django.

---

## 11. Conclusion

The **Student Attendance Management System** provides a simple and efficient solution for managing student attendance records. By using Python and SQLite, the system ensures accurate data storage, quick retrieval of attendance information, and automated attendance percentage calculations. This project demonstrates the practical application of database management and Python programming in educational institutions.

---

### 👨‍💻 Author

**Your Name**

**Mini Project – Student Attendance Management System**
**Department of Computer Science & Engineering**
**Academic Year: 2025-2026**

