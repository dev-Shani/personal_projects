import random

def computer_guess(x, y):
  guess_counter = 1
  low = 1
  high = 100
  game_over = False
  guess = random.randint(x, y)
  while game_over != True:
    user_answer = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
    if user_answer == "h":
      guess_counter += 1
      high = guess - 1
      guess = random.randint(low, high)
    elif user_answer == "l":
      guess_counter += 1
      low = guess + 1
      guess = random.randint(low, high)
    elif user_answer == "c":
      if guess_counter == 1:
        print(f"Yay! The computer guessed your number ({guess}) correctly! It only took {guess_counter} guess.")
      else:
        print(f"Yay! The computer guessed your number ({guess}) correctly! It took {guess_counter} guesses.")
      game_over = True
    else:
      print("Incorrect input. Please try again.")
      continue

answer = input("Would you like to play a guessing game? (Y/N): ").lower()
answer2 = ""
loop = True

if answer == "y":
  while loop:
    answer2 = input("Please think of a number between 1 & 100 (inclusive). Have you got it? (Y/N): ").lower()
    if answer2 == "y":
      computer_guess(1, 100)
      loop = False
    else:
      continue
else:
  print("Okay. Goodbye.")