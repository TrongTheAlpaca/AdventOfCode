# PREAMBLE
with open("input") as f:
    rows: list[list[int]] = [[int(n) for n in line] for line in f.read().split('\n')]

delta_AOE = [(-1, -1), (0, -1), (1, -1),
             (-1,  0),          (1,  0),
             (-1,  1), (0,  1), (1,  1)]

total_flash_per_step = []
while not all(max(row) == 0 for row in rows):

    rows = [[n + 1 for n in row] for row in rows]  # General step incrementation

    while not all(max(row) <= 9 for row in rows):
        for y in range(len(rows)):
            for x in range(len(rows[0])):
                if 9 < rows[y][x] != 0:
                    rows[y][x] = 0
                    for dx, dy in delta_AOE:
                        if 0 <= x + dx < len(rows[0]) and 0 <= y + dy < len(rows) and rows[y + dy][x + dx] != 0:
                            rows[y + dy][x + dx] += 1

    total_flash_per_step.append(sum([r.count(0) for r in rows]))

print("Total Flashes at step 100:", sum(total_flash_per_step[:100]))  # PART 1: 1625 is correct
print("First synchronized flash:", len(total_flash_per_step))        # PART 2:  244 is correct
