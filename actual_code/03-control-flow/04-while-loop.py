user_input = input("What is your password? ")
attempts_tried = 0
is_out_of_tries = False

while user_input != "password123":  # don't know how many times!
    print("Sorry - that was wrong - try again!")
    attempts_tried = attempts_tried + 1
    if attempts_tried > 3:
      print("All out of tries!")
      is_out_of_tries = True
      break
    user_input = input("What is your password? ")

if not is_out_of_tries:
    print("Here are the secret documents.")