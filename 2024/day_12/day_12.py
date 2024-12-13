from collections import defaultdict

with open("input.txt", "r") as f:
    rows = f.read().splitlines()

MAX_X = len(rows[0])
MAX_Y = len(rows)

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

farms = defaultdict(list)
visited = set()
for y, row in enumerate(rows):
    for x, cell in enumerate(row):

        if (x, y) in visited:
            continue

        queue = [(x, y)]
        current_visited = {(x, y)}
        while queue:
            current = queue.pop()
            farm_code_1 = rows[current[1]][current[0]]
            for dx, dy in [LEFT, UP, RIGHT, DOWN]:
                next_pos = current[0] + dx, current[1] + dy
                x2, y2 = next_pos
                if 0 <= x2 < MAX_X and 0 <= y2 < MAX_Y:
                    farm_code_2 = rows[y2][x2]
                    if next_pos not in current_visited and farm_code_1 == farm_code_2:
                        queue.append(next_pos)
                        current_visited.add(next_pos)

        visited |= current_visited
        farms[cell].append(current_visited)


part_1 = 0
part_2 = 0
for farm_type, regions in farms.items():
    # print(farm_type, regions)
    for region in regions:
        unique_walls = set()
        for x, y in region:
            walls = set(
                (x + dx, y + dy)
                for dx, dy in [(0.5, 0), (-0.5, 0), (0, 0.5), (0, -0.5)]
            )
            unique_walls.symmetric_difference_update(walls)

        area = len(region)

        # Part 1
        perimenter = len(unique_walls)
        # print("area:", area)
        # print("perimeter:", perimenter)
        part_1 += perimenter * area

        # Part 2
        n_sides = 0
        while unique_walls:
            (x, y) = unique_walls.pop()
            # Find if wall is horizontal or vertical
            if (x + 0.5, y) in region or (x - 0.5, y) in region:
                # wall is vertical
                inside_is_east = (x + 0.5, y) in region
                current_n_walls = len(unique_walls)
                y2 = 1
                while True:
                    if inside_is_east and (x + 0.5, y + y2) not in region:
                        break
                    if not inside_is_east and (x - 0.5, y + y2) not in region:
                        break
                    unique_walls.discard((x, y + y2))
                    if current_n_walls > len(unique_walls):
                        current_n_walls = len(unique_walls)
                        y2 += 1
                    else:
                        break

                current_n_walls = len(unique_walls)
                y2 = 1
                while True:
                    if inside_is_east and (x + 0.5, y - y2) not in region:
                        break
                    if not inside_is_east and (x - 0.5, y - y2) not in region:
                        break
                    unique_walls.discard((x, y - y2))
                    if current_n_walls > len(unique_walls):
                        current_n_walls = len(unique_walls)
                        y2 += 1
                    else:
                        break
            else:
                # wall is horizontal
                inside_is_south = (x, y + 0.5) in region
                current_n_walls = len(unique_walls)
                x2 = 1
                while True:
                    if inside_is_south and (x + x2, y + 0.5) not in region:
                        break
                    if not inside_is_south and (x + x2, y - 0.5) not in region:
                        break
                    unique_walls.discard((x + x2, y))
                    if current_n_walls > len(unique_walls):
                        current_n_walls = len(unique_walls)
                        x2 += 1
                    else:
                        break

                current_n_walls = len(unique_walls)
                x2 = 1
                while True:
                    if inside_is_south and (x - x2, y + 0.5) not in region:
                        break
                    if not inside_is_south and (x - x2, y - 0.5) not in region:
                        break
                    unique_walls.discard((x - x2, y))
                    if current_n_walls > len(unique_walls):
                        current_n_walls = len(unique_walls)
                        x2 += 1
                    else:
                        break

            n_sides += 1

        print(f"{farm_type}: {area} * {n_sides} = {area * n_sides}")
        part_2 += area * n_sides


print("Part 1:", part_1)  # Part 1: 1477762
print("Part 2:", part_2)  # Part 2: 923480
