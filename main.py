import day_25

with open("input_25") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_25.solve_a(input_file_lines))
print(day_25.solve_b(input_file_lines))
