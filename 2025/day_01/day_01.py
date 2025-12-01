with open("input.txt", "r") as f:
    lines = [(l[0], int(l[1:])) for l in f.readlines()]

current = 50
part_1 = 0
part_2 = 0

for direction, amount in lines:
    for _ in range(amount):
        current += 1 if direction == "R" else -1
        if current == -1:
            current = 99
        if current == 100:
            current = 0
        if current == 0:
            part_2 += 1

    if current == 0:
        part_1 += 1

print("Part 1:", part_1)  #  997
print("Part 2:", part_2)  # 5978
