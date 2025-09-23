# Pythonic -> Idiomatic Python
# It's not required!

number_list = [1,2,3,4,5,6,7,8,9,10]

doubled_list = []

for number in number_list:
  if number > 5:
    doubled_list.append(number * 2)

print(doubled_list)

# List Comprehension
doubled_list = [number * 2 for number in number_list]  # mapping!
doubled_list = [number * 2 for number in number_list if number > 5]  # mapping and filtering!
print(doubled_list)