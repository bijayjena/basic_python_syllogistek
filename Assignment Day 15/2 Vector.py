# Design a vector class that will support some of the vector operations
import math

from pip._vendor.distlib.compat import raw_input


class Vector():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Vector({},{})".format(self.a, self.b)

    def __add__(self, other):
        self.a += other.a
        self.b += other.b
        return Vector(self.a, self.b)

    def __sub__(self, other):
        self.a -= other.a
        self.a -= other.b
        return Vector(self.a, b)

    def __mul__(self, other):
        self.a *= other.a
        self.b *= other.b
        return Vector(self.a, self.b)

    def __abs__(self):
        return math.hypot(self.a, self.b)


# Main
a, b = map(int, raw_input("Input values of vector 1: ").split())
v1 = Vector(a, b)
a, b = map(int, raw_input("Input values of vector 2: ").split())
v2 = Vector(a, b)
v3 = Vector(4, 5)
print("Vector addition:", v1+v2+v3)
print("Vector subtraction:", v1-v2)
print("Vector multiplication:", v1*v2)
print("Absolute Value:", v1.__abs__())