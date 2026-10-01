from time import sleep

def main():
  
  user_password = "PW1243"
  incorrect_password_counter = 0
  entered_password = input("Please enter your password: ")

  validate_password(entered_password, user_password, incorrect_password_counter)

def timeout(t: int) -> None:
  '''
  Causes program to pause for <t> seconds and prints countdown timer.
  '''

  while t:
    seconds_message = "1 second" if t == 1 else f"{t} seconds"
    print(f"\rPlease wait {seconds_message}.", end="", flush=True)
    t -= 1
    sleep(1)

def validate_password(password_to_check: str, correct_password: str, incorrect_attempts: int) -> None:
  while password_to_check != correct_password:
    incorrect_attempts += 1
    remaining_tries_message = "1 try remaining" if incorrect_attempts == 4 else f"{5 - incorrect_attempts} tries remaining"
    if incorrect_attempts < 5:
      password_to_check = input(f"Incorrect password. {remaining_tries_message}. Please try again: ")
    else:
      print("Too many incorrect tries.")
      incorrect_attempts = 0
      timeout(10)
      password_to_check = input("\nPlease enter your password: ")
      continue
  print("Password accepted.")

if __name__ == "__main__":
  main()