class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, and i am {self.age} years old")

p1= Person("Olti", 18)

p1.greet()
