UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

POSITIONS = [UP, RIGHT, DOWN, LEFT]

DELTA = {
  UP: (-1, 0),
  RIGHT: (0, 1),
  DOWN: (1, 0),
  LEFT: (0, -1)
}

with open("input") as file:
  data = file.readlines()

for i in range(len(data)):
  data[i] = '*' + data[i].strip() + '*'

data.append('*' * len(data[0]))
data.insert(0, '*' * len(data[0]))

for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] == '^':
      row, col = (i, j)

current_direction = UP
visited_square = {(row, col)}

while data[row][col] != '*':

  temp_r, temp_col = row + DELTA[current_direction][0], col + DELTA[current_direction][1]
  if data[temp_r][temp_col] != '#':
    row, col = temp_r, temp_col
    visited_square.add((row, col))
  else:
    current_direction = POSITIONS[(POSITIONS.index(current_direction) + 1) % len(POSITIONS)]

print(len(visited_square) - 1)