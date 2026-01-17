# csv is a built-in Python module
# It helps you read from and write to CSV files
# CSV = Comma Separated Values
import csv
from student import Student

class StudentManager:
  def __init__(self, filename = "students.csv"):
    self.filename = filename
    self.students = []
    self.load_students()
    
  def  load_students(self):
    try:
       with open(self.filename , newline = "") as file:
         reader = csv.reader(file)   #csv.reader converts each row into a list when iterated
         for row in reader:
           student = Student(row[0],row[1],row[2],row[3])
           self.students.append(student)
    except FileNotFoundError:
      pass

  def save_students(self):
     with open(self.filename , "w" ,newline="") as file:
        writer = csv.writer(file)
        for student in self.students:
          writer.writerow(student.to_csv_row())

  def add_student(self , student):
       self.students.append(student)
       self.save_students()
         
         
  




