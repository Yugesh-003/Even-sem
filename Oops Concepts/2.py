#single inheritance
class Academic:
    def __init__(self):
        self.marks = 100
    def display_academic(self):
        print(f"Marks: {self.marks}")
class StudentProfile(Academic):
    def __init__(self):
        self.name = "Yugg"
        super().__init__()
    def display(self):
        print(f"Student Name: {self.name}")


student = StudentProfile()
student.display_academic()
student.display()