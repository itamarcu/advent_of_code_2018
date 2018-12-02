import day_02

with open("input_02") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_02.solve_a(input_file_lines))
print(day_02.solve_b(input_file_lines))