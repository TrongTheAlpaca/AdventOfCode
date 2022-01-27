def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        lines = [tuple(line.split(' ')) for line in f.read().split('\n')]
        lines = [([line[0], tuple([tuple(map(int, q[2:].split('..'))) for q in line[1].split(',')])]) for line in lines]

    return lines


def volume(cubic: tuple[tuple[int, int]]) -> int:
    vol = 1
    for dim in range(3):
        vol *= cubic[dim][1] + 1 - cubic[dim][0]
    return vol


def collision(src: tuple, des: tuple):
    x, y, z = src
    _x, _y, _z = des
    if _x[1] < x[0] or _x[0] > x[1]:
        return False
    if _y[1] < y[0] or _y[0] > y[1]:
        return False
    if _z[1] < z[0] or _z[0] > z[1]:
        return False

    return True


def calc_3d_intersection(source: tuple, comparing: tuple) -> tuple[tuple[int, int]]:
    vol: list[tuple[int, int]] = []
    for dim in range(3):
        com = comparing[dim]
        src = source[dim]
        if com[0] <= src[0] and com[1] <= src[1]:  # <=|
            vol.append((src[0], com[1]))
        elif src[0] <= com[0] and com[1] <= src[1]:  # |==|
            vol.append((com[0], com[1]))
        elif src[0] <= com[0] and src[1] <= com[1]:  # |=>
            vol.append((com[0], src[1]))
        else:  # <=>
            vol.append((src[0], src[1]))

    return tuple(vol)


def inclusion_exclusion(src_cuboid, des_cuboids: list[tuple[tuple[int, int]]], inclusion=False) -> int:
    total_volume = 0
    intersections = []
    for des_cuboid in des_cuboids:
        if collision(src_cuboid, des_cuboid):
            intersect_cuboid = calc_3d_intersection(src_cuboid, des_cuboid)
            intersections.append(intersect_cuboid)
            total_volume += volume(intersect_cuboid) if inclusion else -volume(intersect_cuboid)

    for idx, intersection in enumerate(intersections):
        total_volume += inclusion_exclusion(intersection, intersections[idx + 1:], not inclusion)

    return total_volume


def calc_on_cuboids(cuboids: list, part_1) -> int:

    if part_1:
        cuboids = list(filter(lambda x: all([-50 <= t[0] <= 50 and -50 <= t[1] <= 50 for t in x[1]]), cuboids))

    visited = []  # Cuboid/volume that has been noted
    total_volume = 0
    for status, cuboid in reversed(cuboids):
        if status == 'on':
            total_volume += volume(cuboid) + inclusion_exclusion(cuboid, visited)

        visited.append(cuboid)

    return total_volume


if __name__ == '__main__':
    cuboid_input = read_input("input")
    print("Part 1:", calc_on_cuboids(cuboid_input, True))   # PART 1: 609563
    print("Part 2:", calc_on_cuboids(cuboid_input, False))  # PART 2: 1234650223944734
