def calculate_area(length, width):
    return length * width


def calcualte_perimeter(length, width):
    return 2 * length * width

length = 5
width = 3
area = calculate_area(length,width)
perimeter = calcualte_perimeter(length,width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")