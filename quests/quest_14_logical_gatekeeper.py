#!/usr/bin/python3
# Quest 14: The Logical Gatekeeper
age = int(input("How old are you? "))
gold = int(input("How many gold coins do you have? "))
if age >= 18 and gold >= 20:
    print("Welcome to the club!")
else:
    print("Sorry, you cannot enter.")
