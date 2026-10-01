import random

def guess(x):
  guess = x
  random_number = random.randint(1, 100)
  guess_counter = 1
  low = 1
  high = 100
  while guess != random_number:
    guess_counter += 1
    if guess < random_number:
      low = guess
      guess = int(input(f"Guess too low. Please try again (between {low} & {high}): "))
    elif guess > random_number:
      high = guess
      guess = int(input(f"Guess too high. Please try again (between {low} & {high}): "))
  print(f"Good work! You correctly guessed the number ({random_number}). It took you {guess_counter} guesses.")

answer = input("Would you like to play a guessing game? (Y/N): ").lower()

if answer == "y":
  user_guess = int(input("Please guess a number between 1 & 100 (inclusive): "))
  guess(user_guess)
else:
  print("Okay. Goodbye.")