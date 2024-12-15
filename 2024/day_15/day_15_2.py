with open("input.txt", "r") as f:
    walls = set()
    fishes_right = set()
    fishes_left = set()
    start_position = None
    warehouse_string, movements_rows = f.read().split("\n\n")
    rows = warehouse_string.splitlines()

    # Part 2
    extended_rows = []
    for y, row in enumerate(rows):
        extended_row = ""
        for x, cell in enumerate(row):
            if cell == "#":
                extended_row += "##"
            elif cell == "O":
                extended_row += "[]"
            elif cell == "@":
                extended_row += "@."
            else:
                extended_row += ".."
        extended_rows.append(extended_row)

    for y, row in enumerate(extended_rows):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            elif cell == "]":
                fishes_right.add((x, y))
            elif cell == "[":
                fishes_left.add((x, y))
            elif cell == "@":
                start_position = (x, y)

    movements = "".join(movements_rows.splitlines())

MAX_X = len(extended_rows[0])
MAX_Y = len(extended_rows)
PRINT_BOARD = False


def print_board(enable: bool, title: str):
    if not enable:
        return
    drawing = title + "\n"
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if (x, y) in walls:
                drawing += "#"
            elif (x, y) in fishes_left:
                drawing += "["
            elif (x, y) in fishes_right:
                drawing += "]"
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
    elif next_pos in fishes_left or next_pos in fishes_right:
        if move == "<" or move == ">":
            dx, dy = direction
            found_left = set() if move == "<" else {next_pos}
            found_right = set() if move == ">" else {next_pos}
            while True:
                check_pos = (next_pos[0] + dx, next_pos[1] + dy)
                if check_pos in walls:
                    break
                elif check_pos in fishes_left:
                    found_left.add(check_pos)
                    dx, dy = dx + direction[0], dy + direction[1]
                elif check_pos in fishes_right:
                    found_right.add(check_pos)
                    dx, dy = dx + direction[0], dy + direction[1]
                else:
                    # Space is found!
                    fishes_right -= found_right
                    fishes_left -= found_left

                    # Switcheroo - Seems wrong, but let me cook
                    if move == "<":
                        found_right.remove(next_pos)
                        found_right.add(check_pos)
                    else:
                        found_left.remove(next_pos)
                        found_left.add(check_pos)

                    fishes_left |= found_right
                    fishes_right |= found_left

                    current_pos = next_pos
                    break
        elif move == "^" or move == "v":

            dx, dy = direction
            found_left = set()
            found_right = set()
            frontier = {next_pos}

            wall_found = False

            while frontier:
                current_front = frontier.pop()
                front_x, front_y = current_front

                if current_front in walls:
                    wall_found = True
                    break

                if current_front in fishes_left:  # Left part of a fish found
                    found_left.add(current_front)
                    found_right.add((front_x + 1, front_y))
                    frontier |= {
                        (front_x, front_y + direction[1]),
                        (front_x + 1, front_y + direction[1]),
                    }
                elif current_front in fishes_right:  # Righ part of a fish found
                    found_right.add(current_front)
                    found_left.add((front_x - 1, front_y))
                    frontier |= {
                        (front_x, front_y + direction[1]),
                        (front_x - 1, front_y + direction[1]),
                    }

            if not wall_found:
                fishes_left -= found_left
                fishes_right -= found_right
                updated_left = set((x, y + direction[1]) for x, y in found_left)
                fishes_left |= updated_left
                updated_right = set((x, y + direction[1]) for x, y in found_right)
                fishes_right |= updated_right

                current_pos = next_pos
    else:
        # Space ahead
        current_pos = next_pos

    print_board(PRINT_BOARD, f"After move {idx} - {move}:")

part_2 = sum(y * 100 + x for x, y in fishes_left)
print("Part 2:", part_2)  # Part 1: 1476771, Part 2: 1468005
