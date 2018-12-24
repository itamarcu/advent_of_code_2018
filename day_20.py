import itertools
import re
from typing import List
import ast as abstract_syntax_tree


def solve_a(input_file_lines: List[str]) -> str:
    text = input_file_lines[0][1:-1]
    print(text)
    text = "[" + text + "]"
    text = re.sub("([NSEW]+)", "'\\1',", text)
    text = text.replace("(", "  [").replace(")", "],").replace("|", "'|',")
    print(text)
    ast = abstract_syntax_tree.literal_eval(text)
    ast = recurfix(ast)
    print(str(ast))
    return str(max_path_len(ast))


def recurfix(ast):
    if not ast:
        return ast
    if type(ast) == str:
        return ast
    if "|" in ast:
        ast = [list(y) for k, y in itertools.groupby(ast, lambda x: x == "|") if not k]
        return tuple(recurfix(a) for a in ast)  # tuple
    return [recurfix(a) for a in ast]  # list


def max_path_len(ast):
    if not ast:
        return 0
    if isinstance(ast, str):
        return len(ast)
    if isinstance(ast, tuple):
        return max(max_path_len(x) for x in ast)
    if isinstance(ast, list):
        return sum(max_path_len(x) for x in ast)

def solve_b(input_file_lines: List[str]) -> str:
    return "TODO - solve b"

