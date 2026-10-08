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
    student = students.append(one_student)
    for student in students:
        if one_student["student id"]:
            print("Student ID exists already")

    
    return one_student

# test = add_student()
# print(test)

while True:
    print("Add student")
    print("Exit")
    decision = input("Enter 1 or 2")
    if decision == "1":
        add_student()
    elif decision == "2":
        break