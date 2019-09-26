import math
class Circle():
    def __init__(self, xc, yc, x1, y1):
        self.xc = xc
        self.yc = yc
        self.x1 = x1
        self.y1 = y1

    def radius(self):
        r = math.sqrt((self.x1-self.xc)**2+(self.y1-self.yc)**2)
        return r
    
    def area(self):
        r = Circle.radius(self)
        a = math.pi*r**2
        return a
    
    def circumference(self):
        r = Circle.radius(self)
        c = 2*r*math.pi
        return c
    
    def __eq__(self, other):
        return (self.area() == other.area()) and (self.circumference() == other.circumference())

class rcircle(Circle):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        r = self.radius
        area = math.pi*r**2
        return area

    def circumference(self):
        r = self.radius
        circumference = 2*r*math.pi
        return circumference
        
C0 = Circle(0,0,3,4)
r = Circle.radius(C0)
a = Circle.area(C0)
c = Circle.circumference(C0)

C1 = rcircle(5)
a1 = rcircle.area(C1)
c2 = rcircle.circumference(C1)
e = Circle.__eq__(C0, C1)

print(a)
print(c)
print(a1)
print(c2)
print(e)