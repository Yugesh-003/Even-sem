class Shape:
    def area(self, a=None, b=None):
        if a and b:
            print("Rectangle Area:", a * b)
        elif a:
            print("Square Area:", a * a)
        else:
            print("No dimensions provided")
s = Shape()
s.area(5, 10)
s.area(5)
s.area()