import json, csv

students = []


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
    return one_student

def save_students():
    new_students = add_student()
    students.append(new_students)
    with open("students.json", "w") as file:
        json.dump(students, file)

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
        add_student()
    elif decision == "2":
        pass
    elif decision == "3":
        pass
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
