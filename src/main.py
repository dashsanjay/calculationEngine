from substraction import *
from addition import *
from multiplication import *
from division import *
from exponential import *
import math

#Python program to perform Addition Subtraction Multiplication
# Division and Exponential of two numbers

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/,# : ")

result = float (0)
if ch == '+':
    result = add(a, b)
elif ch == '-':
    result = sub(a, b)
elif ch == '*':
    result = mul(a, b)
elif ch == '/':
    result = div(a, b)
elif ch == '#':
    result = exponential(a, b)
else:
    print("Input character is not recognized!")

print(a, ch , b, ":", result)