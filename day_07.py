from itertools import product
from operator import add, mul
from collections.abc import Callable

from utils import answer1, answer2, get_input

lines = get_input("day_07_input")


def combine(a: int, b: int) -> int:
    return int(str(a) + str(b))


def test_args(args: list[int], operations: tuple[Callable[[int, int], int], ...]) -> int:
    total = 0
    for index, arg in enumerate(args):
        if index == 0:
            total = arg
            continue

        total = operations[index - 1](total, arg)

    return total


calibration = 0
for line in lines:
    total, rest = line.split(": ")
    args = [int(item) for item in rest.split()]

    combinations = product((add, mul), repeat=len(args) - 1)

    for combination in combinations:
        test_total = test_args(args, combination)
        if test_total == int(total):
            calibration += test_total
            break


answer1(calibration)


calibration = 0
for line in lines:
    total, rest = line.split(": ")
    args = [int(item) for item in rest.split()]

    combinations = product((add, mul, combine), repeat=len(args) - 1)

    for combination in combinations:
        test_total = test_args(args, combination)
        if test_total == int(total):
            calibration += test_total
            break


answer2(calibration)
