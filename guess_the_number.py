# Import random module
import random

print("----- GUESSING GAME -----")
print("Please enter a min and a max number")
print()
# Choose an upper limit and a lower limit

while True:
    try:
        lower_limit = int(input("Enter min number: "))
        upper_limit = int(input("Enter max number: "))
        if lower_limit < 0:
            print("I can only accept positive numbers.")
        else:
            random_number = random.randint(lower_limit, upper_limit)
            break
    except ValueError:
        print("Hey, insert a min and a max number!")

# Select a random number between the upper limit and the lower limit
# The function takes the upper limit and the lower limit as parameters, and picks a number between the two numbers
# Variables can be declared and assigned at the same time

print()
print(f"You will have to choose a number between {lower_limit} and {upper_limit}")
print()

# Assign a variable 'chances' that will act as the counter for a loop
# The user will have to input his guess so we assign his guess into a variable
chances = 0

while True:
    try:
        while chances < 8:
            chances += 1
            guess = int(input("Enter your guess: "))
            if guess < lower_limit or guess > upper_limit:
                print(f"Hey, insert a number between {lower_limit} and {upper_limit}!")
            elif random_number == guess:
                print(f"Congratulations, you did it. The number was {random_number}.")
                break
            elif guess < random_number:
                print("You guessed a small number.")
            elif guess > random_number:
                print("You guessed a large number.")
            if chances == 7:
                print("\nYou ran out of chances")
                print(f"\nThe number was {random_number}.")
                print("Better luck next time")
                break
        break
    except ValueError:
        print(f"Hey, insert a number between {lower_limit} and {upper_limit}!")


print()
