with open("input.txt", "r") as f:
    parts = f.read().split("\n\n")
    ranges = sorted([tuple(map(int, r.split("-"))) for r in parts[0].splitlines()])
    ingredients = map(int, parts[1].splitlines())

part_1 = 0
part_2 = 0

# Part 1
for ingredient in ingredients:
    for y0, y1 in ranges:
        if y0 <= ingredient <= y1:
            part_1 += 1
            break


# Part 2
x0, x1 = ranges[0]
for y0, y1 in ranges[1:]:
    if x1 < y0:
        part_2 += x1 - x0 + 1
        x0, x1 = y0, y1
    else:
        x1 = max(x1, y1)

part_2 += x1 - x0 + 1

print("Part 1:", part_1)  # 758
print("Part 2:", part_2)  # 343143696885053
