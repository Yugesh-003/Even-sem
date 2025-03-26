class Student:
    def __init__(self):
        self.name = "yugg"
        self.age = 12

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

obj = Student()
obj.display()