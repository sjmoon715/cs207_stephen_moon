import math
import numpy as np
class RealExtensions():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Complex(RealExtensions):
    def __init__(self, a, b):
        RealExtensions.__init__(self, a,b)
    def _magnitude(self):
        m = math.sqrt(self.a**2 + self.b**2)
        return m
    def _angle(self):
        angle = np.arctan(self.b/self.a)
        return angle
    def polar(self):
        self.m = self._magnitude()
        self.angle = self._angle()
        return (self.m, self.angle)

class Dual(RealExtensions):
    def __init__(self, a, b):
        RealExtensions.__init__(self, a,b)
    def _magnitude(self):
        a = self.a
        return a
    def _angle(self):
        a = self.a
        b = self.b
        angle = b/a
        return angle
    def polar(self):
        self.a = self._magnitude()
        self.angle = self._angle()
        return (self.a, self.angle)


