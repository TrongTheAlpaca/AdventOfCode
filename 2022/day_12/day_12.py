DEBUG = False
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# PREAMBLE
with open("input.txt") as f:
    rows = f.read().splitlines()

all_starts = []
start_p1, GOAL = None, None
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == "S":
            start_p1 = (x, y)
            all_starts.append((x, y))
        elif cell == "a":
            all_starts.append((x, y))
        elif cell == "E":
            GOAL = (x, y)

rows[start_p1[1]] = rows[start_p1[1]].replace("S", "a")
rows[GOAL[1]] = rows[GOAL[1]].replace("E", "z")

HEIGTH = len(rows)
LENGTH = len(rows[0])


def print_trail(_trail: list):
    for y in range(HEIGTH):
        print()
        for x in range(LENGTH):
            if (x, y) not in _trail:
                print(".", end="")
            else:
                n = _trail.index((x, y)) - 1
                dx, dy = _trail[n]
                if dx < x:
                    print("<", end="")
                elif dx > x:
                    print(">", end="")
                elif dy > y:
                    print("V", end="")
                else:
                    print("^", end="")
    print()


def solve(matrix: list, start: tuple, goal: tuple):
    trail = {start: None}
    cost = {start: 0}
    priority_queue = [start]
    while priority_queue:

        priority_queue.sort(key=lambda x: cost[x], reverse=True)
        current = priority_queue.pop()

        if current == goal:
            break

        x, y = current
        for dx, dy in DIRECTIONS:
            neighbor = x + dx, y + dy
            xn, yn = neighbor

            if 0 <= xn < LENGTH and 0 <= yn < HEIGTH:
                if ord(matrix[yn][xn]) <= ord(matrix[y][x]) + 1:
                    new_cost = cost[current] + 1

                    if neighbor not in cost or new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        priority_queue.append(neighbor)
                        trail[neighbor] = current

    if DEBUG:
        print(f"Start: {start}", "- ", end="")
    if goal in trail:
        full_trail = []
        c = goal
        while c != start:
            c = trail[c]
            full_trail.append(c)

        if DEBUG:
            print(len(full_trail))
            print_trail(full_trail)

        return len(full_trail)
    else:
        if DEBUG:
            print("DNF")
        return None


# PART 1
print("PART 1", solve(rows, start_p1, GOAL))  # 504

# PART 2
lengths = [solve(rows, s, GOAL) for s in all_starts]
lengths = [l for l in lengths if l is not None]
print("PART 2", min(lengths))  # 500
