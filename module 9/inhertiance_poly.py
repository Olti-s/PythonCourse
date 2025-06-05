import math


class shape:
    def area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.width


class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Paralelogrami(shape):
    def __init__(self, a, ha):
        self.a = a
        self.ha = ha

    def area(self):
        return self.a * self.ha

rrethi = circle(2)
drejtkendshi = rectangle(4,5)
trekendshi = triangle(6,4)
paralelogrami = Paralelogrami(3,8)


