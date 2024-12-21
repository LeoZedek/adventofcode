with open("input") as file:
  data = file.read().strip()

class File:
  def __init__(self, id, size):
    self.id = id
    self.size = size

class FreeSpace:
  def __init__(self, size):
    self.size = size
    self.fill = []

disk = []
files = []
free_space = []
for index, char in enumerate(data):
  if index % 2 == 0:
    disk.append(File(index // 2, int(char)))
  else:
    disk.append(FreeSpace(int(char)))

i_free_space = 1
i_file = len(disk) - 1


while i_free_space < i_file:
  free_space = disk[i_free_space]
  file = disk[i_file]
  
  space_filling = min(free_space.size, file.size)

  free_space.fill.append(File(file.id, space_filling))
  free_space.size -= space_filling
  file.size -= space_filling

  if free_space.size == 0:
    i_free_space += 2
  elif file.size == 0:
    i_file -= 2



multiplier = 0
r = 0
for index, elt in enumerate(disk):
  if index % 2 == 0:
    for d in range(elt.size):
      r += multiplier * elt.id
      multiplier += 1
  else:
    for file in elt.fill:
      for d in range(file.size):
        r += multiplier * file.id
        multiplier += 1

print(r)