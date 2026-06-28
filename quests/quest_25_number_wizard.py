#!/usr/bin/python3
number = 7
max_attempts = 5
attempts = 0

print(f"You only have {max_attempts} attempts to find the correct number!")

while attempts < max_attempts:
    user_guess = int(input("Enter a number between 0 and 10: "))
    attempts += 1
    remaining = max_attempts - attempts

    if user_guess == number:
        print(f"Congratulations! The correct guess is {number}")
        break
    elif user_guess < number:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")

    print("Remaining attempts:", remaining)
else:
    print(f"Out of attempts! The number was {number}.")
