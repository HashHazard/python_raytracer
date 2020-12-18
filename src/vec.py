import math

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if (type(other) == type(self)):
            a = self.x + other.x
            b = self.y + other.y
            c = self.z + other.z
        else:
            a = self.x + other
            b = self.y + other
            c = self.z + other
        return Vector(a, b, c)

    def __sub__(self, other):
        if (type(other) == type(self)):
            a = self.x - other.x
            b = self.y - other.y
            c = self.z - other.z
        else:
            a = self.x - other
            b = self.y - other
            c = self.z - other
        return Vector(a, b, c)

    def __mul__(self, other):
        if (type(other) == type(self)):
            a = self.x * other.x
            b = self.y * other.y
            c = self.z * other.z
        else:
            a = self.x * other
            b = self.y * other
            c = self.z * other
        return Vector(a, b, c)

    def __div__(self, other):
        if (type(other) == type(self)):
            a = self.x / other.x
            b = self.y / other.y
            c = self.z / other.z
        else:
            a = self.x / other
            b = self.y / other
            c = self.z / other
        return Vector(a, b, c)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def show(self):
        return f'{self.x}i {self.y}j {self.z}k'

    def __str__(self):
        return f'{self.x}i {self.y}j {self.z}k'

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def sqrt(self):
        return Vector(math.sqrt(self.x),math.sqrt(self.y),math.sqrt(self.z))

    def normalize(self):
        return Vector(self.x/self.length(), self.y/self.length(), self.z/self.length())
