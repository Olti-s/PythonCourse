#Error Handling Try, Except, Finally
#Try - writting of the needed code
#Except - what happens if an error happens in the try part
#Finally - pjesa qe bohet run gjthimon
from module7.ExamplesTypeCasting import resultati

#This is dedicated for errors that programmers do not predict

#shembulli1
# try:
#     print("pjesto dy nr")
#     nr1=int(input("Shkurani nr1:"))
#     nr2= int(input("Shkurani nr2:"))
#     resltati=nr1/nr2
#     print("Rezultati:",resltati)
# except ZeroDivisionError:
#     print("ke gabu per shkak qe je duke pjestuar me 0")

#second example

fruits={
    "apples":5,
    "Banana":6,
    "orange":7
}
try:
    print(fruits["cherry"])
except KeyError:
    print("this hey doses not exist in the dictonary")




#third example
text="This is not a number"
try:
    text_to_int=int(text)
except Exception as e:
    print("An error occorred while parsing the data:",e)


#forth example
# try:
#     resultati:10/0
# except ZeroDivisionError:
#     print("Division by  zero error occorred")
# else:
#     print("Divison successful, Result",resultati)

#fifth example
try:
    resultati=10/2
except ZeroDivisionError:
    print("Divison by zero error occorred")
finally:
    print("Thsi part of code always runs")
