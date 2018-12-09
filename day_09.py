import re
from collections import deque
from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    player_count, last_marble = [int(x) for x in re.findall("\\d+", input_file_lines[0])]
    return solve(player_count, last_marble)
    # 422980


def solve_b(input_file_lines: List[str]) -> str:
    player_count, last_marble = [int(x) for x in re.findall("\\d+", input_file_lines[0])]
    return solve(player_count, last_marble * 100)
    # 3552041936


def solve(player_count, last_marble):
    board = deque([0])
    player = -1
    scores = [0 for _ in range(player_count)]
    for i in range(1, last_marble + 1):
        player = (player + 1) % player_count
        if i % 23 == 0:
            scores[player] += i
            board.rotate(+7)  # go 7 back
            scores[player] += board.pop()
            board.rotate(-1)  # new current marble = immediately clockwise neighbor of removed marble
        else:
            board.rotate(-1)  # skip one
            board.append(i)  # add one
    highscore = max(scores)
    return str(highscore)
