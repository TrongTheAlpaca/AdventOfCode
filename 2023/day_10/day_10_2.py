# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

S_VERTICAL_PIPE = "|"
S_HORIZONTAL_PIPE = "-"
S_NORTH_EAST = "L"
S_NORTH_WEST = "J"
S_SOUTH_WEST = "7"
S_SOUTH_EAST = "F"
S_GROUND = "."
S_ANIMAL = "S"

NORTH = 0
WEST = 1
EAST = 2
SOUTH = 3

COMPRESS_LEVEL = 4

# fmt: off
ORTHOGONAL = (
              (+0,-1), 
    (-1, +0),          (+1,+0),
              (+0,+1), 
)
# fmt: on

INPUT_FILE = "input.txt"
with open(INPUT_FILE) as f:
    lines = f.read().splitlines()
    cells = [[col for col in row] for row in lines]

MAX_ROW = len(cells)
MAX_COL = len(cells[0])


def get_symbol(cells_to_read_from, position: tuple[int, int]):
    return cells_to_read_from[position[1]][position[0]]


def check_if_direction_is_traversable(
    cells_to_read_from, from_position: tuple[int, int], direction: int
) -> bool:
    (x, y) = from_position
    dx, dy = ORTHOGONAL[direction]
    to_position = (x + dx, y + dy)
    to_position_symbol = get_symbol(cells_to_read_from, to_position)

    if direction == NORTH:
        return to_position_symbol in (S_VERTICAL_PIPE, S_SOUTH_EAST, S_SOUTH_WEST)
    elif direction == WEST:
        return to_position_symbol in (S_HORIZONTAL_PIPE, S_NORTH_EAST, S_SOUTH_EAST)
    elif direction == EAST:
        return to_position_symbol in (S_HORIZONTAL_PIPE, S_NORTH_WEST, S_SOUTH_WEST)
    elif direction == SOUTH:
        return to_position_symbol in (S_VERTICAL_PIPE, S_NORTH_EAST, S_NORTH_WEST)


animal_position = None
for y, row in enumerate(cells):
    for x, cell in enumerate(row):
        if cell == S_ANIMAL:
            print("ANIMAL:", x, y)
            animal_position = (x, y)

animal_pipe = None


def determine_pipe_under_animal(cells_to_read_from, animal_position):
    animal_can_go_north = check_if_direction_is_traversable(
        cells_to_read_from, animal_position, NORTH
    )
    animal_can_go_west = check_if_direction_is_traversable(
        cells_to_read_from, animal_position, WEST
    )
    animal_can_go_east = check_if_direction_is_traversable(
        cells_to_read_from, animal_position, EAST
    )
    animal_can_go_south = check_if_direction_is_traversable(
        cells_to_read_from, animal_position, SOUTH
    )

    if animal_can_go_north and animal_can_go_west:
        return S_NORTH_WEST
    elif animal_can_go_north and animal_can_go_east:
        return S_NORTH_EAST
    elif animal_can_go_south and animal_can_go_east:
        return S_SOUTH_EAST
    elif animal_can_go_south and animal_can_go_west:
        return S_SOUTH_WEST
    elif animal_can_go_west and animal_can_go_east:
        return S_HORIZONTAL_PIPE
    elif animal_can_go_north and animal_can_go_south:
        return S_VERTICAL_PIPE


animal_pipe = determine_pipe_under_animal(cells, animal_position)
assert animal_pipe is not None, "Invalid animal pipe state"


def transpose(array: list[list[str]]):
    return [*zip(*array)]


def try_go(
    cells_to_read_from,
    visited,
    to_visit,
    from_position: tuple[tuple[int, int], int],
    direction: int,
    main_pipe_set: set = None,
) -> bool:
    assert direction in (NORTH, WEST, EAST, SOUTH), "INVALID DIRECTION PROVIDED!"

    (x, y), depth = from_position
    dx, dy = ORTHOGONAL[direction]
    to_position = (x + dx, y + dy)

    if to_position in visited:
        return False

    can_go = check_if_direction_is_traversable(cells_to_read_from, (x, y), direction)

    if not can_go:
        return False

    to_visit.append((to_position, depth + 1))
    visited.add(to_position)
    main_pipe_set.add(to_position)

    return True


# fmt: off
main_loop_pipes = {animal_position}
init_data = (animal_position, 0)
visited = {init_data}
to_visit = [init_data]
while to_visit:
    current_data = to_visit.pop(0)
    current_position, depth = current_data
    (x, y) = current_position
    current_entity = cells[y][x]

    print(f"{(x, y)} = ({current_entity}), {depth} steps away")
    
    if current_entity == S_GROUND:
        continue
    elif current_entity == S_ANIMAL:
        try_go(cells, visited, to_visit,current_data, NORTH, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, WEST, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, EAST, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, SOUTH, main_loop_pipes)
    elif current_entity == S_VERTICAL_PIPE:
        try_go(cells, visited, to_visit,current_data, NORTH, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, SOUTH, main_loop_pipes)
    elif current_entity == S_HORIZONTAL_PIPE:
        try_go(cells, visited, to_visit,current_data, WEST, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, EAST, main_loop_pipes)
    elif current_entity == S_NORTH_EAST:
        try_go(cells, visited, to_visit,current_data, NORTH, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, EAST, main_loop_pipes)
    elif current_entity == S_NORTH_WEST:
        try_go(cells, visited, to_visit,current_data, NORTH, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, WEST, main_loop_pipes)
    elif current_entity == S_SOUTH_EAST:
        try_go(cells, visited, to_visit,current_data, SOUTH, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, EAST, main_loop_pipes)
    elif current_entity == S_SOUTH_WEST:
        try_go(cells, visited, to_visit,current_data, SOUTH, main_loop_pipes)
        try_go(cells, visited, to_visit,current_data, WEST, main_loop_pipes)
    else:
        print("SOMETHING WRONG!")

