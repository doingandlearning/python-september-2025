file = open("test.txt") # handle - a way to manipulate the file
file.close()


with open("test.txt") as file: # context handler! 
  print(file.read())

# idiomatic python -> Pythonic way!

# closes the file for us!!