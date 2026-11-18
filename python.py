
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = input("\nEnter your choice: ")

# Set difficulty level
if choice == "1":
    chances = 10
    level = "Easy"
elif choice == "2":
    chances = 5
    level = "Medium"
elif choice == "3":
    chances = 3
    level = "Hard"
else:
    print("Invalid choice! Please restart the game.")
    exit()

# Generate random number
secret_number = random.randint(1, 100)

print(f"\nGreat! You have selected the {level} difficulty level.")
print("Let's start the game!")

attempts = 0

# Game loop
while attempts < chances:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            break

        elif guess > secret_number:
            print(f"Incorrect! The number is less than {guess}.")

        else:
            print(f"Incorrect! The number is greater than {guess}.")

    except ValueError:
        print("Please enter a valid number.")

else:
    print("\nGame Over! You've used all your chances.")
    print(f"The correct number was {secret_number}.")
