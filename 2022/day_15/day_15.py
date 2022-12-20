from collections import defaultdict
from tqdm import trange, tqdm

EXAMPLE, PART_1, PART_2 = 0, 1, 2

MODE = PART_2


options = ["example.txt", "input.txt", "input.txt"]
boundaries = [10, 2_000_000, 2_000_000]

limits = defaultdict(list)  # { Y: [(x1, x2), (x1, x2)]}

sensors = set()
beacons = set()
no_man_sky = set()
detections = set()
with open(options[MODE]) as f:
    for line in f.read().splitlines():
        sx, sy, bx, by = tuple(
            map(
                int,
                (
                    line.removeprefix("Sensor at x=")
                    .replace(": closest beacon is at ", " ")
                    .replace(", y=", " ")
                    .replace(" x=", " ")
                ).split(" "),
            )
        )

        detections.add(((sx, sy), (bx, by)))
        sensors.add((sx, sy))
        beacons.add((bx, by))


def distance(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for sensor, beacon in tqdm(detections):
    d = distance(sensor, beacon)

    x1 = sensor[0] - d - 1
    x2 = sensor[0] + d + 1
    y = sensor[1]
    dy = -1
    while x2 - x1 > 0:
        dy += 1
        x1 += 1
        x2 -= 1

        # if 0 <= y + dy <= boundaries[MODE]:
        limits[y + dy].append((min(x1, x2 + 1), max(x1, x2 + 1)))
        # if 0 <= y - dy <= boundaries[MODE]:
        limits[y - dy].append((min(x1, x2 + 1), max(x1, x2 + 1)))

        if y + dy == boundaries[MODE]:
            for x in range(x1, x2 + 1):
                no_man_sky.add((x, y + dy))

        if y - dy == boundaries[MODE]:
            for x in range(x1, x2 + 1):
                no_man_sky.add((x, y - dy))

# for Y in range(-5, 22):
#     print(f"{Y:>3}", end=" ")
#     for X in range(-5, 25):
#         if (X, Y) in beacons:
#             print("🎇", end="")  # print("🔲", end="")
#         elif (X, Y) in sensors:
#             print("🎆", end="")
#         elif (X, Y) in no_man_sky:
#             print("🔳", end="")
#         else:
#             print("⬛", end="")
#     print()


n_not_beacon = set()
for (x, y) in no_man_sky:
    if y == boundaries[MODE]:
        n_not_beacon.add((x, y))
print("PART 1:", len(n_not_beacon - beacons))  # PART 1: 5508234

bounded = lambda c: (max(0, c[0]), min(c[1], MAX_BOUND))
is_found = False
MAX_BOUND = boundaries[MODE] * 2
for y in trange(0, MAX_BOUND + 1):  # EXAMPLE NUMBERS
    if y in limits:
        current_limits = sorted(limits[y], key=lambda x: x[0], reverse=True)
        a1, a2 = bounded(current_limits.pop())
        while current_limits:
            b1, b2 = bounded(current_limits.pop())
            if a1 <= b1 <= a2:
                a1, a2 = a1, max(a2, b2)
            else:
                print(
                    "PART 2: Distress beacon found: {} -> Tuning frequency: {}".format(
                        (a2, y), (a2 * 4_000_000) + y
                    )
                )  # 10457634860779
                is_found = True
                break

        if is_found:
            break

    if is_found:
        break
