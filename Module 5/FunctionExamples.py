from email.policy import default

from pyexpat.errors import messages

total=0

for number in range(1,11):
    if number%2==0:
        total+=number
print("THe sum of even numbers from 1 to11 is",total)


#this is defining a function. Keyword def - in python defines functions. greet- emri i funksionit
def greet():
    print("hello")
 #this is how we use the function
greet()

def greet_person(name):
     print("hello",name)

greet_person("alma")

def shuma(x,y): #this type smth in this case a number
    z=x+y
    return z

resultati=shuma(3,4)
print("3+4=",resultati)

#local variable

def greet(name):
    message=f"hello,{name}!"
    print(message)
greet("alma")

#print(message) this outputs an error beacuse the message variable is defined only for the function


#argumentet edhe definimi ityre

def greet_person(name,greetting="heelo"):
    message=f"{greetting}, {name}"
    return message

default_greeting=greet_person("Alma")
print(default_greeting)
custom_greeting=greet_person("alma","Goodmoring")
print(custom_greeting)

# global variable

pershendetje="hi"
def greet_people(name):
    global pershendetje
    return f"{pershendetje}, {name}"
variabla=greet_people("Alma")
print(variabla)




















