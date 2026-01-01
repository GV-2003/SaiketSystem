import random

# Number Guessing Game

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break
