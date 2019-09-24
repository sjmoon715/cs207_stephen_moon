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

C0 = Circle(0,0,5,5)
r = Circle.radius(C0)
a = Circle.area(C0)
c = Circle.circumference(C0)
print(r)
print(a)
print(c)