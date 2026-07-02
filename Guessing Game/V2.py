import random

lower_bound = 1
print("Welcome to the Guessing Game!")
choice = int(input("Choose the difficulty level (1- Easy, 2- Medium, 3- Hard): "))

if choice == 1:
    upper_bound = 10
elif choice == 2:
    upper_bound = 50
elif choice == 3:
    upper_bound = 100
else:
    print("Invalid choice. Please choose a valid difficulty level.")

answer = random.randint(lower_bound, upper_bound)
attempts = 0

while True:
    guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
    attempts += 1
    if guess < answer:
        print("Too Low! Try again.")
    elif guess > answer:
        print("Too High! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number {answer} in {attempts} attempts.")
        break