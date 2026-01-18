import csv
from student import Student


class StudentManager:
    def __init__(self, filename="data/students.csv"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    student = Student(
                        student_id=row[0],
                        name=row[1],
                        age=int(row[2]),
                        course=row[3]
                    )
                    self.students.append(student)
        except FileNotFoundError:
            pass  # File will be created on first save

    def save_students(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow(student.to_csv_row())

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(
                student.student_id,
                student.name,
                student.age,
                student.course
            )
