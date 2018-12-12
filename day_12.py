from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    iter_count = 20
    answer = simulate(input_file_lines, iter_count)

    return str(answer)  # 6201; not 6083, 10241


def simulate(input_file_lines, iter_count: int):
    state = list(input_file_lines[0].split()[2])
    rules = {"".join(line.split()[0]): line.split()[2] for line in input_file_lines[2:]}
    for j in range(iter_count):
        state = list("....") + state + list("....")
        new_state = state[:]
        for i in range(2, len(new_state) - 3):
            area = "".join(state[i - 2:i + 3])
            new_state[i] = rules[area] if area in rules else "."
        state = new_state
    answer = 0
    for i in range(len(state)):
        if state[i] == "#":
            index = i - 4 * iter_count
            answer += index
    return answer


def solve_b(input_file_lines: List[str]) -> str:
    iter_count = 50000000000
    # after 100 iterations, answer is 19623
    # after 101 iterations, answer is 19809
    # after 102 iterations, answer is 19995
    # etc. growing by 186 each time.
    ans_after_100 = simulate(input_file_lines, 100)
    ans_after_101 = simulate(input_file_lines, 101)
    ans_increment = ans_after_101 - ans_after_100
    return str(ans_after_100 + (iter_count - 100) * ans_increment)
