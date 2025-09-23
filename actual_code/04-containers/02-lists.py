empty_list = []   # array

print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo", True, 12, 12.3]

print(len(beatles))
print(beatles[1])

print("George" in beatles)
print("Steph" in beatles)

for band_member in beatles:  # for number in range(5),  for name in names
  print(f"{band_member} is a member of the Beatles")

beatles.append("Steph")  # add one member to the end of the list
print(beatles)

beatles.extend(("Andrew", "Jemima", "John"))
print(beatles)

print(beatles[0])

print("=" * 25)
while "John" in beatles:  # safety feature - remove safely!
  print(beatles)
  beatles.remove("John")
  print(beatles)

print("=" * 25)
print(beatles[0])

beatles.reverse()
print(beatles)

beatles.sort()
print(beatles)

band_member = beatles.pop()

print(band_member)
print(beatles)  # LIFO

bands = [
    ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],      # Queen
    ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
    ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"],   # The Rolling Stones
    ["Beyoncé", "Kelly Rowland", "Michelle Williams"],                   # Destiny's Child
    ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # The Beatles
    ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Phil Selway"],  # Radiohead
    ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."],            # U2
    ["Chris Martin", "Guy Berryman", "Jonny Buckland", "Will Champion"], # Coldplay
    ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri"],       # Blondie
    ["Jack White", "Meg White"]                                          # The White Stripes
]

print(bands[1][2])  # Dave Grohl
nirvana = bands[1]  # assign by value, assign reference
nirvana.append("Neha")
print(nirvana)
print(bands)