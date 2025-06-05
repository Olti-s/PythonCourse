class Dog:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes the sound : woof")

class Cat:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes the sound : mauw")

class Bird:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes the sound : ciu")


qeni= Dog("Reksi")
macja =Cat("tom")
zogu =Bird("tweet")

for kafsha in (qeni ,macja, zogu):
    kafsha.sound()