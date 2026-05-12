# ============================================================
# PF Python - Project: Mad Libs Game
# ============================================================

adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
country = input("Enter a country name: ")
exception = input("Enter an exception/surprise: ")
profit = input("Enter a profit value: ")

madlibs = (f"Computer is a good programming {adj}! It is too {noun}. "
           f"It is used by all of the {country}! "
           f"I like it too {exception}! It has so much {profit}!")
print("\n" + madlibs)


# ============================================================
# PF Python - Project: Guess the Number (Computer picks)
# ============================================================

import random

def guess_number(x):
    """Computer picks a random number, user tries to guess it."""
    number_to_guess = random.randint(1, x)
    user_guess = 0
    attempts = 0

    print(f"\nGuess a number between 1 and {x}")

    while user_guess != number_to_guess:
        user_guess = int(input("Your guess: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")

    print(f"Correct! You guessed it in {attempts} attempts.")

guess_number(10)


# ============================================================
# PF Python - Project: Guess the Number (User picks, Computer guesses)
# ============================================================

def computer_guess(x):
    """User thinks of a number, computer tries to guess it."""
    low = 1
    high = x
    feedback = ''

    print(f"\nThink of a number between 1 and {x}. Press Enter when ready.")
    input()

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"The computer guessed your number: {guess}!")

computer_guess(10)
