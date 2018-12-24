import day_24

with open("input_24") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_24.solve_a(input_file_lines))
print(day_24.solve_b(input_file_lines))
