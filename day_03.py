import re

from utils import answer1, answer2, get_input

lines = get_input("day_03_input")


def mul(string: str) -> int:
    left, right = string[4:-1].split(",")
    return int(left) * int(right)


total = 0
for line in lines:
    matches = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", line)
    for match in matches:
        total += mul(match)

answer1(total)

total = 0
enabled = True
for line in lines:
    matches = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)", line)
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            total += mul(match)


answer2(total)
