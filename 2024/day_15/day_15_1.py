with open("input.txt", "r") as f:
    walls = set()
    fishes = set()
    start_position = None
    warehouse_string, movements_rows = f.read().split("\n\n")
    rows = warehouse_string.splitlines()
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            elif cell == "O":
                fishes.add((x, y))
            elif cell == "@":
                start_position = (x, y)

    movements = "".join(movements_rows.splitlines())

MAX_X = len(rows[0])
MAX_Y = len(rows)
PRINT_BOARD = False


def print_board(enable: bool, title: str):
    if not enable:
        return
    drawing = title + "\n"
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if (x, y) in walls:
                drawing += "#"
            elif (x, y) in fishes:
                drawing += "O"
            elif (x, y) == current_pos:
                drawing += "@"
            else:
                drawing += "."
        drawing += "\n"
    print(drawing)


current_pos = start_position
print_board(PRINT_BOARD, "Initial:")

for idx, move in enumerate(movements):
    direction = None
    if move == ">":
        direction = (1, 0)
    elif move == "^":
        direction = (0, -1)
    elif move == "<":
        direction = (-1, 0)
    else:
        direction = (0, 1)

    next_pos = current_pos[0] + direction[0], current_pos[1] + direction[1]
    next_x, next_y = next_pos

    if next_pos in walls:
        continue
    elif next_pos in fishes:

        dx, dy = direction
        while True:
            check_pos = (next_pos[0] + dx, next_pos[1] + dy)
            if check_pos in walls:
                break
            elif check_pos in fishes:
                dx, dy = dx + direction[0], dy + direction[1]
            else:
                # Space is found
                fishes.remove(next_pos)
                fishes.add(check_pos)
                current_pos = next_pos
                break
    else:
        current_pos = next_pos

    print_board(PRINT_BOARD, f"After move {idx} - {move}:")

part_1 = sum(y * 100 + x for x, y in fishes)
print("Part 1:", part_1)  # Part 1: 1476771
