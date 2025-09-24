# ValueError, SyntaxError, ZeroDivisionError

class BBCError(Exception):
  """This is a custom BBCError"""


try:
  raise BBCError("Something went wrong.")
except ValueError:
  print("Whoops!")
except BBCError:
  print("Something BBC went wrong!")