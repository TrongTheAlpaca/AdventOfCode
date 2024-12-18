import queue

with open("input.txt", "r") as f:
    rows = f.read().splitlines()

MAX_X = len(rows[0])
MAX_Y = len(rows)

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

ROTATE_COST = {
    UP: {UP: 0, RIGHT: 1000, LEFT: 1000, DOWN: 2000},
    DOWN: {DOWN: 0, RIGHT: 1000, LEFT: 1000, UP: 2000},
    LEFT: {LEFT: 0, UP: 1000, DOWN: 1000, RIGHT: 2000},
    RIGHT: {RIGHT: 0, UP: 1000, DOWN: 1000, LEFT: 2000},
}

BACKWARD = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}

walls = set()
start_pos = None
goal = None
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == "#":
            walls.add((x, y))
        elif cell == "S":
            start_pos = (x, y)
        elif cell == "E":
            goal = (x, y)

pqueue = queue.PriorityQueue()
pqueue.put((0, (start_pos, RIGHT), {start_pos}))
visited = {(start_pos, RIGHT): 0}
best_cost = None
all_best_seats = set()
while not pqueue.empty():
    current_cost, current_key, current_trail = pqueue.get()
    current_pos, current_direction = current_key

    if best_cost:
        if current_cost > best_cost:
            break  # All optimal paths have been visited at this point.

    if current_pos == goal:
        if not best_cost:
            best_cost = current_cost

        all_best_seats |= current_trail
        continue

    for next_direction in [UP, DOWN, RIGHT, LEFT]:

        if next_direction == BACKWARD[current_direction]:
            continue

        dx, dy = next_direction
        next_pos = current_pos[0] + dx, current_pos[1] + dy

        if next_pos in walls:
            continue

        next_cost = current_cost + ROTATE_COST[current_direction][next_direction] + 1
        next_key = (next_pos, next_direction)

        if next_key not in visited or next_cost <= visited[next_key]:
            visited[next_key] = next_cost
            pqueue.put((next_cost, next_key, current_trail | {next_pos}))

drawing = ""
for y in range(MAX_Y):
    for x in range(MAX_X):
        if (x, y) in walls:
            drawing += "#"
        elif (x, y) in all_best_seats:
            drawing += "O"
        else:
            drawing += "."
    drawing += "\n"
print(drawing)
print()

print("Part 1:", best_cost)  # Part 1 73432
print("Part 2:", len(all_best_seats))  # Part 2: 496
