class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name
    def set_name(self, name):
       self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self,age):
      self.__age = age


Student1 = Student("Elmedina", 17)

print("Name", Student1.get_name())
Student1.set_name("orhidea")
print("Uptade name", Student1.get_name())
