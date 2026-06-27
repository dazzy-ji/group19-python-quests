secret_code = 42
max_attempts = 3
attempts = 0

print("Your task is to find the secret code")
print(f"You have only {max_attempts} to accomplish this task. ENJOY!")
print("Hint: The secret code is a number between 0 and 100")

while attempts < max_attempts:
    user_guess = int(input("Enter your guess: "))
    attempts = attempts + 1
    remaining = max_attempts - attempts

    if user_guess == secret_code:
        print(f"YOU HAVE CRACKED IT. THE SECRET CODE IS: {secret_code}")
        break
    elif user_guess >= 0 and user_guess <= 40:
        print(f"NOT YET THERE. HINT: NUMBER IS GREATER THAN 40. TRY AGAIN")
    elif user_guess >= 50 and user_guess <= 100:
        print(f"NOT YET THERE. HINT: NUMBER IS LESS THAN 50. TRY AGAIN")
    elif user_guess >= 40 and user_guess <= 50:
        print(f"YOU ARE VERY CLOSE. HINT: NUMBER IS BETWEEN 40 AND 50. TRY AGAIN")
    else: 
        print("Enter a valid option")

    print("Remaining attempts: ",remaining)
else:
    print(f"Out of attempts, the secret code is {secret_code}")
