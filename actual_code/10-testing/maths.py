import utils.strings

def add(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Both arguments must be numbers.")
  return a + b


"""
1. Gather test list: 
- Adds numeric
  - Big numbers
  - Small numbers
  - Decimals
  - Negatives

- Raises errors if they aren't numbers
"""