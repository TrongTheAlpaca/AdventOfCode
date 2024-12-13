with open("input.txt", "r") as f:
    rows = f.read().splitlines()


def is_within_boundaries(pos: tuple[int, int]) -> bool:
    return 0 <= pos[0] < len(rows[0]) and 0 <= pos[1] < len(rows)


antennas = dict()
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell != ".":
            if cell not in antennas:
                antennas[cell] = []
            antennas[cell].append((x, y))

antinodes_part = [set(), set()]
for antenna_type, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            antenna_1, antenna_2 = positions[i], positions[j]

            diff = antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1]
            diff_i = (diff[0] * -1), (diff[1] * -1)

            # part 1
            antinode_1 = antenna_2[0] + diff[0], antenna_2[1] + diff[1]
            if is_within_boundaries(antinode_1):
                antinodes_part[0].add(antinode_1)
            antinode_2 = antenna_1[0] + diff_i[0], antenna_1[1] + diff_i[1]
            if is_within_boundaries(antinode_2):
                antinodes_part[0].add(antinode_2)

            # part 2
            current_pos = antenna_1
            while is_within_boundaries(current_pos):
                antinodes_part[1].add(current_pos)
                current_pos = current_pos[0] + diff[0], current_pos[1] + diff[1]
            current_pos = antenna_2
            while is_within_boundaries(current_pos):
                antinodes_part[1].add(current_pos)
                current_pos = current_pos[0] + diff_i[0], current_pos[1] + diff_i[1]


for antinodes in antinodes_part:
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            print("#" if (x, y) in antinodes else cell, end="")
        print()

for part, antinodes in enumerate(antinodes_part):
    print(f"Part {part + 1}:", len(antinodes))  # Part 1: 376, Part 2: 1352
