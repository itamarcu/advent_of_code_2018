import re
from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    # #1250 @ 725,543: 13x23
    area: List[List[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input_file_lines:
        id, x, y, w, h = map(int, re.fullmatch("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups())
        overlap = False
        for i in range(x, x + w):
            for j in range(y, y + h):
                area[i][j] += 1
                overlap = True
        if not overlap:
            print()
    answer = sum([sum([1 for c in l if c > 1]) for l in area])
    return str(answer)


def solve_b(input_file_lines: List[str]) -> str:
    # #1250 @ 725,543: 13x23
    area: List[List[int]] = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input_file_lines:
        id, x, y, w, h = map(int, re.fullmatch("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups())
        for i in range(x, x + w):
            for j in range(y, y + h):
                area[i][j] += 1
    for line in input_file_lines:
        id, x, y, w, h = map(int, re.fullmatch("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups())
        overlap = False
        for i in range(x, x + w):
            for j in range(y, y + h):
                if area[i][j] > 1:
                    overlap = True
        if not overlap:
            return str(id)