# fmt: on

# current_data will be the last pipe-part visited
print("part 1:", current_data[1])  # 6923


#############
# PART 2
#############


# DECOMPRESS
animal_position = None
with open(INPUT_FILE, "r") as f:
    original_lines = f.read().splitlines()

    # Remove all fake pipes
    for y in range(MAX_ROW):
        for x in range(MAX_COL):
            if (x, y) not in main_loop_pipes:
                original_lines[y] = (
                    original_lines[y][:x] + "." + original_lines[y][x + 1 :]
                )

    # Surround whole board with offset
    offsetted_lines = ["." + line + "." for line in original_lines]
    offsetted_lines = (
        ["." * len(offsetted_lines[0])]
        + offsetted_lines
        + ["." * len(offsetted_lines[0])]
    )

    expanded_lines = []
    for y, line in enumerate(offsetted_lines):
        # Repeat characters COMPRESS_LEVEL times horizontally
        new_line = ""
        for x, c in enumerate(line):
            if c == "S":
                c = animal_pipe
                animal_position = (x * (1 + COMPRESS_LEVEL), y * (1 + COMPRESS_LEVEL))

            new_line += c + (("-" if c in ["F", "-", "L"] else ".") * COMPRESS_LEVEL)

        expanded_lines.append(new_line)

    # Repeat lines COMPRESS_LEVEL times vertically
    cells = [[col for col in row] for row in expanded_lines]
    cells_T = transpose(cells)

    new_lines = []
    for y, row in enumerate(cells_T):
        new_line = ""
        for x, c in enumerate(row):
            new_line += c + (("|" if c in ["|", "F", "7"] else ".") * COMPRESS_LEVEL)

        new_lines.append(new_line)


cells_part_2 = [*zip(*new_lines)]


MAX_ROW = len(cells_part_2)
MAX_COL = len(cells_part_2[0])


# NOTE: Assume same pipe part under animal as part 1!

main_loop_pipes = {animal_position}
init_data = (animal_position, 0)
visited = {init_data}
to_visit = [init_data]
while to_visit:
    current_data = to_visit.pop(0)
    current_position, depth = current_data
    (x, y) = current_position
    current_entity = cells_part_2[y][x]

    # print(f"{(x, y)} = ({current_entity}), {depth} steps away")

    if current_entity == S_GROUND:
        continue
    elif current_entity == S_ANIMAL:
        try_go(cells_part_2, visited, to_visit, current_data, NORTH, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, WEST, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, EAST, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, SOUTH, main_loop_pipes)
    elif current_entity == S_VERTICAL_PIPE:
        try_go(cells_part_2, visited, to_visit, current_data, NORTH, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, SOUTH, main_loop_pipes)
    elif current_entity == S_HORIZONTAL_PIPE:
        try_go(cells_part_2, visited, to_visit, current_data, WEST, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, EAST, main_loop_pipes)
    elif current_entity == S_NORTH_EAST:
        try_go(cells_part_2, visited, to_visit, current_data, NORTH, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, EAST, main_loop_pipes)
    elif current_entity == S_NORTH_WEST:
        try_go(cells_part_2, visited, to_visit, current_data, NORTH, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, WEST, main_loop_pipes)
    elif current_entity == S_SOUTH_EAST:
        try_go(cells_part_2, visited, to_visit, current_data, SOUTH, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, EAST, main_loop_pipes)
    elif current_entity == S_SOUTH_WEST:
        try_go(cells_part_2, visited, to_visit, current_data, SOUTH, main_loop_pipes)
        try_go(cells_part_2, visited, to_visit, current_data, WEST, main_loop_pipes)
    else:
        print("SOMETHING WRONG!")

# fmt: on

# Try vistiting the animal's cool fort, however you are closed outside :(
current_pos = (0, 0)
visited = set()
to_visit = [current_pos]
while to_visit:
    current_pos = to_visit.pop()
    (x, y) = current_pos
    to_check = []
    for dx, dy in ORTHOGONAL:
        x2 = x + dx
        y2 = y + dy
        if 0 <= x2 < MAX_COL and 0 <= y2 < MAX_ROW:
            to_check.append((x2, y2))

    for check in to_check:
        if check not in visited:
            if check not in main_loop_pipes:
                to_visit.append(check)
                visited.add(check)
            else:
                visited.add(check)

visited_ground = visited - main_loop_pipes
new_map = ["" for x in range(MAX_ROW - 1)]
for y in range(MAX_ROW - 1):
    for x in range(MAX_COL - 1):
        new_map[y] += (
            "O" if (x, y) in visited_ground else get_symbol(cells_part_2, (x, y))
        )

with open("TEST_OUTPUT_1.txt", "w") as out_f:
    for y, row in enumerate(new_map):
        out_f.write(row + "\n")


# COMPRESS
with open("TEST_OUTPUT_1.txt", "r") as f:
    lines = f.read().splitlines()

    # HORIZONTAL
    new_lines_compress_x = []
    for line in lines:
        new_line = line[:: COMPRESS_LEVEL + 1]
        new_lines_compress_x.append(list(new_line))

    # VERTICAL
    new_lines_compress_y = []
    for line in transpose(new_lines_compress_x):
        new_line = line[:: COMPRESS_LEVEL + 1]
        new_lines_compress_y.append(new_line)

with open("TEST_OUTPUT_2.txt", "w") as out_f:
    out_f.write(
        "\n".join(["".join(line_list) for line_list in [*zip(*new_lines_compress_y)]])
    )


with open("TEST_OUTPUT_2.txt", "r") as f:
    print("part_2", f.read().count("."))  # 529
