# PREAMBLE
with open("input") as f:
    lines = [(y[0], int(y[1])) for y in [x.split(' ') for x in f.readlines()]]

# match-case: https://stackoverflow.com/a/30881320

# PART 1
horizontal = 0
depth = 0
for command in lines:
    match command[0]:
        case 'forward':
            horizontal += command[1]
        case 'down':
            depth += command[1]
        case 'up':
            depth -= command[1]

print(horizontal * depth)  # 1488669 is Correct!

# PART 2
horizontal = 0
depth = 0
aim = 0

for command in lines:
    match command[0]:
        case 'forward':
            horizontal += command[1]
            depth += command[1] * aim
        case 'down':
            aim += command[1]
        case 'up':
            aim -= command[1]

print(horizontal * depth)  # 1176514794 is Correct!
