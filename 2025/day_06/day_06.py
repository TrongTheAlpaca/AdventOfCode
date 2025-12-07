with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    number_strings = lines[:-1]
    operator_string = lines[-1]

part_1 = 0
part_2 = 0

# Part 1
number_rows = [list(map(int, l.split())) for l in number_strings]
operators = operator_string.split()
for x in range(len(number_rows[0])):
    operator = operators[x]
    current = number_rows[0][x]
    for y in range(1, len(number_rows)):
        if operator == "+":
            current += number_rows[y][x]
        elif operator == "*":
            current *= number_rows[y][x]

    part_1 += current

# Part 2
operator_idx = 0
current_value = 0
for x in range(len(operator_string)):
    number = "".join([r[x] for r in number_strings])
    if number.isspace():
        part_2 += current_value
        current_value = 0
        operator_idx += 1
        continue

    if operators[operator_idx] == "+":
        current_value += int(number)
    else:
        if current_value == 0:
            current_value = 1
        current_value *= int(number)
part_2 += current_value

print("Part 1:", part_1)  # 5060053676136
print("Part 2:", part_2)  # 9695042567249
