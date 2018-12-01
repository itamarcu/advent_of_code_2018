from typing import List


def solve(input_file_lines: List[str]) -> str:
    frequency = 0
    seen = {0}
    while True:
        for x in input_file_lines:
            frequency += int(x)
            if frequency in seen:
                return str(frequency)
            seen.add(frequency)
