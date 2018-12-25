from collections import defaultdict
from typing import List
from helpful import UnionFind


def dist(coords1, coords2):
    return sum([abs(coords1[i] - coords2[i]) for i in range(len(coords1))])


def solve_a(input_file_lines: List[str]) -> str:
    all_coords = []
    unions = UnionFind()
    for line in input_file_lines:
        coords = tuple([int(x) for x in line.split(",")])
        all_coords.append(coords)
        for other_coords in all_coords:
            if dist(coords, other_coords) <= 3:
                unions.union(coords, other_coords)
    union_counts = defaultdict(lambda: 0)
    for coords in all_coords:
        union_counts[unions[coords]] += 1

    constellation_count = len(union_counts.keys())

    return str(constellation_count)


def solve_b(input_file_lines: List[str]) -> str:
    return "TODO - solve b"
