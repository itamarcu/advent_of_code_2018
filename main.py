import day_01

with open("input_01") as file:
    input_file_lines = file.readlines()

print(day_01.solve(input_file_lines))