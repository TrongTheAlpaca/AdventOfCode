DEBUG = False

with open("input.txt") as f:
    rows = [list(map(int, line)) for line in f.read().splitlines()]

HEIGHT = len(rows)
WIDTH = len(rows[0])


def print_forest(header: str, s: set, spot: tuple = None):
    if not DEBUG:
        return

    print(f"\n{header}", end="")
    for Y in range(HEIGHT):
        print()
        for X in range(WIDTH):
            print("👀" if spot == (X, Y) else "🌲" if (X, Y) in s else "⬛", end="")

    print(f"\n{len(s)} trees spotted")


SYMBOL, IS_HORIZONTAL, RANGE_0, RANGE_1 = 0, 1, 2, 3  # Indices
spotted: set[tuple[int, int]] = set()
for O in [
    ("dir: ▶", True, range(HEIGHT), range(WIDTH)),
    ("dir: ◀", True, range(HEIGHT), range(WIDTH - 1, -1, -1)),
    ("dir: ▼", False, range(WIDTH), range(HEIGHT)),
    ("dir: ▲", False, range(WIDTH), range(HEIGHT - 1, -1, -1)),
]:
    current_spotted = set()
    for Y in O[RANGE_0]:
        prev_tree = -1
        for X in O[RANGE_1]:
            current_height = rows[Y][X] if O[IS_HORIZONTAL] else rows[X][Y]
            if prev_tree < current_height:
                current_spotted.add((X, Y) if O[IS_HORIZONTAL] else (Y, X))
                prev_tree = current_height

    print_forest(O[SYMBOL], current_spotted)
    spotted |= current_spotted

print_forest("⭕", spotted)
print("PART 1:", len(spotted))  # PART 1: 1776


# PART 2
IS_HORIZONTAL, DX, DY = 0, 1, 2  # Indices

scenic_scores = []
for Y in range(HEIGHT):
    for X in range(WIDTH):
        spotted = set()
        scenic_score = 1

        for O in [(True, 1, 0), (True, -1, 0), (False, 0, 1), (False, 0, -1)]:
            current_spotted = set()
            x, y = X + O[DX], Y + O[DY]
            while 0 <= x < WIDTH and 0 <= y < HEIGHT:
                current_spotted.add((x, Y) if O[IS_HORIZONTAL] else (X, y))

                if (rows[Y][x] if O[IS_HORIZONTAL] else rows[y][X]) >= rows[Y][X]:
                    break

                x += O[DX]
                y += O[DY]

            scenic_score *= len(current_spotted)
            spotted |= current_spotted

        print_forest(f"X={X},Y={Y}", spotted, (X, Y))
        if DEBUG:
            print("scenic score:", scenic_score)
        scenic_scores.append(scenic_score)

print("PART 2:", max(scenic_scores))  # PART 2: 234416
