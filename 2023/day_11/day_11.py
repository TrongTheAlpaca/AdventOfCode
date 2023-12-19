with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def solve(input, is_part_2):
    N_expansion = 1 if not is_part_2 else 1_000_000 - 1

    def transpose(array: list[list[str]]):
        return ["".join(t) for t in [*zip(*array)]]

    no_galaxies_y = []
    new_lines = input.copy()
    for y, row in enumerate(new_lines):
        if "#" not in row:
            no_galaxies_y.append(y)

    no_galaxies_y_expanded = []
    for i, y in enumerate(no_galaxies_y):
        no_galaxies_y_expanded.append(y + (i * N_expansion))

    no_galaxies_x = []
    new_lines = transpose(new_lines)
    for x, col in enumerate(new_lines):
        if "#" not in col:
            no_galaxies_x.append(x)

    no_galaxies_x_expanded = []
    for i, x in enumerate(no_galaxies_x):
        no_galaxies_x_expanded.append(x + (i * N_expansion))

    def manhatten_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
        x0, x1 = min(a[0], b[0]), max(a[0], b[0])
        y0, y1 = min(a[1], b[1]), max(a[1], b[1])

        for e_x in no_galaxies_x_expanded:
            if e_x <= x0:
                x0 += N_expansion
                x1 += N_expansion
            elif x0 <= e_x <= x1:
                x1 += N_expansion

        for e_y in no_galaxies_y_expanded:
            if e_y <= y0:
                y0 += N_expansion
                y1 += N_expansion
            elif y0 <= e_y <= y1:
                y1 += N_expansion

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        return dx + dy

    galaxies = []
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((x, y))

    distances = []
    i = 0
    while len(galaxies) > 1:
        current = galaxies.pop()
        i += 1
        for j, other in enumerate(galaxies):
            distances.append(
                ((i, i + j + 1), (current, other), manhatten_distance(current, other))
            )

    return sum(d[2] for d in distances)


print("part 1:", solve(lines, False))  # 9312968
print("part 2:", solve(lines, True))  # 597714117556
