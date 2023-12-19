def rotate_cw(array):
    return list(zip(*array[::-1]))


class Entity:
    def __init__(self, x: int, y: int, symbol: str, weight: int):
        self.x = x
        self.y = y
        self.coordinate = str((x, y))
        self.symbol: str = symbol
        self.weight: int = weight

    def __repr__(self):
        return self.symbol

    def change_symbol(self, new_symbol: str):
        self.symbol = new_symbol
        return self

    def __hash__(self) -> int:
        return hash(f"{self.x}{self.y}{self.symbol}")


# Smooth solution, however, only works on strings :(
# def move_row_for_string(row: list) -> list:
#     row_reversed = row[::-1]
#     new_row = ""
#     new_space = ""
#     for symbol in row_reversed:
#         if symbol == ".":
#             new_space += "."
#         elif symbol == "O":
#             new_row += symbol
#         else:
#             new_row += new_space
#             new_space = ""
#             new_row += "#"

#     if new_space != "":
#         new_row += new_space

#     return new_row[::-1]


def move_row(row: list[Entity]) -> list[Entity]:
    row_reversed = reversed(row)
    new_row = ""
    new_space = ""
    for entity in row_reversed:
        if entity.symbol == ".":
            new_space += "."
        elif entity.symbol == "O":
            new_row += "O"
        else:
            new_row += new_space
            new_space = ""
            new_row += "#"

    if new_space != "":
        new_row += new_space

    new_row = new_row[::-1]

    return [entity.change_symbol(symbol) for entity, symbol in zip(row, new_row)]


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    # lines_R = rotate_cw(lines)

WIDTH = len(lines[0])
HEIGHT = len(lines)

entities = []
board = []
for y, row in enumerate(lines):
    board_row = []
    for x, cell in enumerate(row):
        new_entity = Entity(x, y, cell, HEIGHT - y)
        board_row.append(new_entity)
        entities.append(new_entity)
    board.append(board_row)

board_rotations = [board]
for _ in range(3):
    board = rotate_cw(board)
    board_rotations.append(board)


def move_board(direction: int) -> list[list[list[Entity]]]:
    for row in board_rotations[direction]:
        row = move_row(row)
    return board_rotations[direction]


def get_current_north_load() -> int:
    return sum(e.weight for e in entities if e.symbol == "O")


def get_board_hash():
    final_hash = 0
    for e in entities:
        final_hash ^= hash(e)
    return final_hash


EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


hashes = set()
first_hash = None
second_hash = None
for i in range(1_000_000_000):
    move_board(NORTH)
    move_board(WEST)
    move_board(SOUTH)
    move_board(EAST)
    h = get_board_hash()
    if h in hashes:
        print(f"HASH FOUND AT {i}!")

        if not first_hash:
            first_hash = i
        elif not second_hash:
            second_hash = i

            diff = second_hash - first_hash
            m = (1_000_000_000 - (i + 1)) % diff
            print()
            for _ in range(m):
                move_board(NORTH)
                move_board(WEST)
                move_board(SOUTH)
                move_board(EAST)
            print("Part 2:", get_current_north_load())  # 93102
            break

        hashes.clear()
    hashes.add(h)
