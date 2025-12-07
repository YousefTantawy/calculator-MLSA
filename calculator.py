from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
choice = int(input("Enter what operation you'd like to write\n1.Addition\n2.Subtraction" \
"\n3.Multiplication\n4.Division\nAnswer: "))

if (choice == 1):
    Addition(num1, num2) 
elif(choice == 2):
    Subtraction(num1, num2)
elif(choice == 3):
    Multiplication(num1, num2)
elif(choice == 4):
    Division(num1, num2)
else:
    print("Incorrect choice/number inputted")

