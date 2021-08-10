import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")

    attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break

    print("Guess again.")