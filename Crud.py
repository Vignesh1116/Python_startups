students = {}

# CREATE
def create_student(student_id, name):
    students[student_id] = name
    print("Student added successfully")

# READ
def read_students():
    print(students)

# UPDATE
def update_student(student_id, name):
    if student_id in students:
        students[student_id] = name
        print("Student updated successfully")
    else:
        print("Student not found")

# DELETE
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully")
    else:
        print("Student not found")


# Function calls
create_student(1, "Vignesh")
create_student(2, "Kumar")

read_students()

update_student(1, "Vignesh Kumar")
read_students()

delete_student(2)
read_students()