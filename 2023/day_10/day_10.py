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

with open("input.txt") as f:
    lines = f.read().splitlines()
    cells = [[col for col in row] for row in lines]

MAX_ROW = len(cells)
MAX_COL = len(cells[0])

animal_position = None
for y, row in enumerate(cells):
    for x, cell in enumerate(row):
        if cell == S_ANIMAL:
            print("ANIMAL:", x, y)
            animal_position = (x, y)


# fmt: off
AoE = [
    (-1, -1), (+0,-1), (+1,-1),
    (-1, +0),          (+1,+0),
    (-1, +1), (+0,+1), (+1,+1),
]

ORTHOGONAL = (
              (+0,-1), 
    (-1, +0),          (+1,+0),
              (+0,+1), 
)
# fmt: on


def get_symbol(position: tuple[int, int]):
    return cells[position[1]][position[0]]


def try_go(from_position: tuple[tuple[int, int], int], direction: int) -> bool:
    assert direction in (NORTH, WEST, EAST, SOUTH), "INVALID DIRECTION PROVIDED!"

    (x, y), depth = from_position
    dx, dy = ORTHOGONAL[direction]
    to_position = (x + dx, y + dy)
    to_position_symbol = get_symbol(to_position)

    if to_position in visited:
        return False

    can_go = False
    if direction == NORTH:
        can_go = to_position_symbol in (S_VERTICAL_PIPE, S_SOUTH_EAST, S_SOUTH_WEST)
    elif direction == WEST:
        can_go = to_position_symbol in (S_HORIZONTAL_PIPE, S_NORTH_EAST, S_SOUTH_EAST)
    elif direction == EAST:
        can_go = to_position_symbol in (S_HORIZONTAL_PIPE, S_NORTH_WEST, S_SOUTH_WEST)
    elif direction == SOUTH:
        can_go = to_position_symbol in (S_VERTICAL_PIPE, S_NORTH_EAST, S_NORTH_WEST)

    if not can_go:
        return False

    to_visit.append((to_position, depth + 1))
    visited.add(to_position)
    return True


# PART 2 configs:
main_loop_pipes = set()

# fmt: off
init_data = (animal_position, 0)
visited = {init_data}
to_visit = [init_data]
while to_visit:
    current_data = to_visit.pop(0)
    current_position, depth = current_data
    (x, y) = current_position
    current_entity = cells[y][x]

    main_loop_pipes.add(current_position)

    print(f"{(x, y)} = ({current_entity}), {depth} steps away")

    if current_entity == S_GROUND:
        continue
    elif current_entity == S_ANIMAL:
        try_go(current_data, NORTH)
        try_go(current_data, WEST)
        try_go(current_data, EAST)
        try_go(current_data, SOUTH)
    elif current_entity == S_VERTICAL_PIPE:
        try_go(current_data, NORTH)
        try_go(current_data, SOUTH)
    elif current_entity == S_HORIZONTAL_PIPE:
        try_go(current_data, WEST)
        try_go(current_data, EAST)
    elif current_entity == S_NORTH_EAST:
        try_go(current_data, NORTH)
        try_go(current_data, EAST)
    elif current_entity == S_NORTH_WEST:
        try_go(current_data, NORTH)
        try_go(current_data, WEST)
    elif current_entity == S_SOUTH_EAST:
        try_go(current_data, SOUTH)
        try_go(current_data, EAST)
    elif current_entity == S_SOUTH_WEST:
        try_go(current_data, SOUTH)
        try_go(current_data, WEST)
    else:
        print("SOMETHING WRONG!")

# fmt: on

# current_data will be the last pipe-part visited
print("part 1:", current_data[1])  # 6923

print("\n\n")
for y in range(MAX_ROW):
    print()
    for x in range(MAX_COL):
        print("░" if (x, y) not in main_loop_pipes else "█", end="")

print("\n")
print("part 2")
