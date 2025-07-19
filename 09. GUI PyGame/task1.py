""" Task 1. Write a game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries.
The program reads the numbers entered by the user and prompts the user
whether the guessed number is greater or less than the number entered by the
user. The game must continue until the user has used 10 attempts and guessed
the number. If the user guessed the number, the program prints a
congratulatory message, and if 10 attempts have been exhausted and the user
did not have time to guess the number, then the corresponding message is
displayed.
(to perform the task, you need to import the random module,
and from it the randint() function)
"""

from random import randint

def number_guessing_game():
    secret_number = randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt} of {attempts}")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempt} attempts!")
            return
        elif guess < secret_number:
            print("The secret number is higher than your guess.")
        else:
            print("The secret number is lower than your guess.")

    print(f"\nGame over! You didn't guess the number. The secret number was {secret_number}.")


number_guessing_game()
