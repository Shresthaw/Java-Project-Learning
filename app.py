import json

FILE_NAME = "students.txt"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    students[sid] = {"name": name, "marks": marks}
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\nID\tName\tMarks")
    print("-" * 25)
    for sid, data in students.items():
        print(f"{sid}\t{data['name']}\t{data['marks']}")


def search_student(students):
    sid = input("Enter Student ID to search: ")
    if sid in students:
        print("Name:", students[sid]["name"])
        print("Marks:", students[sid]["marks"])
    else:
        print("Student not found.")


def update_marks(students):
    sid = input("Enter Student ID to update: ")
    if sid in students:
        new_marks = int(input("Enter new marks: "))
        students[sid]["marks"] = new_marks
        save_students(students)
        print("Marks updated.")
    else:
        print("Student not found.")


def delete_student(students):
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        save_students(students)
        print("Student deleted.")
    else:
        print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_marks(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
