import re

with open('input') as file:
  data = file.readlines()

r = 0

for line in data:
  matches = re.findall("mul\([0-9]+,[0-9]+\)", line)

  for match in matches:
    number1, number2 = match.split(',')
    r += int(number1[4:]) * int(number2[:-1])

print(r)