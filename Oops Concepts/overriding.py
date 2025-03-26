class Marks:
    def calculate(self):
        print("Calculating marks...")
class Student(Marks):
    def calculate(self):
        print("Student's Marks Calculated")
s = Student()
s.calculate()