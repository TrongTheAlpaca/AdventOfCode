with open("input.txt") as f:
    rows = [list(map(int, line)) for line in f.read().splitlines()]

DEBUG = False


def print_spotted(header: str, spotted: set, spot: tuple = None):
    if not DEBUG:
        return

    print(f"\n{header}", end="")
    for Y in range(HEIGHT):
        print()
        for X in range(WITDH):
            if spot == (X, Y):
                print("👀", end="")
            else:
                print("🌲" if (X, Y) in spotted else "⬛", end="")
    print(f"\n{len(spotted)} trees spotted")


spotted: set[tuple[int, int]] = set()

HEIGHT = len(rows)
WITDH = len(rows[0])

current_spotted = set()
for Y in range(HEIGHT):
    prev_tree = -1
    for X in range(WITDH):
        current_height = rows[Y][X]
        if prev_tree < current_height:
            current_spotted.add((X, Y))
            prev_tree = current_height

print_spotted("▶", current_spotted)
spotted |= current_spotted


current_spotted = set()
for Y in range(HEIGHT):
    prev_tree = -1
    for X in reversed(range(WITDH)):
        current_height = rows[Y][X]
        if prev_tree < current_height:
            current_spotted.add((X, Y))
            prev_tree = current_height
print_spotted("◀", current_spotted)
spotted |= current_spotted


current_spotted = set()
for X in range(WITDH):
    prev_tree = -1
    for Y in range(HEIGHT):
        current_height = rows[Y][X]
        if prev_tree < current_height:
            current_spotted.add((X, Y))
            prev_tree = current_height
print_spotted("🔻", current_spotted)
spotted |= current_spotted


current_spotted = set()
for X in range(WITDH):
    prev_tree = -1
    for Y in reversed(range(HEIGHT)):
        current_height = rows[Y][X]
        if prev_tree < current_height:
            current_spotted.add((X, Y))
            prev_tree = current_height
print_spotted("🔺", current_spotted)
spotted |= current_spotted

print_spotted("⭕", spotted)  # PART 1: 1776


# PART 2
scenic_scores = []
for Y in range(HEIGHT):
    for X in range(WITDH):

        original = rows[Y][X]

        spotted = set()

        scenic_score = 1

        # RIGHT
        current_spotted = set()
        x_current = X + 1
        while x_current < WITDH:
            current_spotted.add((x_current, Y))

            if rows[Y][x_current] >= original:
                break

            x_current += 1

        scenic_score *= len(current_spotted)
        spotted |= current_spotted

        # LEFT
        current_spotted = set()
        x_current = X - 1
        while x_current >= 0:
            current_spotted.add((x_current, Y))

            if rows[Y][x_current] >= original:
                break

            x_current -= 1

        scenic_score *= len(current_spotted)
        spotted |= current_spotted

        # UP
        current_spotted = set()
        y_current = Y - 1
        while y_current >= 0:
            current_spotted.add((X, y_current))

            if rows[y_current][X] >= original:
                break

            y_current -= 1

        scenic_score *= len(current_spotted)
        spotted |= current_spotted

        # DOWN
        current_spotted = set()
        y_current = Y + 1
        while y_current < HEIGHT:
            current_spotted.add((X, y_current))

            if rows[y_current][X] >= original:
                break

            y_current += 1

        scenic_score *= len(current_spotted)
        spotted |= current_spotted

        print_spotted(f"X={X},Y={Y}", spotted, (X, Y))
        print("scenic score:", scenic_score)
        scenic_scores.append(scenic_score)

print("PART 2:", max(scenic_scores))  # PART 2: 234416
