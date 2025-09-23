def add(first_number, second_number):
  return first_number + second_number

result = add(1,2)
print(result)

print(add(2,3))

def get_readings_from_user():
  readings = []

  while True:
    reading = input("Please enter reading (q to quit)")
    if reading == "q":
      break
    readings.append(reading)

  return readings

results = get_readings_from_user()
print(results)