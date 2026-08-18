students = []
all_marks = {}  
def new_student():
    """Add a new student record."""
    name = input("enter student name:")
    department = input("enter student department:")
    while True:
        try:
            student_id = int(input("enter student id:"))
            break
        except ValueError:
            print("enter valid numbers only!!!")
    student = {
        "name": name,
        "department": department,
        "id": str(student_id)
    }
    students.append(student)
    print("student record entered!!!")
def update_student():
    """Update an existing student's name or department by id."""
    student_id = input("enter student id to update:")
    for student in students:
        if student["id"] == student_id:
            print("leave blank to keep current value")
            new_name = input(f"enter new name (current: {student['name']}): ")
            new_department = input(f"enter new department (current: {student['department']}): ")
            if new_name.strip() != "":
                student["name"] = new_name
            if new_department.strip() != "":
                student["department"] = new_department
            print("student record updated!!!")
            return
    print("no student found with that id")
def marks():
    """Record marks for a student by id."""
    student_id = input("enter student id to add marks for:")
    while True:
        try:
            english = int(input("Enter Marks For English:"))
            computer = int(input("Enter Marks For Computer Science:"))
            art = int(input("Enter Marks For Arts:"))
            break
        except ValueError:
            print("enter valid numbers only!!!")
    all_marks[student_id] = {
        "english": str(english),
        "computer": str(computer),
        "art": str(art)
    }
    print("marks recorded for id", student_id)
def display_marks():
    """Show marks for a student by id."""
    student_id = input("enter student id to view marks :")
    if student_id in all_marks:
        m = all_marks[student_id]
        print("Subject Wise Result:")
        print("Marks of English:", m["english"])
        print("Marks of Computer:", m["computer"])
        print("Marks of Art:", m["art"])
    else:
        print("no marks found for that id")
def menu():
    """Main menu loop."""
    while True:
        print("----Student Result Display System----")
        print("1.Add Student")
        print("2.Enter Marks")
        print("3.Display Marks")
        print("4.Update Student")
        print("5.Exit")
        choice = input("Enter Choice:")
        if choice == "1":
            new_student()
        elif choice == "2":
            marks()
        elif choice == "3":
            display_marks()
        elif choice == "4":
            update_student()
        elif choice == "5":
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    menu()