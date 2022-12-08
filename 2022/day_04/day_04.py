# PREAMBLE
with open("input.txt") as f:
    pairs: list[tuple[int, int, int, int]] = [
        tuple(map(int, line.replace("-", ",").split(",")))
        for line in f.read().splitlines()
    ]

# PART 1
tot_overlap = 0
for p1_x, p1_y, p2_x, p2_y in pairs:
    if (p1_x <= p2_x and p2_y <= p1_y) or (p2_x <= p1_x and p1_y <= p2_y):
        tot_overlap += 1

print("PART 1:", tot_overlap)  # 540 Correct

# PART 2
tot_overlap = 0
for p1_x, p1_y, p2_x, p2_y in pairs:
    if (p2_x <= p1_y <= p2_y) or (p1_x <= p2_y <= p1_y):
        tot_overlap += 1

print("PART 2:", tot_overlap)  # 872 Correct
