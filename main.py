import day_03

with open("input_03") as file:
    input_file_lines = file.readlines()
    input_file_lines = [x.strip() for x in input_file_lines]

print(day_03.solve_a(input_file_lines))
print(day_03.solve_b(input_file_lines))