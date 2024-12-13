with open("input.txt", "r") as f:
    layout = f.read().splitlines()

print(layout)

visited = set()
n_xmas = 0
for y, row in enumerate(layout):
    for x, cell in enumerate(row):

        if cell == "X":
            # Eastwards
            if layout[y][x : x + 4] == "XMAS":
                print("EAST + 1")
                n_xmas += 1
                visited |= set([(x + i, y) for i in range(4)])

            # Westwards
            if layout[y][x - 3 : x + 1] == "SAMX":
                print("WEST + 1")
                n_xmas += 1
                visited |= set([(x - i, y) for i in range(4)])

            # Northwards
            if (
                y - 3 >= 0
                and layout[y - 1][x] == "M"
                and layout[y - 2][x] == "A"
                and layout[y - 3][x] == "S"
            ):
                print("NORTH + 1")
                n_xmas += 1
                visited |= set([(x, y - i) for i in range(4)])

            # Southwards
            if (
                y + 3 < len(layout)
                and layout[y + 1][x] == "M"
                and layout[y + 2][x] == "A"
                and layout[y + 3][x] == "S"
            ):
                print("SOUTH + 1")
                n_xmas += 1
                visited |= set([(x, y + i) for i in range(4)])

            # Diagonal SE
            if (
                y + 3 < len(layout)
                and x + 3 < len(layout[0])
                and layout[y + 1][x + 1] == "M"
                and layout[y + 2][x + 2] == "A"
                and layout[y + 3][x + 3] == "S"
            ):
                print("NE + 1")
                n_xmas += 1
                visited |= set([(x + i, y + i) for i in range(4)])

            # Diagonal SW
            if (
                y + 3 < len(layout)
                and x - 3 >= 0
                and layout[y + 1][x - 1] == "M"
                and layout[y + 2][x - 2] == "A"
                and layout[y + 3][x - 3] == "S"
            ):
                print("SW + 1")
                n_xmas += 1
                visited |= set([(x - i, y + i) for i in range(4)])

            # Diagonal NW
            if (
                y - 3 >= 0
                and x - 3 >= 0
                and layout[y - 1][x - 1] == "M"
                and layout[y - 2][x - 2] == "A"
                and layout[y - 3][x - 3] == "S"
            ):
                print("NW + 1")
                n_xmas += 1
                visited |= set([(x - i, y - i) for i in range(4)])

            # Diagonal NE
            if (
                y - 3 >= 0
                and x + 3 < len(layout[0])
                and layout[y - 1][x + 1] == "M"
                and layout[y - 2][x + 2] == "A"
                and layout[y - 3][x + 3] == "S"
            ):
                print("NE + 1")
                n_xmas += 1
                visited |= set([(x + i, y - i) for i in range(4)])

for y, row in enumerate(layout):
    for x, cell in enumerate(row):
        print(cell if (x, y) in visited else ".", end="")
    print()

print("part 1:", n_xmas)  # 2613
