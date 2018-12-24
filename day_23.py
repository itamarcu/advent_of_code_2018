import itertools
import re
from typing import List

import helpful


def solve_a(input_file_lines: List[str]) -> str:
    dots = [tuple(int(x) for x in re.findall("-?\d+", y)) for y in input_file_lines]

    highest_index, big_dot, big_radius = helpful.fullmax(dots, key_func=lambda x: x[3], full_result=True)
    count = sum(1 for dot in dots if abs(dot[0]-big_dot[0]) + abs(dot[1]-big_dot[1]) + abs(dot[2]-big_dot[2]) <= big_radius)
    return str(count)  # 721


def solve_b(input_file_lines: List[str]) -> str:
    dots = [tuple(int(x) for x in re.findall("-?\d+", y)) for y in input_file_lines]

    best = (17432354, 37654608, 42003205)
    best_count = sum(1 for dot in dots if abs(dot[0]-best[0]) + abs(dot[1]-best[1]) + abs(dot[2]-best[2]) <= dot[3])
    for change in itertools.product(range(-300, +300, +100), repeat=3):
        dot_1 = tuple(best[i] + change[i] for i in range(3))
        count = sum(1 for dot in dots if abs(dot[0]-dot_1[0]) + abs(dot[1]-dot_1[1]) + abs(dot[2]-dot_1[2]) <= dot[3])
        if count > best_count:
            best_count = count
            best = dot_1

    out_of_range_dots = []
    for dot in dots:
        dot_1 = best
        dist = abs(dot[0]-dot_1[0]) + abs(dot[1]-dot_1[1]) + abs(dot[2]-dot_1[2])
        if dot[3] < dist:
            out_of_range_dots.append((dist-dot[3], tuple((dot[i]-best[i])*(dist-dot[3])//dist for i in range(3))))
    out_of_range_dots.sort(key=lambda pair: pair[0])
    for dist, dot in out_of_range_dots[::-1]:
        print(dist, dot)

    # print()
    # closest_pair = None
    # closest_pair_dist = 99999999999999
    # for d1p, d2p in itertools.product(out_of_range_dots, out_of_range_dots):
    #     _, d1 = d1p
    #     _, d2 = d2p
    #     dist = abs(d2[0]-d1[0]) + abs(d2[1]-d1[1]) + abs(d2[2]-d1[2])
    #     if dist == 0:
    #         continue
    #     if dist < closest_pair_dist:
    #         closest_pair_dist = dist
    #         closest_pair = (d1, d2)
    # print(closest_pair)

    return f"{best}, {best_count}, {sum(abs(x) for x in best)}"
# 97850167 too high (911)
#
# f"{best_position}, {best_count}, {sum(abs(x) for x in best_position)}"
# (21572114, 41246838, 43694765), 861, 106513717
# (21472114, 41346838, 43794765), 862, 106613717
# (17472114, 39196838, 41794765), 887, 98463717
# (18092665, 38165030, 41593452), 888, 97851147
# (18092677, 38165022, 41593441), 889, 97851140
# (18092683, 38165017, 41593440), 891, 97851140
# (18092354, 38164607, 41593206), 911, 97850167
#
#
#
#

