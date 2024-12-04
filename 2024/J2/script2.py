def isSafe(reports):

  if reports[0] == reports[1]:
    return False

  increased = reports[0] < reports[1]

  for i in range(1, len(reports)):
    distance = reports[i-1] - reports[i]
    if increased:
      distance *= -1
    
    if not(1 <= distance and distance <= 3):
      return False

  return True

with open("input") as file:
  data = file.readlines()

r = 0

for reports in data:
  tab = list(map(int, reports.split()))

  safe = False

  for i in range(len(tab)):
    temp = tab.copy()
    temp.pop(i)
    if isSafe(temp):
      safe = True

  r += safe

print(r)
