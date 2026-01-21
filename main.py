# csv is a built-in Python module
# It helps you read from and write to CSV files
# CSV = Comma Separated Values
# Student Management System - Local Git Setup

from student import Student
from manager import StudentManager

def show_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ====== ")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("=======================================")

manager = StudentManager()

def get_valid_student_data():

    while True:
     try:
       sid =  input("ID: ").strip()
       break
       
     except ValueError:
        print("Input the valid integer only!")    

    while True:
        name = input("Name: ").strip()
        if name :
            break
        print("The name input should not be empty")
                     
    while True:
     try :
         age = int(input("Age: "))
         if age > 0:             
            break
         print("Age must be positive")

     except ValueError:
         print("Age must be a number")


    while True:
        course = input("Course: ")
        if course:
            break
        print("Course should not be empty")


    return sid,name,age,course



while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        sid, name, age, course = get_valid_student_data()
        student = Student(sid, name, age, course)
        manager.add_student(student) 
        
    elif choice == "2":
        manager.view_students()


    elif choice == "3":
         sid = input("Enter Student ID to search: ")
         manager.search_student(sid)

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        manager.delete_student(sid)    

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")



    



    
    


