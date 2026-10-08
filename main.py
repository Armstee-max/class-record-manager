import json, csv


def load_students():
    with open("students.json", "r") as file:
        load = json.load(file)
        return load

students = load_students()


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Student Course: ")
    score = int(input("Enter Student Score: "))
    one_student = {
        "student id": student_id,
        "name": name,
        "course": course,
        "score": score
    }

    for student in students:
        if student["student id"] == student_id:
            print("Student ID exists already")
            return False
    return one_student

def save_students():
    new_students = add_student()
    if new_students:
        students.append(new_students)
    with open("students.json", "w") as file:
        json.dump(students, file)

def view_students():
    students = load_students()
    if not students:
        print("No Students Available")
        return
    print("Student Records:")
    for student in students:
        print(f"Student ID: {student['student id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Score: {student['score']}")

def search_students():
    student_id = input("Enter Student ID: ")
    found = False
    for student in students:
        if student["student id"] == student_id:
            found = True
            print("Match Found")
            print(f"Student ID: {student['student id']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Score: {student['score']}")
    if not found:
        print("Match not found")


while True:
    print("CLASSROOM RECORD MANAGER")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Score")
    print("5. Remove Student")
    print("6. Show Class Statistics")
    print("7. Export Records to CSV")
    print("8. Exit")

    decision = input("Choose an option: ")
    if decision == "1":
        save_students()
    elif decision == "2":
        view_students()
    elif decision == "3":
        search_students()
    elif decision == "4":
        pass
    elif decision == "5":
        pass
    elif decision == "6":
        pass
    elif decision == "7":
        pass
    elif decision == "8":
        break
