
def calculate(nr1,nr2,operatori):
    if operatori =="+":
        return nr1+nr2
    elif operatori=="-":
        return nr1-nr2
    elif operatori=="*":
        return nr1*nr2
    elif operatori=="/":
        return nr1/nr2
    else:
        raise ValueError("Invalid operation")


try:
    num1=float(input("enter first number"))
    num2=float(input("Enter the second number"))
    operatori=input("enter an operation:+,-,*,/")
    resultati=calculate(num1,num2,operatori)
    print(f"The result of {num1} {operatori} {num2}:{resultati}")

except ValueError as e:
    print(f"Invalid input {e}")

except ZeroDivisionError as e:
    print(f"cannot dive by 0 {e}")

except Exception as e:
    print(f"error {e}")

finally:
    print("End of the program")
    