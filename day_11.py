import itertools
from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    grid_serial = int(input_file_lines[0])

    def calc_power(x, y):
        rack_id = x + 10
        power = (rack_id * y + grid_serial) * rack_id
        power = (power // 100) % 10 - 5
        return power

    grid_power = {(x, y): calc_power(x, y) for (x, y) in itertools.product(range(1, 300 + 1), range(1, 300 + 1))}
    largest_square_corner = None
    largest_square_value = -999999
    for (x, y) in itertools.product(range(1, 300 - 1), range(1, 300 - 1)):
        square_value = grid_power[x, y] + grid_power[x + 1, y] + grid_power[x + 2, y] + grid_power[x, y + 1] \
                       + grid_power[x + 1, y + 1] + grid_power[x + 2, y + 1] + grid_power[x, y + 2] + grid_power[
                           x + 1, y + 2] + grid_power[x + 2, y + 2]
        if largest_square_value < square_value:
            largest_square_value = square_value
            largest_square_corner = (x, y)
    return f"{largest_square_corner[0]},{largest_square_corner[1]}"
    # 20,58


def solve_b(input_file_lines: List[str]) -> str:
    grid_serial = int(input_file_lines[0])

    def calc_power(x, y):
        rack_id = x + 10
        power = (rack_id * y + grid_serial) * rack_id
        power = (power // 100) % 10 - 5
        return power

    grid_power = {(x, y): calc_power(x, y) for (x, y) in itertools.product(range(1, 300 + 1), range(1, 300 + 1))}
    largest_square_corner = None
    largest_square_value = -999999
    largest_square_size = None
    cache = {(1, 1): grid_power[1, 1]}
    for k in range(2, 300 + 1):
        cache[1, k] = cache[1, k - 1] + grid_power[1, k]
        cache[k, 1] = cache[k - 1, 1] + grid_power[k, 1]
    for x in range(2, 300 + 1):
        for y in range(2, 300 + 1):
            cache[x, y] = grid_power[x, y] + cache[x, y - 1] + cache[x - 1, y] - cache[x - 1, y - 1]
    for (x, y) in itertools.product(range(1, 300 + 1), range(1, 300 + 1)):
        for s in range(300 - max(x, y)):  # is size minus 1
            square_value = cache.get(
                (x + s, y + s), 0) - cache.get((x - 1, y + s), 0) - \
                           cache.get((x + s, y - 1), 0) + cache.get((x - 1, y - 1), 0)
            if largest_square_value < square_value:
                largest_square_value = square_value
                largest_square_corner = (x, y)
                largest_square_size = s + 1
    return f"{largest_square_corner[0]},{largest_square_corner[1]},{largest_square_size}"
    # 233,268,13
