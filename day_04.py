import re

from utils import answer1, answer2, get_input_as_grid

grid = get_input_as_grid("day_04_input")


def find_xmas(x_coords: tuple[int, int], grid: dict[tuple[int, int], str]) -> int:
    finds = 0
    x_coord, y_coord = x_coords

    try:
        if (
            grid[(x_coord, y_coord - 1)] == "M"
            and grid[(x_coord, y_coord - 2)] == "A"
            and grid[(x_coord, y_coord - 3)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord + 1, y_coord - 1)] == "M"
            and grid[(x_coord + 2, y_coord - 2)] == "A"
            and grid[(x_coord + 3, y_coord - 3)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord + 1, y_coord)] == "M"
            and grid[(x_coord + 2, y_coord)] == "A"
            and grid[(x_coord + 3, y_coord)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord + 1, y_coord + 1)] == "M"
            and grid[(x_coord + 2, y_coord + 2)] == "A"
            and grid[(x_coord + 3, y_coord + 3)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord, y_coord + 1)] == "M"
            and grid[(x_coord, y_coord + 2)] == "A"
            and grid[(x_coord, y_coord + 3)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord - 1, y_coord + 1)] == "M"
            and grid[(x_coord - 2, y_coord + 2)] == "A"
            and grid[(x_coord - 3, y_coord + 3)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord - 1, y_coord)] == "M"
            and grid[(x_coord - 2, y_coord)] == "A"
            and grid[(x_coord - 3, y_coord)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    try:
        if (
            grid[(x_coord - 1, y_coord - 1)] == "M"
            and grid[(x_coord - 2, y_coord - 2)] == "A"
            and grid[(x_coord - 3, y_coord - 3)] == "S"
        ):
            finds += 1
    except KeyError:
        pass

    return finds


def find_x_mas(a_coords: tuple[int, int], grid: dict[tuple[int, int], str]) -> int:
    x_coord, y_coord = a_coords

    try:
        top_left = grid[(x_coord - 1, y_coord - 1)]
        top_right = grid[(x_coord + 1, y_coord - 1)]
        bottom_left = grid[(x_coord - 1, y_coord + 1)]
        bottom_right = grid[(x_coord + 1, y_coord + 1)]
    except KeyError:
        return 0

    if (top_left == "M" and bottom_right == "S" or top_left == "S" and bottom_right == "M") and (
        bottom_left == "M" and top_right == "S" or bottom_left == "S" and top_right == "M"
    ):
        return 1
    else:
        return 0


total = 0
for coordinates, value in grid.items():
    if value != "X":
        continue

    total += find_xmas(coordinates, grid)


answer1(total)


total = 0
for coordinates, value in grid.items():
    if value != "A":
        continue

    total += find_x_mas(coordinates, grid)


answer2(total)
