# PREAMBLE
with open("input") as f:
    lines = [n.rstrip().split(' -> ') for n in f.readlines()]
    lines = [(tuple(map(int, x[0].split(','))), tuple(map(int, x[1].split(',')))) for x in lines]


def calculate_overlap(include_diagonal=False):

    vent_map = [[0 for _ in range(1000)] for _ in range(1000)]

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            # Vertical Line
            if y1 > y2:
                y1, y2 = y2, y1

            while y1 <= y2:
                vent_map[x1][y1] += 1
                y1 += 1

        elif y1 == y2:
            # Horizontal Line
            if x1 > x2:
                x1, x2 = x2, x1

            while x1 <= x2:
                vent_map[x1][y1] += 1
                x1 += 1

        elif include_diagonal:
            d_x = x2 - x1
            d_y = y2 - y1

            # left-down
            if d_x < 0 and d_y < 0:
                while x2 <= x1:
                    vent_map[x2][y2] += 1
                    x2 += 1
                    y2 += 1

            # right-up
            elif d_x > 0 and d_y > 0:
                while x1 <= x2:
                    vent_map[x1][y1] += 1
                    x1 += 1
                    y1 += 1

            # right-down
            elif d_x > 0 and d_y < 0:
                while x1 <= x2:
                    vent_map[x1][y1] += 1
                    x1 += 1
                    y1 -= 1

            # left-up
            else:
                while x2 <= x1:
                    vent_map[x2][y2] += 1
                    x2 += 1
                    y2 -= 1

    n_overlap = 0
    for row in vent_map:
        n_overlap += sum(map(lambda x: x > 1, row))

    return n_overlap


print(calculate_overlap(False))  # PART 1 -  6005
print(calculate_overlap(True))   # PART 2 - 23864
