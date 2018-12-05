import day_05

with open("input_05") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_05.solve_a(input_file_lines))
print(day_05.solve_b(input_file_lines))