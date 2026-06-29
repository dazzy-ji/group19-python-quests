# Quest 18: The Loop of Riddles
# A guessing game that runs until the user inputs the correct secret number

secret_number = 7

while True:
    try:
        guess = int(input("Guess the secret number: "))
        if guess == secret_number:
            print("Correct! You solved the riddle.")
            break
        else:
            print("Wrong guess! Try again.")
    except ValueError:
        print("Please enter a valid integer.")
