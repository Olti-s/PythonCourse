class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def calculate_area(self):
        return self.length * self.width

    def calcualte_perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calcualte_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

