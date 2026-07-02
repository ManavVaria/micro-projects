import random

lower_bound = 1
upper_bound = 10
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
