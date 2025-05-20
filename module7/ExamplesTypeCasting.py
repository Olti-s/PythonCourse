age=25
age_As_string=str(age)
print(age_As_string, " of type", type(age_As_string))


print(bool(0)) #false beacuse 0 if false boolean
print(bool(42)) # true beascuse 44442 translates as 1

print(bool(""))
print(bool("Hello"))

#implicit TypeCasting
x=32
y=5.3
resultati=x+y
print(resultati,"of type", type(resultati))

a=5
b="3"
resultati1=a*int(b)
print(resultati1,"of type", type(resultati1))

c=4
resultati2="Hello"*c
print(resultati2,"of type", type(resultati2))



#get two numbers from user input and sum them up

user=int(input("first number:"))
user1=int(input("second number:"))
resultati3=user+user1
print(resultati3)