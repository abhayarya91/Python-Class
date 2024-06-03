class Student:
    def __init__(self, name, roll_no, class_, specialization, mark1, mark2):
        self.name = name
        self.roll_no = roll_no
        self.class_ = class_
        self.specialization = specialization
        self.mark1 = mark1
        self.mark2 = mark2

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student(self):
        name = input("Enter student's name: ")
        roll_no = input("Enter student's roll number: ")
        class_ = input("Enter student's class: ")
        specialization = input("Enter student's specialization: ")
        mark1 = float(input("Enter student's mark1: "))
        mark2 = float(input("Enter student's mark2: "))
        student = Student(name, roll_no, class_, specialization, mark1, mark2)
        self.students.append(student)
        print("Student information accepted successfully.")

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("List of students:")
            for student in self.students:
                print(f"Name: {student.name}, Roll No: {student.roll_no}, Class: {student.class_}, Specialization: {student.specialization}, Mark1: {student.mark1}, Mark2: {student.mark2}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found with roll number {roll_no}:")
                print(f"Name: {student.name}, Roll No: {student.roll_no}, Class: {student.class_}, Specialization: {student.specialization}, Mark1: {student.mark1}, Mark2: {student.mark2}")
                return
        print(f"No student found with roll number {roll_no}.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with roll number {roll_no} deleted successfully.")
                return
        print(f"No student found with roll number {roll_no}.")

    def update_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Enter new information:")
                student.name = input("Enter student's name: ")
                student.class_ = input("Enter student's class: ")
                student.specialization = input("Enter student's specialization: ")
                student.mark1 = float(input("Enter student's mark1: "))
                student.mark2 = float(input("Enter student's mark2: "))
                print(f"Student with roll number {roll_no} updated successfully.")
                return
        print(f"No student found with roll number {roll_no}.")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nWelcome to Student Management System")
        print("1. Accept Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sms.accept_student()
        elif choice == '2':
            sms.display_students()
        elif choice == '3':
            roll_no = input("Enter student's roll number to search: ")
            sms.search_student(roll_no)
        elif choice == '4':
            roll_no = input("Enter student's roll number to delete: ")
            sms.delete_student(roll_no)
        elif choice == '5':
            roll_no = input("Enter student's roll number to update: ")
            sms.update_student(roll_no)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
