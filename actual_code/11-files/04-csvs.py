import csv

# with open("movies.csv") as file:
#   reader = csv.reader(file)
#   next(reader) # skips the header row
#   for title, year, director, genre in reader: # unpacking
#     print(f"{title} ({year}) was directed by {director}. Genre: {genre}")

# with open("movies.csv", "a", newline='') as file:
#   writer = csv.writer(file)
#   writer.writerow(["Nobody 2", "2025", "Timo Tjahjanto", "Action comedy"])

import shutil
shutil.copy("movies.csv", "movies_backup.csv")

with open("movies.csv", "r") as file:
  lines = file.readlines()

with open("movies.csv", "w") as file:
  for line in lines:
    if "Nobody 2" in line:
      file.write(line.replace("2025", "2024"))
    else:
      file.write(line)
