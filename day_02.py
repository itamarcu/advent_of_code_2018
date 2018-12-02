import itertools
from collections import defaultdict
from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    count_2s = 0
    count_3s = 0
    for id1 in input_file_lines:
        counts = defaultdict(lambda: 0)
        for char in id1:
            counts[char] += 1
        if 2 in counts.values():
            count_2s += 1
        if 3 in counts.values():
            count_3s += 1
    return str(count_2s * count_3s)


def solve_b(input_file_lines: List[str]) -> str:
    for id1, id2 in itertools.combinations(input_file_lines, 2):
        diff = [c1 != c2 for c1, c2 in zip(id1, id2)]
        if sum(diff) == 1:
            for i in range(len(diff)):
                if diff[i]:
                    return id1[:i] + id1[i+1:]
