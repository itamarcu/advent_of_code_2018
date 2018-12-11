import day_11

with open("input_11") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_11.solve_a(input_file_lines))
print(day_11.solve_b(input_file_lines))
