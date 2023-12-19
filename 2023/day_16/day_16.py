with open("input.txt", "r") as f:
    board = f.read().splitlines()


mirrors = {}
for y, row in enumerate(board):
    for x, cell in enumerate(row):
        if cell != ".":
            mirrors[(x, y)] = cell


WIDTH = len(board[0])
HEIGTH = len(board)

NORTH = (+0, -1)
WEST = (-1, +0)
SOUTH = (+0, +1)
EAST = (+1, +0)


def get_pos(position: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    (dx, dy) = direction
    x, y = position
    return (x + dx, y + dy), direction


def shoot_laser(start_position, start_direction):
    visited = set()
    energized = set()
    active_lasers = [(start_position, start_direction)]

    while active_lasers:
        current_position, direction = active_lasers.pop()
        (x, y) = current_position

        if not (0 <= x < WIDTH and 0 <= y < HEIGTH):
            continue

        if (current_position, direction) in visited:
            continue

        energized.add((x, y))
        visited.add(((x, y), direction))

        if current_position not in mirrors:
            active_lasers.append(get_pos(current_position, direction))
        else:
            mirror = mirrors[current_position]

            if mirror == ".":
                active_lasers.append(get_pos(current_position, direction))
            elif mirror == "-":
                if direction in [NORTH, SOUTH]:
                    active_lasers.append(get_pos(current_position, WEST))
                    active_lasers.append(get_pos(current_position, EAST))
                else:
                    active_lasers.append(get_pos(current_position, direction))

            elif mirror == "|":
                if direction in [WEST, EAST]:
                    active_lasers.append(get_pos(current_position, NORTH))
                    active_lasers.append(get_pos(current_position, SOUTH))
                else:
                    active_lasers.append(get_pos(current_position, direction))

            elif mirror == "/":
                if direction == NORTH:
                    active_lasers.append(get_pos(current_position, EAST))
                elif direction == WEST:
                    active_lasers.append(get_pos(current_position, SOUTH))
                elif direction == SOUTH:
                    active_lasers.append(get_pos(current_position, WEST))
                elif direction == EAST:
                    active_lasers.append(get_pos(current_position, NORTH))

            elif mirror == "\\":
                if direction == NORTH:
                    active_lasers.append(get_pos(current_position, WEST))
                elif direction == WEST:
                    active_lasers.append(get_pos(current_position, NORTH))
                elif direction == SOUTH:
                    active_lasers.append(get_pos(current_position, EAST))
                elif direction == EAST:
                    active_lasers.append(get_pos(current_position, SOUTH))

    # Print Board w/ energized cells
    # for y in range(HEIGTH):
    #     print()
    #     for x in range(WIDTH):
    #         cursor = "."
    #         if (x, y) in mirrors:
    #             cursor = mirrors[(x, y)]
    #         if (x, y) in energized:
    #             cursor = "#"

    #         print(cursor, end="")
    #     print()

    return len(energized)


n_energized = shoot_laser((0, 0), EAST)

print("Part 1:", n_energized)  # 7199


energized_results = []
for x in range(WIDTH):
    energized_results.append(shoot_laser((x, 0), SOUTH))
    energized_results.append(shoot_laser((x, HEIGTH - 1), NORTH))

for y in range(HEIGTH):
    energized_results.append(shoot_laser((0, y), EAST))
    energized_results.append(shoot_laser((WIDTH - 1, y), WEST))


print("Part 2:", max(energized_results))  # 7438
