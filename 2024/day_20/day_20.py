from collections import defaultdict
from tqdm import tqdm

with open("input.txt", "r") as f:
    rows = f.readlines()

walls = set()
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == "#":
            walls.add((x, y))
        elif cell == "S":
            start_pos = (x, y)
        elif cell == "E":
            end_pos = (x, y)

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

DIRECTIONS = [UP, DOWN, RIGHT, LEFT]

steps = 0
current_pos = start_pos
visited = {current_pos: 0}
while current_pos != end_pos:
    x, y = current_pos
    for dx, dy in DIRECTIONS:
        next_pos = x + dx, y + dy
        if next_pos in walls:
            continue
        if next_pos in visited:
            continue

        current_pos = next_pos
        break

    steps += 1
    visited[current_pos] = steps

saved_seconds_part_1 = defaultdict(lambda: 0)
saved_seconds_part_2 = defaultdict(lambda: 0)
for x, y in tqdm(visited.keys()):
    cost = visited[(x, y)]
    for dx in range(-20, 20 + 1):
        for dy in range(-20, 20 + 1):
            if (abs(dx) + abs(dy)) > 20:
                continue
            next_pos = (x + dx, y + dy)
            if next_pos in visited:
                other_cost = visited[next_pos]
                distance = abs(dx) + abs(dy)
                saved_seconds = other_cost - (distance + cost)
                saved_seconds_part_2[saved_seconds] += 1
                if distance <= 2:
                    saved_seconds_part_1[saved_seconds] += 1


part_1 = sum({k: v for k, v in saved_seconds_part_1.items() if 100 <= k}.values())
part_2 = sum({k: v for k, v in saved_seconds_part_2.items() if 100 <= k}.values())

print("Part 1:", part_1)  # Part 1: 1404
print("Part 2:", part_2)  # Part 2: 1010981
