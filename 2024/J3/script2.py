import re

with open('input') as file:
  data = file.readlines()

r = 0

do = True

for line in data:
  if do:
    split = line.split('do()')
  else:
    split = line.split('do()')[1:]
  for after_do in split:
    before_dont = after_do.split("don't()")[0]
    matches = re.findall("mul\([0-9]+,[0-9]+\)", before_dont)
    do = before_dont == after_do
    for match in matches:
      number1, number2 = match.split(',')
      r += int(number1[4:]) * int(number2[:-1])

print(r)