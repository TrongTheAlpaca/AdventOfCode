# PREAMBLE
with open("input") as f:
    rows = [[int(n) for n in list(line)] for line in f.read().split('\n')]
    rows = [[9] * (len(rows[0]) + 2)] + [[9] + row + [9] for row in rows] + [[9] * (len(rows[0]) + 2)]  # Padding nines

# PART 1
coordinates = []
for r in range(1, len(rows) - 1):
    for c in range(1, len(rows[0]) - 1):
        if all(rows[r][c] < rows[r + dy][c + dx] for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]):
            coordinates.append((c, r))

print(sum([rows[y][x] + 1 for x, y in coordinates]))  # PART 1: 465 is correct!


# PART 2
def count_adjacent_elevations(x, y):
    if rows[y][x] == 9:
        return 0

    rows[y][x] = 9

    return 1 + sum([count_adjacent_elevations(x, y - 1),   # UP
                    count_adjacent_elevations(x, y + 1),   # DOWN
                    count_adjacent_elevations(x - 1, y),   # LEFT
                    count_adjacent_elevations(x + 1, y)])  # RIGHT


basins = sorted([count_adjacent_elevations(x, y) for x, y in coordinates], reverse=True)
print(basins[0] * basins[1] * basins[2])  # PART 2: 1269555 is correct!
