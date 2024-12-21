with open("test") as file:
  data = file.read().strip()

class File:
  def __init__(self, id, size):
    self.id = id
    self.size = size
    self.originalSize = size

  def __repr__(self):
    return "id : " + str(self.id) + "; size : " + str(self.size) +  "; originalSize : " + str(self.originalSize)

class FreeSpace:
  def __init__(self, size, disk_index):
    self.size = size
    self.fill = []
    self.disk_index = disk_index

  def __repr__(self):
    return "size : " + str(self.size) + "; fill" + str(self.fill)

disk = []
free_spaces = []
for index, char in enumerate(data):
  if index % 2 == 0:
    disk.append(File(index // 2, int(char)))
  else:
    free_space = FreeSpace(int(char), index)
    disk.append(free_space)
    free_spaces.append(free_space)

i_file = len(disk) - 1
k = 0
while len(free_spaces) > 0 and free_spaces[0].disk_index < i_file:
  file = disk[i_file]

  k += 1
  temp_i_fp = 0
  while temp_i_fp < len(free_spaces) and free_spaces[temp_i_fp].disk_index < i_file and file.size > 0:
    free_space = free_spaces[temp_i_fp]

    if file.size <= free_space.size:
      free_space.size -= file.size
      free_space.fill.append(File(file.id, file.size))
      file.size = 0
      i_file -= 2

      if free_space.size == 0:
        free_spaces.remove(free_space)

    temp_i_fp += 1

  if file.size > 0:
    i_file -= 2

multiplier = 0
r = 0
for index, elt in enumerate(disk):
  if index % 2 == 0:
    for d in range(elt.size):
      r += multiplier * elt.id
      multiplier += 1
    multiplier += elt.originalSize - elt.size
  else:
    for file in elt.fill:
      for d in range(file.size):
        r += multiplier * file.id
        multiplier += 1
    multiplier += elt.size

print(r)