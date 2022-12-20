with open("input.txt") as f:
    cubes = set(tuple(map(int, l.split(","))) for l in f.read().splitlines())

adjacent_non_cubes = set()
cubes_adjacents = dict()
for cube in cubes:
    cubes_adjacents[cube] = set()

for (x, y, z) in cubes:
    neighbors = set(
        [
            (x + 1, y + 0, z + 0),
            (x - 1, y + 0, z + 0),
            (x + 0, y + 1, z + 0),
            (x + 0, y - 1, z + 0),
            (x + 0, y + 0, z + 1),
            (x + 0, y + 0, z - 1),
        ]
    )

    cubes_adjacents[(x, y, z)] = cubes & neighbors
    adjacent_non_cubes |= neighbors - cubes

n_exposed = 0
for cube, adjacents in cubes_adjacents.items():
    print(f"cube: {cube} => {6 - len(adjacents)} ({adjacents})")
    n_exposed += 6 - len(adjacents)

print("PART 1:", n_exposed)  # 3522

# PART 2
def get_water():

    queue = [(0, 0, 0)]
    water = {(0, 0, 0)}

    while queue:

        (x, y, z) = queue.pop(0)

        if x < -5 or y < -5 or z < -5:
            continue

        if x > 25 or y > 25 or z > 25:
            continue

        neighbors = set(
            [
                (x + 1, y + 0, z + 0),
                (x - 1, y + 0, z + 0),
                (x + 0, y + 1, z + 0),
                (x + 0, y - 1, z + 0),
                (x + 0, y + 0, z + 1),
                (x + 0, y + 0, z - 1),
            ]
        )

        for n in neighbors:
            if n not in water:
                if n not in cubes:
                    queue.append(n)
                    water.add(n)
    return water


water = get_water()

cubes_adjacents = dict()
for cube in cubes:
    cubes_adjacents[cube] = set()

for (x, y, z) in cubes:
    neighbors = set(
        [
            (x + 1, y + 0, z + 0),
            (x - 1, y + 0, z + 0),
            (x + 0, y + 1, z + 0),
            (x + 0, y - 1, z + 0),
            (x + 0, y + 0, z + 1),
            (x + 0, y + 0, z - 1),
        ]
    )

    cubes_adjacents[(x, y, z)] = neighbors & water

n_exposed = 0
for cube, adjacents in cubes_adjacents.items():
    print(f"cube: {cube} => {len(adjacents)} ({adjacents})")
    n_exposed += len(adjacents)
print(n_exposed)

print("PART 2:", n_exposed)  # 2074
