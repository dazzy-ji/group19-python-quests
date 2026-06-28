#!/usr/bin/python3
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def modulus(a, b):
    return(a % b)

firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
operation = input("Operation: (add, subtract, multiply, divide, modulus): ").lower()

if operation == "add":
    result = firstNumber + secondNumber
elif operation == "subtract":
    result = firstNumber - secondNumber
elif operation == "multiply":
    result = firstNumber * secondNumber
elif operation == "divide":
    result = firstNumber / secondNumber
elif operation == "modulus":
    result = firstNumber % secondNumber
else:
    print("Invalid option")

print("Result: ", result)
