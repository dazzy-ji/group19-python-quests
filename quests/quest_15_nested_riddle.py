#!/usr/bin/python3
# Quest 15: The Nested Riddle
direction = input("Do you go left or right? ")
if direction == "left":
    action = input("Do you swim or wait? ")
    if action == "swim":
        print("You find a treasure chest! You win!")
    else:
        print("You wait too long and the tide rises. Game over!")
else:
    print("You walk right into a dead end. Turn back!")
