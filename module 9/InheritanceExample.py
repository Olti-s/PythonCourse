#class Superclass:

#class Subclass(Superclass): # ketu subclasa trashegon prej superklasabe

class Animal:  #this is a general
    def eat(self):
        print("This animal eats")
    def sleep(self):
        print("it sleeps")

class Bird(Animal):
    def fly(self):
        print("it flyes in the sky")
    def sings(self):
        print("it sings")


bilbili=Bird()
bilbili.fly()