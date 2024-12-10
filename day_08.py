from collections import defaultdict
from itertools import permutations

from utils import answer1, answer2, get_input_as_grid

grid = get_input_as_grid("day_08_input")

antennas: defaultdict[str, set[tuple[int, int]]] = defaultdict(set)
for location, char in grid.items():
    if char == ".":
        continue

    antennas[char].add(location)

antinode_locations: set[tuple[int, int]] = set()
for char, locations in antennas.items():
    for loc1, loc2 in permutations(locations, 2):
        new_x = loc1[0] + (loc1[0] - loc2[0])
        new_y = loc1[1] + (loc1[1] - loc2[1])
        if (new_x, new_y) in grid:
            antinode_locations.add((new_x, new_y))


answer1(len(antinode_locations))


antinode_locations: set[tuple[int, int]] = set()
for char, locations in antennas.items():
    for loc1, loc2 in permutations(locations, 2):
        antinode_locations.add(loc1)
        antinode_locations.add(loc2)
        diff_x = loc1[0] - loc2[0]
        diff_y = loc1[1] - loc2[1]
        new_x = loc1[0] + diff_x
        new_y = loc1[1] + diff_y
        while True:
            if (new_x, new_y) in grid:
                antinode_locations.add((new_x, new_y))
                new_x = new_x + diff_x
                new_y = new_y + diff_y
            else:
                break


answer2(len(antinode_locations))
