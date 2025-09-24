import csv

# with open("movies.csv") as file:
#   reader = csv.reader(file)
#   next(reader) # skips the header row
#   for title, year, director, genre in reader: # unpacking
#     print(f"{title} ({year}) was directed by {director}. Genre: {genre}")

with open("movies.csv", "a") as file:
  writer = csv.writer(file)
  writer.writerow(["Nobody 2", "2025", "Timo Tjahjanto", "Action comedy"])