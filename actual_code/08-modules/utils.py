"""
This is a utils module. Leave stuff here until you find a better home for it.
"""

def printer(text):
  print("Here is the message")
  print(text)
  print("Did I do okay?")
  print("=" * 20)

class Shape:
  def __init__(self, type):
    self.type = type

  def __str__(self):
    return f"Shape of type {self.type}."



default_shape = Shape("circle")

def main():
  print(f"Welcome to the utils module - {__name__}")
  printer(default_shape)

if __name__ == "__main__":
  main()