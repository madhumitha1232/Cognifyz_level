import random

def guess_number():
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    number = random.randint(low, high)
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != number:
        if guess > number:
            print("Too high!")
        else:
            print("Too low!")
        guess = int(input("Guess again: "))
    print("Congratulations! You guessed the number correctly.")

guess_number()
