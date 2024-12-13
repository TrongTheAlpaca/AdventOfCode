with open("input.txt", "r") as f:
    rows = f.read().splitlines()

MAX_X = len(rows[0])
MAX_Y = len(rows)

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

rows = [list(map(lambda n: int(n) if n != "." else None, row)) for row in rows]

start_positions = set()
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == 0:
            start_positions.add((x, y))

part_result = [0, 0]
all_visited = set()
for part in [0, 1]:
    start_positions_copy = start_positions.copy()
    while start_positions_copy:
        n_trailheads = 0
        start_pos = start_positions_copy.pop()
        queue = [start_pos]
        visited = set()
        while queue:
            (x, y) = queue.pop()

            if part == 0:
                if (x, y) in visited:
                    continue

            visited.add((x, y))

            if rows[y][x] == 9:
                n_trailheads += 1
                continue

            for x2, y2 in [UP, LEFT, RIGHT, DOWN]:
                next_pos = (x + x2, y + y2)
                if 0 <= next_pos[0] < MAX_X and 0 <= next_pos[1] < MAX_Y:
                    value = rows[next_pos[1]][next_pos[0]]
                    if value is not None and rows[y][x] + 1 == value:
                        queue.append(next_pos)

        part_result[part] += n_trailheads
        all_visited |= visited

        # for y, row in enumerate(rows):
        #     for x, cell in enumerate(row):
        #         if (x, y) in visited:
        #             print(cell, end="")
        #         else:
        #             print(".", end="")
        #     print()

print("Part 1:", part_result[0])  # 468
print("Part 2:", part_result[1])  # 966
