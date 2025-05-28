class circle():
    
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2 * 3.14
    def peri(self):
        return self.radius * 2 * 3.14
    
radius = int(input('Enter radius: '))
newCircle  = circle(radius)
print(newCircle.area())
print(newCircle.peri())


class rectangle():

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def peri(self):
        return 2 * (self.length + self.breadth)
    
length = int(input('Enter length: '))
breadth = int(input('Enter breadth: '))
newRect = rectangle(length, breadth)
print(newRect.area())
print(newRect.peri())