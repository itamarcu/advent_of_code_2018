from typing import List, Tuple, Optional


def solve_a(input_file_lines: List[str]) -> str:
    reqs = [(x[5], x[36]) for x in input_file_lines]
    have = []
    remaining = [chr(x) for x in range(ord("A"), ord("Z")+1)][::-1]  # REVERSED
    while remaining:
        next_step = None
        for char in remaining:
            possible = True
            for a, b in reqs:
                if b == char:
                    if a not in have:
                        possible = False
                        break
            if possible:
                next_step = char
        have.append(next_step)
        remaining.remove(next_step)

    return "".join(have)


def solve_b(input_file_lines: List[str]) -> str:
    reqs = [(x[5], x[36]) for x in input_file_lines]
    char_count = ord(max(reqs, key=lambda pair: pair[0])[0]) - ord("A") + 1
    workers: List[Optional[Tuple[str, int]]] = [None for _ in range(5)]  # (char, time_left)
    remaining = [chr(x) for x in range(ord("A"), ord("A") + char_count)]
    have = []
    total_time = 0
    while len(have) < char_count:
        total_time += 1
        possible_chars = []
        free_worker_count = len([x for x in workers if x is None])
        if free_worker_count > 0:
            for char in remaining:
                possible = True
                for a, b in reqs:
                    if b == char:
                        if a not in have:
                            possible = False
                            break
                if possible:
                    possible_chars.append(char)
            for char in possible_chars:
                for i in range(len(workers)):
                    if workers[i] is None:
                        time_left = ord(char) - ord("A") + 1 + 60
                        workers[i] = (char, time_left)
                        remaining.remove(char)
                        free_worker_count -= 1
                        break
        for i, w in enumerate(workers):
            if w is not None:
                c, t = w
                if t == 1:
                    workers[i] = None
                    have.append(c)
                else:
                    workers[i] = (c, t-1)

    return str(total_time)

