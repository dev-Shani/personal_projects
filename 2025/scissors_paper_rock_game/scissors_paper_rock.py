import random

def user_wins(player, opponent):
  # returns True if player wins
  # s > p, p > r, r > s

  if (player == "s" and opponent == "p") \
  or (player == "p" and opponent == "r") \
  or (player == "r" and opponent == "s"):
    return True

def game():
  user_move = input("Please pick scissors (s), paper (p), or rock (r): ")
  computer_move = random.choice(["s", "p", "r"])
  
  if user_move == computer_move:
    print(f"You and the computer have both chosen {user_move}, so it's a draw.")

  elif user_wins(user_move, computer_move):
    print(f"You have chosen {user_move}, and the computer chose {computer_move}, so you win!")

  else:
    print(f"You chose {user_move}, and the computer chose {computer_move}, so you lose!")

play_loop = True

while play_loop:
  answer = input("Would you like to play a game of scissors, paper, rock? (y/n): ")
  if answer == "y":
    game()
    play_loop = False
  elif answer == "n":
    print("Okay. Godbye.")
    play_loop = False
  else:
    print("Incorrect input, please try again.")
    continue