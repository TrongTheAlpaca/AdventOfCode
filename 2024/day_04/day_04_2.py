with open("test.txt", "r") as f:
    layout = f.read().splitlines()

print(layout)

visited = set()
n_xmas = 0
for y, row in enumerate(layout):
    for x, cell in enumerate(row):
        if cell == "A":
            if (
                0 <= y - 1
                and y + 1 < len(layout)
                and 0 <= x - 1
                and x + 1 < len(layout[0])
            ):
                if (
                    (layout[y + 1][x + 1] == "M" and layout[y - 1][x - 1] == "S")
                    or (layout[y + 1][x + 1] == "S" and layout[y - 1][x - 1] == "M")
                ) and (
                    (layout[y - 1][x + 1] == "M" and layout[y + 1][x - 1] == "S")
                    or (layout[y - 1][x + 1] == "S" and layout[y + 1][x - 1] == "M")
                ):
                    print("CROSS")
                    n_xmas += 1
                    visited |= set(
                        [
                            (x, y),
                            (x - 1, y - 1),
                            (x + 1, y + 1),
                            (x - 1, y + 1),
                            (x + 1, y - 1),
                        ]
                    )

for y, row in enumerate(layout):
    for x, cell in enumerate(row):
        print(cell if (x, y) in visited else ".", end="")
    print()

print("part 2:", n_xmas)  # 1905
