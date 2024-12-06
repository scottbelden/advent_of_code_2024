from collections import defaultdict
import re

from utils import answer1, answer2, get_line_separated_inputs

chunks = get_line_separated_inputs("day_05_input")

rules: defaultdict[str, set[str]] = defaultdict(set)

for rule in chunks[0]:
    left, right = rule.split("|")
    rules[left].add(right)

total = 0
for update in chunks[1]:
    nums = update.split(",")
    compliant = True
    for index, num in enumerate(nums):
        if set(nums[0:index]) & rules[num]:
            compliant = False
            break

    if compliant:
        halfway = int((len(nums) - 1) / 2)
        total += int(nums[halfway])


answer1(total)


total = 0
for update in chunks[1]:
    original_compliant = True
    while True:
        nums = update.split(",")
        compliant = True
        retry = False
        for index, num in enumerate(nums):
            left_nums = nums[0:index]
            non_compliant_numbers = set(nums[0:index]) & rules[num]
            if non_compliant_numbers:
                original_compliant = False
                compliant = False
                right_nums: list[str] = [num]
                for non_compliant_number in non_compliant_numbers:
                    left_nums.remove(non_compliant_number)
                    right_nums.append(non_compliant_number)

                new_nums = left_nums + right_nums + nums[index + 1 :]
                update = ",".join(new_nums)
                retry = True
                break

        if retry:
            continue

        if compliant and not original_compliant:
            halfway = int((len(nums) - 1) / 2)
            total += int(nums[halfway])

        break


answer2(total)
