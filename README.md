🚀 Version: v1.0 (Stable)

# Student Management System (Python)
Console-based Student Management System built in Python using OOP and file handling (CSV/TXT) to perform CRUD operations with persistent storage.
### 🔚 Status
Project structure completed and ready for local Git workflow.


---

## Features

- Add new student
- Prevent duplicate student IDs
- View all students
- Search student by ID
- Delete student
- Persistent storage using CSV file



What’s New in v2.0 :

Added a confirmation step before deleting a student to avoid accidental data loss
Implemented validation to ensure student IDs are unique during the add operation
Introduced automatic creation of the student data file if it is missing

Improved User Experience :

Improved menu layout for better readability
Displayed student details in a clear and consistent format
Added safety prompts for actions that modify or delete data

File Safety & Reliability :

Automatically creates the required data folder and CSV file if they do not exist
Prevents program crashes caused by missing or deleted data files

---

## Project Structure

student-management-system/
├── data/
│   └── students.csv
├── student.py
├── student_manager.py
├── main.py
└── README.md

---

## Technologies Used

- Python 3
- CSV File Handling
- Object-Oriented Programming (OOP)
- Git & GitHub

---

## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the program:

python main.py



---

## Learning Outcomes

- Practical use of Python classes and objects
- File handling using CSV
- Modular coding practices
- Using Git for version control

---

## Author

Sahil Wasankar


