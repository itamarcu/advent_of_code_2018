from collections import defaultdict
from typing import List

from helpful import fullmax


def solve_a(input_file_lines: List[str]) -> str:
    points = []
    for index, line in enumerate(input_file_lines):
        x, y = line.split(", ")
        x, y = int(x), int(y)
        points.append((index, x, y))

    def make_attempt(world_size):
        closest_counts = defaultdict(lambda: 0)
        for x in range(-world_size, world_size):
            for y in range(-world_size, world_size):
                closest_dist = 9999999
                closest_index = None
                for point in points:
                    index, xx, yy = point
                    dist = abs(x-xx) + abs(y-yy)
                    if closest_dist > dist:
                        closest_dist = dist
                        closest_index = index
                    elif closest_dist == dist:
                        closest_index = None  # tie
                if closest_index is not None:
                    closest_counts[closest_index] += 1
        return closest_counts

    attempt_1 = make_attempt(400)
    attempt_2 = make_attempt(500)
    unchanging_counts = {x: attempt_1[x] for x in attempt_1.keys() if attempt_1[x] == attempt_2[x]}
    return str(fullmax(unchanging_counts)[1])  # 6047


def solve_b(input_file_lines: List[str]) -> str:
    points = []
    for index, line in enumerate(input_file_lines):
        x, y = line.split(", ")
        x, y = int(x), int(y)
        points.append((index, x, y))
    distance_maximum = 10000
    count_in_region = 0
    for x in range(-200, 500):
        for y in range(-200, 500):
            sum_distances = 0
            for point in points:
                index, xx, yy = point
                dist = abs(x-xx) + abs(y-yy)
                sum_distances += dist
            if sum_distances < distance_maximum:
                count_in_region += 1

    return str(count_in_region)  # NOT 46320 ?!?!


def someone_elses_solution(input_file_lines):
    import re
    from collections import defaultdict
    d = input_file_lines

    d = list(map(lambda s: list(map(int, re.findall(r'-?\d+', s))), d))
    min_x = min(x[0] for x in d)-(10000//len(d))-1
    max_x = max(x[0] for x in d)+(10000//len(d))+1
    min_y = min(x[1] for x in d)-(10000//len(d))-1
    max_y = max(x[1] for x in d)+(10000//len(d))+1
    mapping = {}
    in_region = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            closest = d[0]
            closest_dist = (1 << 31)
            dist_sum = 0
            for (px, py) in d:
                dist = abs(px - x) + abs(py - y)
                dist_sum += dist
                if dist < closest_dist:
                    closest = (px, py)
                    closest_dist = dist
                elif dist == closest_dist and closest != (px, py):
                    closest = None
            mapping[(x, y)] = closest
            if dist_sum < 10000:
                in_region.add((x, y))

    rev_mapping = defaultdict(int)
    for h in mapping:
        if not mapping[h]:
            continue
        if h[0] in (min_x, max_x) or h[1] in (min_y, max_y):
            rev_mapping[mapping[h]] -= (1 << 31)
        rev_mapping[mapping[h]] += 1
    print("a", max(rev_mapping.values()))
    print("b", len(in_region))

