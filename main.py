import day_04

with open("input_04") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_04.solve_a(input_file_lines))
print(day_04.solve_b(input_file_lines))