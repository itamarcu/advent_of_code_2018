from collections import defaultdict
from typing import List


def calc_value(world):
    world_size = len(world)
    counts = defaultdict(lambda: 0)
    for x in range(world_size):
        for y in range(world_size):
            if world[x][y] not in counts:
                counts[world[x][y]] = 0
            counts[world[x][y]] += 1
    return counts["|"] * counts["#"]


def print_world(world):
    for row in world[::2]:  # looks nicer
        print("".join(row), flush=False)
    print()


def solve_a(input_file_lines: List[str]) -> str:
    world = [list(x) for x in input_file_lines]
    world_size = len(world)

    for minute in range(1000):
        new_world = [row.copy() for row in world]
        for x in range(world_size):
            for y in range(world_size):
                counts = defaultdict(lambda: 0)
                for xx in range(x-1, x+2):
                    for yy in range(y-1, y+2):
                        if xx == min(max(0, xx), world_size-1) and yy == min(max(0, yy), world_size-1):
                            counts[world[xx][yy]] += 1
                counts[world[x][y]] -= 1
                if world[x][y] == "." and counts["|"] >= 3:
                    new_world[x][y] = "|"
                elif world[x][y] == "|" and counts["#"] >= 3:
                    new_world[x][y] = "#"
                elif world[x][y] == "#" and (counts["#"] < 1 or counts["|"] < 1):
                    new_world[x][y] = "."
        world = new_world
        print_world(world)
        # resource_value = calc_value(world)
        # print(minute, resource_value)

    resource_value = calc_value(world)
    return str(resource_value)


def solve_b(input_file_lines: List[str]) -> str:
    # at 500 it's 180560
    # then it's:
    #
    # 500 180560
    # 501 181383
    # 502 182700
    # 503 180942
    # 504 176782
    # 505 175212
    # 506 173290
    # 507 173658
    # 508 173922
    # 509 177815
    # 510 182358
    # 511 186042
    # 512 192504
    # 513 195308
    # 514 200646
    # 515 205120
    # 516 208650
    # 517 210588
    # 518 212833
    # 519 212688
    # 520 212443
    # 521 208278
    # 522 200466
    # 523 196680
    # 524 195290
    # 525 189980
    # 526 186795
    # 527 184392
    #
    # 528 180560
    # 529 181383
    # 530 182700
    # ... (looping)
    #
    # So it has a loop of size 28
    # so:
    # value(1000000000) == value(500 + (1000000000-500) % 28)
    # == value(524) == 195290
    return "195290"

