class Animal:
    def __init__(self,name):#shembulli per nje konstruktor dhe nje variable e cila po inicohet per kete class
        self.name=name

    def sound(self):
        print("Some generic animal sound")
    def descrtiption(self):
        print(f"This is an animal named {self.name}")

class Dog(Animal):
    def __init__(self, breed,name): # ketu eshte insturoktori i klases dhe ketu esgte variabla eklases
        self.breed=breed  #variabla qe vlene vetem per kete eklase
        super().__init__(name) # ketu thirret konstruktori i superklases
    def sound(self):
        print("Woof Woof")

    def descrtiption(self):
        super().descrtiption()
        print(f"Breed:{self.breed}")

class Cat(Animal):
    def __init__(self, color, name):  # ketu eshte insturoktori i klases dhe ketu esgte variabla eklases
        self.color = color
        super().__init__(name)

    def sound(self):
        print("Meow Meow")

    def description(self):
        super().descrtiption()
        print(f"Color:{self.color}")




rex=Dog("golden Retriever","Rex")
rex.sound()
rex.descrtiption()


spaky=Cat("black","Tom",)
spaky.sound()
spaky.description()

