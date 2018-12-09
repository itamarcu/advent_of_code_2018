import day_09

with open("input_09") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_09.solve_a(input_file_lines))
print(day_09.solve_b(input_file_lines))
