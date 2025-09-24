def divide(a,b):
  return a/b

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
except:
  print("Something went wrong. Please try again.")

