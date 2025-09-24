file = open("test.txt") # handle - a way to manipulate the file

# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# fwt  255 -> all of the ascii table -> simplified chinese, kanji, ...  

file_contents = file.read()  # searching the file, getting data ... it's big quickly!!
print(file_contents)
print(type(file_contents))

file.seek(0) # move the cursor to the start of the file
file_contents = file.readlines()
print(file_contents)
print(type(file_contents))

file.seek(0)

line = file.readline()

while line:
  print(line)
  line = file.readline()

file.close()