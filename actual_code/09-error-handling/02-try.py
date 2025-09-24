def divide(a,b):
  try:
    # raise ArithmeticError()
    return a/b
  except ZeroDivisionError:
    print("You tried to divide by zero - better luck next time!")

def get_user_numbers():
  try:
    first_number = int(input("What's your first number? "))
    second_number = int(input("What's your second number? "))
    return first_number, second_number
  except ValueError:
    print("Oi! That's not a valid number. Try again.")
    return get_user_numbers()

user_numbers = get_user_numbers()

try:
  print(divide(user_numbers[0], user_numbers[1]))
except ValueError:  # at least one except to go with a try!
  print("Something went wrong. I got a ValueError.")
except Exception as exp:
  print("Something unexpected went wrong.")
else: # optional
  print("Only runs if there were no errors!")
finally: # optional!
  print("Whether or not there's an error!") # cleanup!
