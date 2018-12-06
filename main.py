import day_06

with open("input_06") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_06.solve_a(input_file_lines))
print(day_06.solve_b(input_file_lines))
