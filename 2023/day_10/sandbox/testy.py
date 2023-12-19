N = 1

# DECOMPRESS
with open("test_in_4.txt", "r") as f:
    expanded_lines = []
    for line in f:
        # Repeat characters N times horizontally
        new_line = ""
        for c in line:
            if c == ".":
                new_line += "." + ("." * N)
            elif c == "|":
                new_line += "|" + ("." * N)
            elif c == "F":
                new_line += "F" + ("-" * N)
            elif c == "-":
                new_line += "-" + ("-" * N)
            elif c == "J":
                new_line += "J" + ("." * N)
            elif c == "7":
                new_line += "7" + ("." * N)
            elif c == "L":
                new_line += "L" + ("-" * N)

        # Repeat lines N times vertically
        expanded_lines.append(new_line)

    cells = [[col for col in row] for row in expanded_lines]
    cells_T = [*zip(*cells)]

    new_lines = []
    for y, row in enumerate(cells_T):
        new_line = ""
        for x, c in enumerate(row):
            if c == ".":
                new_line += "." + ("." * N)
            elif c == "|":
                new_line += "|" + ("|" * N)
            elif c == "F":
                new_line += "F" + ("|" * N)
            elif c == "-":
                new_line += "-" + ("." * N)
            elif c == "J":
                new_line += "J" + ("." * N)
            elif c == "7":
                new_line += "7" + ("|" * N)
            elif c == "L":
                new_line += "L" + ("." * N)

        new_lines.append(new_line)

with open("test_out_2.txt", "w") as out_f:
    correct_transposed_lines = [*zip(*new_lines)]
    lines = "\n".join("".join(line) for line in correct_transposed_lines)
    out_f.write(lines)

## MAIN

with open("test_out_2.txt", "r") as f:
    lines = f.read().splitlines()
    cells = [[col for col in row] for row in lines]


MAX_ROW = len(cells)
MAX_COL = len(cells[0])


def get_symbol(position: tuple[int, int]):
    return cells[position[1]][position[0]]


ORTHOGONAL = (
    (+0, -1),
    (-1, +0),
    (+1, +0),
    (+0, +1),
)

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
            if get_symbol(check) == ".":  # if not in main pipe INSTEAD
                to_visit.append(check)
                visited.add(check)
            else:
                visited.add(check)

# MOCK MAIN LOOP, USE REAL IN ACTUAL
main_loop_pipes = set()
new_map = ["" for x in range(MAX_ROW - 1)]
for y in range(MAX_ROW):
    for x in range(MAX_COL):
        if get_symbol((x, y)) != ".":
            main_loop_pipes.add((x, y))


print("\n\n")
visited_ground = visited - main_loop_pipes
new_map = ["" for x in range(MAX_ROW - 1)]
for y in range(MAX_ROW - 1):
    for x in range(MAX_COL - 1):
        new_map[y] += "O" if (x, y) in visited_ground else get_symbol((x, y))

with open("test_out_3.txt", "w") as out_f:
    for y, row in enumerate(new_map):
        out_f.write(row + "\n")

# COMPRESS
with open("test_out_3.txt", "r") as f:
    lines = f.read().splitlines()

    # HORIZONTAL
    new_lines_compress_x = []
    for line in lines:
        new_line = line[:: N + 1]
        new_lines_compress_x.append(list(new_line))

    # VERTICAL
    new_lines_compress_y = []
    for line in [*zip(*new_lines_compress_x)]:
        new_line = line[:: N + 1]
        print(new_line)
        new_lines_compress_y.append(new_line)

with open("test_out_4.txt", "w") as out_f:
    out_f.write(
        "\n".join(["".join(line_list) for line_list in [*zip(*new_lines_compress_y)]])
    )


with open("test_out_4.txt", "r") as f:
    print("part_2", f.read().count("."))
