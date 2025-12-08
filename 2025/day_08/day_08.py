import math


def calc_distance(point_a, point_b):
    x = (point_a[0] - point_b[0]) ** 2
    y = (point_a[1] - point_b[1]) ** 2
    z = (point_a[2] - point_b[2]) ** 2

    return math.sqrt(x + y + z)


with open("input.txt", "r") as f:
    boxes = [tuple(map(int, row.split(","))) for row in f.read().splitlines()]

N_PAIRINGS = 1000 if f.name == "input.txt" else 10

connection_order = []
for idx_a, a in enumerate(boxes):
    for idx_b, b in enumerate(boxes[idx_a + 1 :], start=idx_a + 1):
        connection_order.append((calc_distance(a, b), idx_a, idx_b))
connection_order.sort()

circuits = [frozenset({idx}) for idx in range(len(boxes))]
for idx, connection in enumerate(connection_order):
    _, box_a, box_b = connection

    if circuits[box_a] != circuits[box_b]:
        new_circuit = circuits[box_a] | circuits[box_b]
        for k in new_circuit:
            circuits[k] = new_circuit

        if len(new_circuit) == len(boxes):
            part_2 = boxes[box_a][0] * boxes[box_b][0]
            break

    if idx == N_PAIRINGS:
        s = sorted(set(circuits), key=len, reverse=True)
        part_1 = len(s[0]) * len(s[1]) * len(s[2])

print("Part 1:", part_1)
print("Part 2:", part_2)

if f.name == "input.txt":
    assert part_1 == 122636
    assert part_2 == 9271575747
elif f.name == "test_0.txt":
    assert part_1 == 40
    assert part_2 == 25272
