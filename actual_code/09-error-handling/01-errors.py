"""
1. Developer errors - not closing brackets, using a method that doesn't exist!

- Logic errors
- Do want our programs to crash!! Don't want errors to silently occur!

2. Real-world errors - deployed errors

- user input
- database is down
- api is down

Error <> Exception -> used interchangably

SyntaxError
FileNotFoundException

try:
  risky code! never trust users! file system, querying a db, ... 
  raise Exception/Error  (throw)
except:
  handle the errors we are expecting

"""
