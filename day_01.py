from collections import Counter

from utils import answer1, answer2, get_input

lines = get_input("day_01_input")

lefts: list[int] = []
rights: list[int] = []

for line in lines:
    left, right = line.split()
    lefts.append(int(left))
    rights.append(int(right))

diff = 0
for left_int, right_int in zip(sorted(lefts), sorted(rights)):
    diff += abs(left_int - right_int)

answer1(diff)

right_counter = Counter(rights)

similarity_score = 0
for left_int in lefts:
    similarity_score += left_int * right_counter[left_int]

answer2(similarity_score)
