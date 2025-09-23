user_dict = {"name": "Jemima", "team": "Infosec"}

print(user_dict["name"])
# print(user_dict["not-there"])
print(user_dict.get("name"))
print(user_dict.get("not-there", "Anonymous"))

print(user_dict.keys())
print(user_dict.values())
print(user_dict.items())