# nesting -> reduce this!

is_sunny = True
temperature_in_celcius = 24
has_airconditioning = True

if is_sunny:
  if temperature_in_celcius > 20:   # == !=  > <  >=  <=
    if has_airconditioning:
      print("Whack the airconditioning (sorry planet)")
    else:
      print("Try not to melt - it's hot out there!")
  print("It's nice outside!")
else:
  print("I like it when it's not sunny!")

# cyclomatic complexity