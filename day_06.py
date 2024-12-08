import re

from utils import answer1, answer2, get_input_as_grid

grid = get_input_as_grid("day_06_input")

direction = -1
current_x = current_y = 0

visits: set[tuple[int, int]] = set()
for coord, value in grid.items():
    if value == "^":
        direction = 0  # up
        current_x, current_y = coord
        visits.add(coord)
        break
    if value == ">":
        direction = 1  # right
        current_x, current_y = coord
        visits.add(coord)
        break
    if value == "v":
        direction = 2  # down
        current_x, current_y = coord
        visits.add(coord)
        break
    if value == "<":
        direction = 3  # left
        current_x, current_y = coord
        visits.add(coord)
        break


while True:
    next_x = current_x
    next_y = current_y
    if direction == 0:
        next_y = current_y - 1
    elif direction == 1:
        next_x = current_x + 1
    elif direction == 2:
        next_y = current_y + 1
    elif direction == 3:
        next_x = current_x - 1

    try:
        next_spot = grid[(next_x, next_y)]
    except KeyError:
        break
    if next_spot == "#":
        direction = (direction + 1) % 4
        continue
    else:
        visits.add((next_x, next_y))
        current_x = next_x
        current_y = next_y


answer1(len(visits))


# answer2(total)
