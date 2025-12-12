students = {}
courses = {}
grades = {}


def main():
    load_all_data()

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_courses()
        elif choice == "3":
            manage_enrollments_grades()
        elif choice == "4":
            statistics_reports()
        elif choice == "5":
            file_operations()
        elif choice == "6":
            break


def print_menu():
    print("\n=== UNIVERSITY SYSTEM ===")
    print("1. Students")
    print("2. Courses")
    print("3. Grades")
    print("4. Statistics")
    print("5. Files")
    print("6. Exit")


# === STUDENTS ===
def manage_students():
    while True:
        print("\n--- STUDENTS ---")
        print("1. Add")
        print("2. View all")
        print("3. Update")
        print("4. Delete")
        print("5. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break


def add_student():
    student_id = input("Student ID: ").strip()

    # Check if exists
    for sid in students:
        if sid == student_id:
            print("Error: ID exists!")
            return

    name = input("Name: ").strip()

    try:
        year = int(input("Year (1-5): "))
        if year < 1 or year > 5:
            print("Error: Invalid year!")
            return
    except:
        print("Error: Enter a number!")
        return

    students[student_id] = {"name": name, "year": year}
    print("Student added!")


def view_students():
    if len(students) == 0:
        print("No students")
        return

    # Get all IDs and sort them
    student_ids = list(students.keys())
    student_ids.sort()  # Sort alphabetically

    print("\nAll Students:")
    for student_id in student_ids:
        info = students[student_id]
        print(f"ID: {student_id}")
        print(f"  Name: {info['name']}")
        print(f"  Year: {info['year']}")


def update_student():
    student_id = input("Student ID to update: ").strip()

    if student_id not in students:
        print("Error: Student not found!")
        return

    info = students[student_id]
    print(f"Current: {info['name']}, Year {info['year']}")

    name = input("New name (press Enter to keep): ").strip()
    if name:
        students[student_id]['name'] = name

    year_input = input("New year (press Enter to keep): ").strip()
    if year_input:
        try:
            year = int(year_input)
            if 1 <= year <= 5:
                students[student_id]['year'] = year
        except:
            print("Invalid year!")

    print("Updated!")


def delete_student():
    student_id = input("Student ID to delete: ").strip()

    if student_id not in students:
        print("Error: Student not found!")
        return

    # Remove student
    del students[student_id]

    # Remove their grades
    for key in list(grades.keys()):
        if key[0] == student_id:  # key is (student_id, course_id)
            del grades[key]

    print("Student deleted!")


# === COURSES ===
def manage_courses():
    while True:
        print("\n--- COURSES ---")
        print("1. Add")
        print("2. View all")
        print("3. Update")
        print("4. Delete")
        print("5. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            break


def add_course():
    course_id = input("Course ID: ").strip().upper()

    # Check if exists
    for cid in courses:
        if cid == course_id:
            print("Error: Course exists!")
            return

    name = input("Course name: ").strip()
    credits = input("Credits: ").strip()

    courses[course_id] = {"name": name, "credits": credits}
    print("Course added!")


def view_courses():
    if len(courses) == 0:
        print("No courses")
        return

    course_ids = list(courses.keys())
    course_ids.sort()

    print("\nAll Courses:")
    for course_id in course_ids:
        info = courses[course_id]
        print(f"ID: {course_id}")
        print(f"  Name: {info['name']}")
        print(f"  Credits: {info['credits']}")


def update_course():
    course_id = input("Course ID to update: ").strip().upper()

    if course_id not in courses:
        print("Error: Course not found!")
        return

    info = courses[course_id]
    print(f"Current: {info['name']}, {info['credits']} credits")

    name = input("New name (press Enter to keep): ").strip()
    if name:
        courses[course_id]['name'] = name

    credits = input("New credits (press Enter to keep): ").strip()
    if credits:
        courses[course_id]['credits'] = credits

    print("Updated!")


def delete_course():
    course_id = input("Course ID to delete: ").strip().upper()

    if course_id not in courses:
        print("Error: Course not found!")
        return

    # Remove course
    del courses[course_id]

    # Remove related grades
    for key in list(grades.keys()):
        if key[1] == course_id:  # key is (student_id, course_id)
            del grades[key]

    print("Course deleted!")


# === GRADES ===
def manage_enrollments_grades():
    while True:
        print("\n--- GRADES ---")
        print("1. Enroll student")
        print("2. Add/update grade")
        print("3. View grades")
        print("4. Remove enrollment")
        print("5. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            enroll_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_grades()
        elif choice == "4":
            remove_enrollment()
        elif choice == "5":
            break


def enroll_student():
    print("\nAvailable students:")
    for sid in students:
        print(f"{sid}: {students[sid]['name']}")

    print("\nAvailable courses:")
    for cid in courses:
        print(f"{cid}: {courses[cid]['name']}")

    student_id = input("\nStudent ID: ").strip()
    course_id = input("Course ID: ").strip().upper()

    if student_id not in students:
        print("Error: Student not found!")
        return

    if course_id not in courses:
        print("Error: Course not found!")
        return

    # Check if already enrolled
    for key in grades:
        if key[0] == student_id and key[1] == course_id:
            print("Error: Already enrolled!")
            return

    # Enroll with no grade initially
    grades[(student_id, course_id)] = None
    print("Student enrolled!")


def add_grade():
    student_id = input("Student ID: ").strip()
    course_id = input("Course ID: ").strip().upper()

    # Find the enrollment
    found_key = None
    for key in grades:
        if key[0] == student_id and key[1] == course_id:
            found_key = key
            break

    if found_key is None:
        print("Error: Not enrolled!")
        return

    try:
        grade = int(input("Grade (0-20): "))
        if grade < 0 or grade > 20:
            print("Error: Invalid grade!")
            return

        grades[found_key] = grade
        print("Grade saved!")

    except:
        print("Error: Enter a number!")


def view_grades():
    student_id = input("Student ID: ").strip()

    if student_id not in students:
        print("Error: Student not found!")
        return

    print(f"\nGrades for {students[student_id]['name']}:")

    student_grades = []
    for key, grade in grades.items():
        if key[0] == student_id:
            course_name = courses[key[1]]['name']
            if grade is not None:
                print(f"{course_name}: {grade}/20")
                student_grades.append(grade)
            else:
                print(f"{course_name}: No grade")

    # Calculate average
    if len(student_grades) > 0:
        total = 0
        for grade in student_grades:
            total += grade
        average = total / len(student_grades)
        print(f"Average: {average:.1f}/20")


def remove_enrollment():
    student_id = input("Student ID: ").strip()
    course_id = input("Course ID: ").strip().upper()

    # Find and remove
    for key in list(grades.keys()):
        if key[0] == student_id and key[1] == course_id:
            del grades[key]
            print("Enrollment removed!")
            return

    print("Error: Enrollment not found!")


# === STATISTICS ===
def statistics_reports():
    while True:
        print("\n=== STATISTICS ===")
        print("1. Student averages")
        print("2. Course averages")
        print("3. Top 3 students")
        print("4. Pass/Fail rates")
        print("5. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            student_averages()
        elif choice == "2":
            course_averages()
        elif choice == "3":
            top_students()
        elif choice == "4":
            pass_fail_rates()
        elif choice == "5":
            break


def student_averages():
    print("\n--- STUDENT AVERAGES ---")

    if len(students) == 0:
        print("No students")
        return

    # Create list of students with averages
    student_list = []

    for student_id in students:
        # Collect grades for this student
        grade_list = []
        for key, grade in grades.items():
            if key[0] == student_id and grade is not None:
                grade_list.append(grade)

        # Calculate average
        if len(grade_list) > 0:
            total = 0
            for grade in grade_list:
                total += grade
            average = total / len(grade_list)

            student_list.append({
                'id': student_id,
                'name': students[student_id]['name'],
                'average': average
            })

    # Sort by average (highest first) - without lambda
    # Using simple bubble sort
    n = len(student_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_list[j]['average'] < student_list[j + 1]['average']:
                # Swap
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

    # Display
    for student in student_list:
        print(f"{student['name']}: {student['average']:.1f}/20")


def course_averages():
    print("\n--- COURSE AVERAGES ---")

    for course_id in courses:
        grade_list = []

        for key, grade in grades.items():
            if key[1] == course_id and grade is not None:
                grade_list.append(grade)

        if len(grade_list) > 0:
            total = 0
            for grade in grade_list:
                total += grade
            average = total / len(grade_list)

            # Count passes
            passes = 0
            for grade in grade_list:
                if grade >= 10:
                    passes += 1

            pass_rate = (passes / len(grade_list)) * 100

            print(f"{courses[course_id]['name']}:")
            print(f"  Average: {average:.1f}/20")
            print(f"  Pass rate: {pass_rate:.1f}%")
            print()


def top_students():
    print("\n--- TOP 3 STUDENTS ---")

    # First get all students with averages
    student_list = []

    for student_id in students:
        grade_list = []
        for key, grade in grades.items():
            if key[0] == student_id and grade is not None:
                grade_list.append(grade)

        if len(grade_list) > 0:
            total = 0
            for grade in grade_list:
                total += grade
            average = total / len(grade_list)

            student_list.append({
                'id': student_id,
                'name': students[student_id]['name'],
                'average': average
            })

    if len(student_list) == 0:
        print("No grades available!")
        return

    # Sort (bubble sort)
    n = len(student_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_list[j]['average'] < student_list[j + 1]['average']:
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

    # Show top 3
    count = min(3, len(student_list))
    for i in range(count):
        student = student_list[i]
        print(f"{i + 1}. {student['name']}: {student['average']:.1f}/20")


def pass_fail_rates():
    print("\n--- PASS/FAIL RATES ---")

    for course_id in courses:
        grade_list = []

        for key, grade in grades.items():
            if key[1] == course_id and grade is not None:
                grade_list.append(grade)

        if len(grade_list) > 0:
            passes = 0
            fails = 0

            for grade in grade_list:
                if grade >= 10:
                    passes += 1
                else:
                    fails += 1

            pass_rate = (passes / len(grade_list)) * 100
            fail_rate = (fails / len(grade_list)) * 100

            print(f"{courses[course_id]['name']}:")
            print(f"  Pass: {passes} students ({pass_rate:.1f}%)")
            print(f"  Fail: {fails} students ({fail_rate:.1f}%)")
            print()


# === FILES ===
def file_operations():
    while True:
        print("\n=== FILES ===")
        print("1. Save data")
        print("2. Load data")
        print("3. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            save_all_data()
        elif choice == "2":
            load_all_data()
        elif choice == "3":
            break


def save_all_data():
    try:
        # Save students
        with open("students.txt", "w") as f:
            for student_id in students:
                info = students[student_id]
                f.write(f"{student_id};{info['name']};{info['year']}\n")

        # Save courses
        with open("courses.txt", "w") as f:
            for course_id in courses:
                info = courses[course_id]
                f.write(f"{course_id};{info['name']};{info['credits']}\n")

        # Save grades
        with open("grades.txt", "w") as f:
            for key in grades:
                grade = grades[key]
                grade_str = "" if grade is None else str(grade)
                f.write(f"{key[0]};{key[1]};{grade_str}\n")

        print("Data saved!")

    except:
        print("Error saving!")


def load_all_data():
    try:
        # Clear current data
        students.clear()
        courses.clear()
        grades.clear()

        # Load students
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 3:
                    student_id = parts[0]
                    name = parts[1]
                    year = int(parts[2])
                    students[student_id] = {"name": name, "year": year}

        # Load courses
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 3:
                    course_id = parts[0]
                    name = parts[1]
                    credits = parts[2]
                    courses[course_id] = {"name": name, "credits": credits}

        # Load grades
        with open("grades.txt", "r") as f:
            for line in f:
                parts = line.strip().split(';')
                if len(parts) == 3:
                    student_id = parts[0]
                    course_id = parts[1]
                    grade_str = parts[2]

                    grade = None
                    if grade_str:
                        grade = int(grade_str)

                    grades[(student_id, course_id)] = grade

        print("Data loaded!")

    except FileNotFoundError:
        print("No previous data found.")
    except:
        print("Error loading!")


if __name__ == "__main__":
    main()








