from student import Student
from teacher import Teacher
from courses import Course
import utils

# Global lists to store data
students = []
teachers = []
courses = []

# Student management functions
def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = Student(id, name, age, grade)
    students.append(student)
    save_students()

def remove_student():
    id = input("Enter student ID to remove: ")
    global students
    students = [student for student in students if student.id != id]
    save_students()

def update_student():
    id = input("Enter student ID to update: ")
    for student in students:
        if student.id == id:
            student.name = input("Enter new name: ")
            student.age = input("Enter new age: ")
            student.grade = input("Enter new grade: ")
            save_students()
            return
    print("Student not found")

def view_students():
    for student in students:
        student.display_info()

def save_students():
    data = [student.to_csv() for student in students]
    utils.write_csv('data/students.csv', data)

def load_students():
    rows = utils.read_csv('data/students.csv')
    return [Student.from_csv(row) for row in rows]

# Teacher management functions
def add_teacher():
    id = input("Enter teacher ID: ")
    name = input("Enter teacher name: ")
    subject = input("Enter teacher subject: ")
    teacher = Teacher(id, name, subject)
    teachers.append(teacher)
    save_teachers()

def remove_teacher():
    id = input("Enter teacher ID to remove: ")
    global teachers
    teachers = [teacher for teacher in teachers if teacher.id != id]
    save_teachers()

def update_teacher():
    id = input("Enter teacher ID to update: ")
    for teacher in teachers:
        if teacher.id == id:
            teacher.name = input("Enter new name: ")
            teacher.subject = input("Enter new subject: ")
            save_teachers()
            return
    print("Teacher not found")

def view_teachers():
    for teacher in teachers:
        teacher.display_info()

def save_teachers():
    data = [teacher.to_csv() for teacher in teachers]
    utils.write_csv('data/teachers.csv', data)

def load_teachers():
    rows = utils.read_csv('data/teachers.csv')
    return [Teacher.from_csv(row) for row in rows]

# Course management functions
def add_course():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    teacher_id = input("Enter teacher ID for the course: ")
    course = Course(id, name, teacher_id)
    courses.append(course)
    save_courses()

def remove_course():
    id = input("Enter course ID to remove: ")
    global courses
    courses = [course for course in courses if course.id != id]
    save_courses()

def update_course():
    id = input("Enter course ID to update: ")
    for course in courses:
        if course.id == id:
            course.name = input("Enter new name: ")
            course.teacher_id = input("Enter new teacher ID: ")
            save_courses()
            return
    print("Course not found")

def view_courses():
    for course in courses:
        course.display_info()

def save_courses():
    data = [course.to_csv() for course in courses]
    utils.write_csv('data/courses.csv', data)

def load_courses():
    rows = utils.read_csv('data/courses.csv')
    return [Course.from_csv(row) for row in rows]

# Main program
def main():
    global students, teachers, courses
    students = load_students()
    teachers = load_teachers()
    courses = load_courses()

    while True:
        print("\n1. Student Management")
        print("2. Teacher Management")
        print("3. Course Management")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manage_students()
        elif choice == '2':
            manage_teachers()
        elif choice == '3':
            manage_courses()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

def manage_students():
    while True:
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. View Students")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

def manage_teachers():
    while True:
        print("\n1. Add Teacher")
        print("2. Remove Teacher")
        print("3. Update Teacher")
        print("4. View Teachers")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_teacher()
        elif choice == '2':
            remove_teacher()
        elif choice == '3':
            update_teacher()
        elif choice == '4':
            view_teachers()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

def manage_courses():
    while True:
        print("\n1. Add Course")
        print("2. Remove Course")
        print("3. Update Course")
        print("4. View Courses")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_course()
        elif choice == '2':
            remove_course()
        elif choice == '3':
            update_course()
        elif choice == '4':
            view_courses()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
