from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @abstractmethod

    def calculate_bmi(self, weight, height, bmi):
        pass
    @abstractmethod

    def get_bmi_categoty(self):
        pass
    @abstractmethod

class Adult(Person):
    def calculate_bmi(self, weight, height, bmi):
        bmi=(self.weight / self.height)
        return bmi



    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5 :
            print("Underweight")
        elif 18.5>bmi<24.9 :
            print("Normal")
        elif 24.9 > bmi < 29.9:
            print("Overweight")
        elif bmi < 29.9 :
            print("Obese")
        else:
            raise ValueError("Invalid operation")
    def print_info(self):
        print(f"{self.name}, Age:{self.age} ,Weight:{self.weight}, Height:{self.height}  ")

class Child(Person):
    def calculate_bmi(self, weight, height, bmi):
        bmi = (self.weight / self.height) * 1.3
        return bmi

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            print("Underweight")
        elif 14 > bmi < 18:
            print("Normal")
        elif 18 > bmi < 24:
            print("Overweight")
        elif bmi < 24:
            print("Obese")
        else:
            raise ValueError("Invalid operation")

        def print_info(self):
            print(f"{self.name}, Age:{self.age} ,Weight:{self.weight}, Height:{self.height}  ")









