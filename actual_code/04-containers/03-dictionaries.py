# () => tuple
# [] => list
# {} => dict

empty_dict = {}
print(type(empty_dict))  # dict => dictionary

user_dict = {
  "name": "Jemima",   # key: value
  "team": "Infosec",
  "location": "London",
  "previous_programming": ["Java", "Powershell"]
}

print(user_dict["name"])
print(user_dict.keys())  # .keys() -> list of the keys
print("London" in user_dict)  # This checks keys and not values 
print("location" in user_dict)

for value in user_dict.values():  # .values() -> a list of hte values
  print(value)

for value in user_dict.items():  # .items() -> a list of tuples of (key, value)
  print(value)

user_dict["aim"] = "Get to grips with the basics again"

print(user_dict)

del user_dict["location"]

print(user_dict)


bands = {
  "Queen":  {"singer": "Freddie Mercury", 
            "guitarist": "Brian May", 
            "bassist": "Roger Taylor", 
            "drummer": "John Deacon"},      # Queen
  "Nirvana":  ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
   "The Rolling Stones": ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"]
}

print(bands["Queen"]["singer"])

ditto = {
  "abilities": [
    {
      "ability": {
        "name": "limber",
        "url": "https://pokeapi.co/api/v2/ability/7/"
      },
      "is_hidden": False,
      "slot": 1
    }]
}

print(ditto["abilities"][0]["ability"]["name"])