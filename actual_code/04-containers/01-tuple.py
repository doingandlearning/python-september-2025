empty_tuple = ()  # creates a tuple

#          0         1        2        3        4
names = ("Sam", "Florence", "Lipi", "Neha", "Mohammed")
print(type(names))
print(names)
print(len(names))

print(names[3])  # prints out the person in position (or index)
# print(names[10]) # print beyond the index
print(names[1:3])  # everyone from the first number upto but not including the second number
print(names[:3])
print(names[3:])  # sublisting - subindexing

print("Neha" in names)
print("Kevin" in names)  # check for membership in my tuple

# user_name = input("What's your name?")

# if user_name in names:
#   print("Welcome!")
# else:
#   print("Unauthorized")

for name in names:
  print(f"{name} is on our list")


nested_names = ("Jemima", "Steph", "Rani", names, "Saifur",)
print(nested_names)

# i want to print Neha

print(nested_names[3][3])

print(nested_names.count("Jemima"))
print(nested_names.count("Kevin"))

print(nested_names.index("Jemima"))

if "Kevin" in nested_names:
  print(nested_names.index("Kevin"))