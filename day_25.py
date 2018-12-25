from collections import defaultdict
from typing import List, Sequence

from helpful import UnionFind


def dist(coords1: Sequence[int], coords2: Sequence[int]):
    assert len(coords1) == len(coords2)
    return sum([abs(coords1[i] - coords2[i]) for i in range(len(coords1))])


def solve_a_slower(input_file_lines: List[str]) -> str:
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


def solve_a_faster(input_file_lines: List[str]) -> str:
    def calc_bucket_key(c: Sequence[int]):
        return sum(c)
    all_coords = set()
    unions = UnionFind()
    buckets = defaultdict(lambda: set())
    for line in input_file_lines:
        coords = tuple([int(x) for x in line.split(",")])
        bucket_key = calc_bucket_key(coords)
        for other_coords in buckets[bucket_key]:
            if dist(coords, other_coords) <= 3:
                unions.union(coords, other_coords)
        all_coords.add(coords)
        for small_change in range(-3, +3 + 1):
            buckets[bucket_key + small_change].add(coords)
    union_counts = defaultdict(lambda: 0)
    for coords in all_coords:
        union_counts[unions[coords]] += 1

    constellation_count = len(union_counts.keys())
    return str(constellation_count)


def solve_a(input_file_lines: List[str]) -> str:
    return solve_a_faster(input_file_lines)


def solve_b(input_file_lines: List[str]) -> str:
    return "TODO - solve b"
