count = 1

def increase_count():
  global count   # gives the function WRITE access to the variable outside of itself!
  # While possible - not advisable! Try to avoid global!
  count = count + 1

increase_count()
# Functions have read access to variables outside of themselves.

def print_count(count):  # variable shadowing
  print(count)
  my_function_variable = True # anything created inside the function stays there
  # unless we return!
  return my_function_variable 

print(f"Before function: {count}")
result = print_count(10)  # we capture return values to variables which we name ourselves
print(f"After function: {count}")

print(result)
print(result)


