from typing import List

ELF = "E"
GOBLIN = "G"
FLOOR = "."
WALL = "#"


class Thing:
    def __init__(self, kind: str):
        self.kind = kind  # E G # .
        self.hit_points = 200
        self.attack = 3


def solve_a(input_file_lines: List[str]) -> str:
    world: List[List[Thing]] = []
    for y, line in enumerate(input_file_lines):
        world.append([])
        for x, char in enumerate(line):
            world[y].append(Thing(char))
    world_size = len(world)
    assert world_size == len(world[0])  # square world

    rounds = 0
    elf_count = sum(sum(1 for c in line if c.kind == ELF) for line in world)
    goblin_count = sum(sum(1 for c in line if c.kind == GOBLIN) for line in world)
    round_should_end = False
    while not round_should_end:
        rounds += 1
        for x1 in range(world_size):
            for y1 in range(world_size):
                thing = world[x1][y1]
                if thing.kind == GOBLIN:
                    enemy_kind = ELF
                elif thing.kind == ELF:
                    enemy_kind = GOBLIN
                else:
                    continue
                pathfinding_map = [[(None, None) for _ in row] for row in world]  # min_dist, min_prev
                pathfinding_stack = [(x1, y1, 0, None)]  # x, y, dist, prev
                has_any_enemy = False
                while pathfinding_stack:
                    x, y, dist, prev = pathfinding_stack.pop()
                    if x < 0 or world_size > x or y < 0 or world_size > y:
                        continue
                    min_dist, min_prev = pathfinding_map[x][y]
                    if not min_dist or min_dist <= dist:
                        if min_dist and min_dist == dist and min_prev < prev:
                            continue  # preference for first in reading-order
                        pathfinding_map[x][y] = (dist, prev)
                        thing2 = world[x][y]
                        if thing2.kind != WALL:
                            # in reading order (up, left, right, down) reversed for stack
                            pathfinding_stack.append((x, y + 1, dist + 1, (x, y)))
                            pathfinding_stack.append((x + 1, y, dist + 1, (x, y)))
                            pathfinding_stack.append((x - 1, y, dist + 1, (x, y)))
                            pathfinding_stack.append((x, y - 1, dist + 1, (x, y)))
                        if thing2.kind == enemy_kind:
                            has_any_enemy = True
                if not has_any_enemy:
                    round_should_end = True
                else:
                    closest_enemy = None
                    closest_enemy_distance = 999
                    for x in range(world_size):
                        for y in range(world_size):
                            thing2 = world[x][y]
                            min_dist, min_prev = pathfinding_map[x][y]
                            if thing2.kind == enemy_kind and min_dist:
                                if closest_enemy_distance > min_dist:
                                    closest_enemy_distance = min_dist
                                    closest_enemy = thing2

    rounds -= 1  # last one wasn't completed

    return "TODO - solve a"


def solve_b(input_file_lines: List[str]) -> str:
    return "TODO - solve b"

LACUFXVRPWGYH
DJBEZMIOKQxTN