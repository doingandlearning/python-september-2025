def add(a, b, c=0, d=0):
  return a + b + c + d

def add(*numbers):  # *args
  total = 0
  for number in numbers:
    total = total + number
    # total += number
  return total


print(f"Adding 1 and 1 gets {add(1,1)}")
print(f"Adding 1 and 4 gets {add(1,4)}")
print(f"Adding 1 and 2 and 3 gets {add(1,2,3)}")
print(f"Adding 1 and 2 and 3 and 4 gets {add(1,2,3,4)}")
print(add())
print(add(1,2,3,4,5,6,7,8,9,10,1,2,2,3,4,5,6,7,5,4,3,4,56,76,5,4,4,5,6,5,3))