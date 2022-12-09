DEBUG = True
ZODIAC = "🐀🐂🐅🐇🐉🐍🐎🐐🐒🐓🐕🐖"
DIRECTIONS = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}


def print_rope(visit: set, rope: list, size: int = 20):
    if not DEBUG:
        return

    for Y in range(-size, size):
        print()
        for X in range(-size, size):
            if (0, 0) == (X, Y):
                print("⭐", end="")
            elif (X, Y) in rope:
                print(ZODIAC[rope.index((X, Y))], end="")
            else:
                print("🐾" if (X, Y) in visit else "⬛", end="")
    print(f"\n{len(visit)}", "spots")


def solve(commands: list, n_knots: int):
    visited = set()
    knots = [(0, 0) for _ in range(n_knots)]
    for direction, steps in commands:
        delta = DIRECTIONS[direction]
        for _ in range(steps):
            knots[0] = (knots[0][0] + delta[0], knots[0][1] + delta[1])  # HEAD
            for current in range(1, n_knots):
                (tx, ty), (hx, hy) = knots[current], knots[current - 1]
                diff = (tx - hx, ty - hy)
                if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                    if diff[0] != 0:
                        tx += 1 if diff[0] < 0 else -1
                    if diff[1] != 0:
                        ty += 1 if diff[1] < 0 else -1

                knots[current] = (tx, ty)

            visited.add(knots[-1])

    print_rope(visited, knots, 20)


with open("input.txt") as f:
    lines = list(map(lambda v: (v[0], int(v[1])), list(map(str.split, f.readlines()))))
    solve(lines, +2)  # PART 1: 5779
    solve(lines, 10)  # PART 2: 2331
