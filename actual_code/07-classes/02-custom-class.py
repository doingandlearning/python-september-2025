user1 = {
  "name": "Andrew",
  "role": "Senior System Engineer",
  "previous_languages": ["C++", "Basic"]
}

user2 = {
  "name": "Lipi",
  "role": "Core data team",
  "previous_languages": ["DBT", "Python"]
}

for user in [user1, user2]:
  print(user["name"])

class User:  #UserNameClassThingy  Pascal Case  userNameClassThingy Camel Case
  # dunder - double underscore  - dunder init
  def __init__(self, provided_name, provided_role, provided_languages):
    self.name = provided_name
    self.role = provided_role
    self.languages = provided_languages

  def __repr__(self):
    return f"User(provided_name='{self.name}', provided_role='{self.role}', provided_languages={self.languages})"

  def add_language(self, new_language):
    self.languages.append(new_language)

  def language_length(self):
    return len(self.languages)


user3 = User("Steph", "Mechanics Workshop", ["C", "C++", "Python"])
print(user3.name)
print(user3.languages)
user3.add_language("TypeScript")
print(f"{user3.name} is skilled in {user3.language_length()} languages. They are {', '.join(user3.languages)}.")


print(user1)  # Protocols ... __str__   __repr__
print(user3)

user4 = User("Sam", "Network Engineer", ["VS"])
print(user4.name)

# user3.name = "Steph"
# user3.role = "Mechanics Workshop"
# user3.previous_languages = ["C", "C++", "Python"]

# print(user3.name)

# user4 = User()
# print(type(user4))