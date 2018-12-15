from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    recipes = [3, 7]
    e1 = 0
    e2 = 1
    improvement_count = int(input_file_lines[0])
    while len(recipes) < improvement_count + 10:  # started with 2 already
        sum_number = recipes[e1] + recipes[e2]
        if sum_number >= 10:
            recipes.append(sum_number // 10)
        recipes.append(sum_number % 10)
        e1 = (e1 + recipes[e1] + 1) % len(recipes)
        e2 = (e2 + recipes[e2] + 1) % len(recipes)
    if len(recipes) > improvement_count + 10:
        del recipes[-1]
    last_ten = recipes[-10:]

    return "".join(str(x) for x in last_ten)


def solve_b(input_file_lines: List[str]) -> str:
    recipes = [3, 7]
    e1 = 0
    e2 = 1
    target_sequence = tuple(int(x) for x in input_file_lines[0])
    seqlen = len(target_sequence)
    while True:  # started with 2 already
        sum_number = recipes[e1] + recipes[e2]
        if sum_number >= 10:
            next_recipe = sum_number // 10
            recipes.append(next_recipe)
            if tuple(recipes[-seqlen:]) == target_sequence:
                return str(len(recipes) - seqlen)
        recipes.append(sum_number % 10)
        if tuple(recipes[-seqlen:]) == target_sequence:
            return str(len(recipes) - seqlen)
        e1 = (e1 + recipes[e1] + 1) % len(recipes)
        e2 = (e2 + recipes[e2] + 1) % len(recipes)
