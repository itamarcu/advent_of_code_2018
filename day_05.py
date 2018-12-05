from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    polymer = input_file_lines[0]
    return str(len(react(polymer)))


def will_react(polymer, i, j):
    return abs(ord(polymer[i]) - ord(polymer[j])) == 32  # 32 == ord("A")-ord("a")


def react(polymer):
    i = 0
    while i < len(polymer) - 1:
        i += 1
        clump_size = 0
        while clump_size < i \
                and i + clump_size < len(polymer) \
                and will_react(polymer, i + clump_size, i - clump_size - 1):
            clump_size += 1
        if clump_size > 0:
            polymer = polymer[:i - clump_size] + polymer[i + clump_size:]
            i -= clump_size + 1  # to retry clumping with last unclumped letter
    return polymer


def solve_b(input_file_lines: List[str]) -> str:
    polymer = input_file_lines[0]
    best_length = 99999999999999
    for letter_ord in range(ord("a"), ord("z") + 1):
        letter = chr(letter_ord)
        # print(letter + "…")
        polymer_copy = "".join([x for x in polymer if x.lower() != letter])
        len_after_react = len(react(polymer_copy))
        if best_length > len_after_react:
            best_length = len_after_react
    return str(best_length)
