from typing import List


def solve_a(input_file_lines: List[str]) -> str:
    chars = list(map(int, input_file_lines[0].split(" ")))

    def recurse(i):
        """return (sum, new_i)"""
        child_count = chars[i]
        metadata_count = chars[i + 1]
        i += 2
        total_sum = 0
        for c in range(child_count):
            child_sum, new_i = recurse(i)
            total_sum += child_sum
            i = new_i
        total_sum += sum(chars[i:i + metadata_count])
        i += metadata_count
        return total_sum, i

    answer, _ = recurse(0)
    return str(answer)


def solve_b(input_file_lines: List[str]) -> str:
    chars = list(map(int, input_file_lines[0].split(" ")))

    def recurse(i):
        """return (value, new_i)"""
        child_count = chars[i]
        metadata_count = chars[i + 1]
        i += 2
        if child_count == 0:
            total_value = sum(chars[i:i + metadata_count])
            i += metadata_count
            return total_value, i

        total_value = 0
        child_values = []
        for c in range(child_count):
            child_value, new_i = recurse(i)
            child_values.append(child_value)
            i = new_i
        total_value += sum(child_values[c - 1] for c in chars[i:i + metadata_count] if 0 <= c - 1 <= child_count - 1)
        i += metadata_count
        return total_value, i

    answer, _ = recurse(0)
    return str(answer)
