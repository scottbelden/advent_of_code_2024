from itertools import pairwise, combinations
from typing import Sequence

from utils import answer1, answer2, get_input

lines = get_input("day_02_input")

safe = 0
for line in lines:
    diffs: set[int] = set()
    nums = [int(num) for num in line.split()]
    for first, second in pairwise(nums):
        diff = second - first
        diffs.add(diff)
        if diff == 0 or abs(diff) > 3:
            # unsafe
            break

        if diffs & {1, 2, 3} and diffs & {-1, -2, -3}:
            # unsafe
            break
    else:
        safe += 1

answer1(safe)


def is_safe(nums: Sequence[int]) -> bool:
    diffs: set[int] = set()
    for first, second in pairwise(nums):
        diff = second - first
        diffs.add(diff)
        if diff == 0 or abs(diff) > 3:
            # unsafe
            return False

        if diffs & {1, 2, 3} and diffs & {-1, -2, -3}:
            # unsafe
            return False
    else:
        return True


safe = 0
for line in lines:
    diffs: set[int] = set()
    nums = [int(num) for num in line.split()]
    if is_safe(nums):
        safe += 1
    else:
        for combo in combinations(nums, len(nums) - 1):
            if is_safe(combo):
                safe += 1
                break


answer2(safe)
