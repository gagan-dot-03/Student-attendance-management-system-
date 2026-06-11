from database import create_database
import sqlite3
from datetime import date

create_database()


def add_student():
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, department) VALUES (?, ?)",
        (name, department)
    )

    conn.commit()
    conn.close()

    print("Student added successfully!")


def add_course():
    course_name = input("Enter Course Name: ")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (course_name) VALUES (?)",
        (course_name,)
    )

    conn.commit()
    conn.close()

    print("Course added successfully!")


def view_students():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    print("\n--- Students ---")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def view_courses():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")

    print("\n--- Courses ---")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def enroll_student():
    view_students()
    view_courses()

    student_id = int(input("\nEnter Student ID: "))
    course_id = int(input("Enter Course ID: "))

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )

    conn.commit()
    conn.close()

    print("Student enrolled successfully!")


def mark_attendance():
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))

    status = input("Enter Attendance (P/A): ").upper()

    attendance_date = str(date.today())

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO attendance
        (student_id, course_id, attendance_date, status)
        VALUES (?, ?, ?, ?)
    """, (student_id, course_id, attendance_date, status))

    conn.commit()
    conn.close()

    print("Attendance marked successfully!")


def attendance_history():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               c.course_name,
               a.attendance_date,
               a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.student_id
        JOIN courses c ON a.course_id = c.course_id
    """)

    records = cursor.fetchall()

    print("\n--- Attendance History ---")

    if not records:
        print("No attendance records found.")
    else:
        for row in records:
            print(row)

    conn.close()


def attendance_percentage():
    student_id = int(input("Enter Student ID: "))

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE student_id = ?
    """, (student_id,))

    total_classes = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE student_id = ?
        AND status = 'P'
    """, (student_id,))

    present_count = cursor.fetchone()[0]

    conn.close()

    if total_classes == 0:
        print("No attendance records found.")
    else:
        percentage = (present_count / total_classes) * 100
        print(f"Attendance Percentage: {percentage:.2f}%")


while True:

    print("\n========== STUDENT ATTENDANCE MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Add Course")
    print("3. View Students")
    print("4. View Courses")
    print("5. Enroll Student")
    print("6. Mark Attendance")
    print("7. Attendance History")
    print("8. Attendance Percentage")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_course()

    elif choice == "3":
        view_students()

    elif choice == "4":
        view_courses()

    elif choice == "5":
        enroll_student()

    elif choice == "6":
        mark_attendance()

    elif choice == "7":
        attendance_history()

    elif choice == "8":
        attendance_percentage()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")