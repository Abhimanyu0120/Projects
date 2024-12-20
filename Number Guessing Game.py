
import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game! 🎉")
    
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts! 🎊")

number_guessing_game()