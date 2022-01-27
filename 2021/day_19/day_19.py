# PREAMBLE
def calc_distance(start: tuple, end: tuple):
    x1, y1, z1 = start
    x2, y2, z2 = end
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def calc_offset(src_coord: tuple, des_coord: tuple) -> tuple:
    return (
        des_coord[0] - src_coord[0],
        des_coord[1] - src_coord[1],
        des_coord[2] - src_coord[2]
    )


def point_rotate(coord: tuple, x_axis, y_axis, z_axis) -> tuple:
    assert 0 <= x_axis < 4 and 0 <= y_axis < 4 and 0 <= z_axis < 4

    mutable = list(coord)
    for _ in range(z_axis):
        mutable[0], mutable[1] = mutable[1], -mutable[0]
    for _ in range(x_axis):
        mutable[2], mutable[1] = mutable[1], -mutable[2]
    for _ in range(y_axis):
        mutable[0], mutable[2] = mutable[2], -mutable[0]

    return tuple(mutable)


class Scanner:
    def __init__(self, beacon_coordinates: list[tuple[int]]):
        self.beacon_coordinates = beacon_coordinates
        self.x = 0
        self.y = 0
        self.z = 0
        self.calibrated = False

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
        self.beacon_coordinates = [(a + x, b + y, c + z) for (a, b, c) in self.beacon_coordinates]

    def rotate(self, x_axis, y_axis, z_axis):
        assert 0 <= x_axis < 4 and 0 <= y_axis < 4 and 0 <= z_axis < 4
        self.x, self.y, self.z = point_rotate((self.x, self.y, self.z), x_axis, y_axis, z_axis)
        self.beacon_coordinates = [point_rotate(coord, x_axis, y_axis, z_axis) for coord in self.beacon_coordinates]

    def calibrate(self, other):
        assert isinstance(other, Scanner)

        s1_distances = []
        for src in self.beacon_coordinates:
            s1_distances.append((src, set([calc_distance(src, des) for des in self.beacon_coordinates if src != des])))

        s2_distances = []
        for src in other.beacon_coordinates:
            s2_distances.append((src, set([calc_distance(src, des) for des in other.beacon_coordinates if src != des])))

        s1_relevant_points = []
        s2_relevant_points = []
        for i, d1 in s1_distances:
            for j, d2 in s2_distances:
                if len(d1.intersection(d2)) > 1:
                    s1_relevant_points.append(i)
                    s2_relevant_points.append(j)

        if len(s2_relevant_points) < 2:
            return False

        for (x_rot, y_rot, z_rot) in [(x_rot, y_rot, z_rot) for x_rot in range(4) for y_rot in range(4) for z_rot in range(4)]:
            rotated_points = tuple([point_rotate(d, x_rot, y_rot, z_rot) for d in s2_relevant_points])
            offsets = [calc_offset(rotated_points[i], s1_relevant_points[i]) for i in range(len(s2_relevant_points))]

            if len(set(offsets)) == 1:  # Perfect alignment with offset
                other.rotate(x_rot, y_rot, z_rot)
                other.move(*offsets[0])
                return True

        return False


def read_scanners(file: str):
    with open(file) as f:
        scanners = [[tuple(map(int, y.split(',')[:3])) for y in x.split('\n')[1:]] for x in f.read().split('\n\n')]
        return [Scanner(s) for s in scanners]


if __name__ == '__main__':

    scanners = read_scanners("input")

    print("Number of scanners:", len(scanners))

    # Run two times to calibrate all
    while not all([s.calibrated for s in scanners]):
        scanners[0].calibrated = True
        for s1 in scanners:
            if s1.calibrated:
                for s2 in scanners[1:]:
                    if s1 != s2 and not s2.calibrated:
                        s2.calibrated = s1.calibrate(s2)

    unique_beacons = set()
    for i, s in enumerate(scanners):
        print(f"S_{i}", s.x, s.y, s.z)
        unique_beacons.update(s.beacon_coordinates)

    print("Number of Unique Beacons:", len(unique_beacons))  # PART 1: 320

    longest_manhattan = 0
    for s1 in scanners:
        for s2 in scanners:
            if s1 != s2:
                distance = abs(s2.x - s1.x) + abs(s2.y - s1.y) + abs(s2.z - s1.z)
                if distance > longest_manhattan:
                    longest_manhattan = distance

    print("Longest Manhattan distance:", longest_manhattan)  # PART 2: 9655
