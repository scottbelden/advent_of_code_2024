from collections import deque
from typing import Literal

from utils import answer1, answer2, get_input_as_str

disk_map = get_input_as_str("day_09_input")

file_id = 0
disk_space: deque[int | Literal[""]] = deque()
for index, char in enumerate(disk_map):
    if index % 2 == 0:
        value = file_id
        file_id += 1
    else:
        value = ""

    for _ in range(int(char)):
        disk_space.append(value)

checksum = 0
position = 0
try:
    while True:
        left = disk_space.popleft()
        if left != "":
            checksum += position * left
            position += 1
        else:
            while True:
                right = disk_space.pop()
                if right != "":
                    checksum += position * right
                    position += 1
                    break
except IndexError:
    pass


answer1(checksum)


file_id = 0
disk_space = deque()
file_locations: list[tuple[int, int, int]] = []
# Free space is the position to how much space exists
free_space: dict[int, int] = {}
for index, char in enumerate(disk_map):
    if index % 2 == 0:
        value = file_id
        file_locations.append((file_id, int(char), len(disk_space)))
        file_id += 1
    else:
        value = ""
        free_space[len(disk_space)] = int(char)

    for _ in range(int(char)):
        disk_space.append(value)


for file_id, size, position in reversed(file_locations):
    for free_position, available_space in sorted(free_space.items()):
        if free_position > position:
            continue
        if size == available_space:
            del free_space[free_position]
            free_space[position] = size
            for i in range(size):
                disk_space[free_position + i] = file_id
                disk_space[position + i] = ""
            break
        elif size < available_space:
            del free_space[free_position]
            free_space[free_position + size] = available_space - size
            for i in range(size):
                disk_space[free_position + i] = file_id
                disk_space[position + i] = ""
            break

checksum = 0
for index, file_id in enumerate(disk_space):
    if file_id != "":
        checksum += index * file_id

answer2(checksum)
