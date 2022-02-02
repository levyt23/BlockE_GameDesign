import os
os.system('clear')
import random
#define rock, paper, and scissors
#define variables
#make a menu
#loop it when the player gets it wrong
#loop game if the player wins 
#make sure the computer's turns are randomized when the game is going

def menu():
    print('########################################')
    print('#         guess a number menu          #')
    print('#           choice  1: 1-10            #')
    print('#           choice  2: 1-50            #')
    print('#           choice  3: 1-100           #')
    print('########################################')

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        