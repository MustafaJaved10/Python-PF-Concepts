# ============================================================
# PF Python - Project: Rock Paper Scissors Game
# ============================================================

import random

item_list = ["ROCK", "PAPER", "SCISSOR"]
user_input = input("Enter your move (ROCK / PAPER / SCISSOR): ").upper()
comp_input = random.choice(item_list)

print(f"User: {user_input}  |  Computer: {comp_input}")

if user_input == comp_input:
    print("TIE!")
elif user_input == "ROCK":
    if comp_input == "PAPER":
        print("Computer wins - Paper covers Rock")
    else:
        print("You win! - Rock smashes Scissor")
elif user_input == "PAPER":
    if comp_input == "SCISSOR":
        print("Computer wins - Scissor cuts Paper")
    else:
        print("You win! - Paper covers Rock")
elif user_input == "SCISSOR":
    if comp_input == "PAPER":
        print("You win! - Scissor cuts Paper")
    else:
        print("Computer wins - Rock smashes Scissor")
else:
    print("Invalid input! Please enter ROCK, PAPER, or SCISSOR.")
