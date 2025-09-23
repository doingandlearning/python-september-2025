# print("Hello!")
# input("")
# set()
# list()
# int()

def print_hello():
  print("=" * 20)
  print("Hello")
  print("=" * 20)

# print_hello()

def say_hello_to_user(name, seperator="=", width=20):
  """
  A function to say hello to a user with seperators
  Arguments:
    - name: str
    - seperator
    - width
  """
  if not isinstance(width, int) or not isinstance(width, float):
    raise Exception("Width has to be a number")
  print(seperator * width)
  print(f"Hello {name}")  # formatted string -> {}  => "Hello " + name
  print(seperator * width) 

say_hello_to_user("Sam")
say_hello_to_user("Sam", "*", 40)
say_hello_to_user("Sam", width=10)
say_hello_to_user(name="Sam", seperator="%", width=100)
# say_hello_to_user()