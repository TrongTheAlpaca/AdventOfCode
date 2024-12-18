import queue

with open("input.txt", "r") as f:
    bytes = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

START_N_BYTES = 1024
GRID_LENGTH = 71

START_POS = (0, 0)
GOAL = (GRID_LENGTH - 1, GRID_LENGTH - 1)

part_1_bytes = set(bytes[:START_N_BYTES])

drawing = ""
for y in range(GRID_LENGTH):
    for x in range(GRID_LENGTH):
        if (x, y) not in part_1_bytes:
            drawing += "."
        else:
            drawing += "#"
    drawing += "\n"
print(drawing)


def try_escape(walls: set):

    if START_POS in walls:
        return None

    visited = {START_POS: 0}
    frontier = queue.PriorityQueue()
    frontier.put((0, START_POS, {START_POS}))

    while not frontier.empty():
        current_cost, current_pos, current_trail = frontier.get()

        if current_pos == GOAL:
            return current_cost, current_trail

        for dx, dy in [UP, LEFT, RIGHT, DOWN]:
            next_pos = current_pos[0] + dx, current_pos[1] + dy
            x2, y2 = next_pos

            if not (0 <= x2 < GRID_LENGTH and 0 <= y2 < GRID_LENGTH):
                continue

            if next_pos in walls:
                continue

            if next_pos not in visited or next_cost < visited[next_pos]:
                next_cost = current_cost + 1
                visited[next_pos] = next_cost
                frontier.put((next_cost, next_pos, current_trail | {next_pos}))

    return None


# Part 1
cost, trail = try_escape(part_1_bytes)

drawing = ""
for y in range(GRID_LENGTH):
    for x in range(GRID_LENGTH):
        if (x, y) in part_1_bytes:
            drawing += "#"
        elif (x, y) in trail:
            drawing += "O"
        else:
            drawing += "."
    drawing += "\n"
print(drawing)

print("Part 1:", cost)

# part 2
n_bytes = START_N_BYTES
while True:

    current_walls = set(bytes[:n_bytes])
    result = try_escape(current_walls)

    if result is None:
        break

    cost, trail = result
    print(f"\rNumber of bytes: {n_bytes}", end="", flush=True)
    n_bytes += 1

ending_byte = (set(bytes[:n_bytes]) - set(bytes[: n_bytes - 1])).pop()
print(f"\nPart 2: {ending_byte[0]},{ending_byte[1]}")
# Part 2:  27,60
