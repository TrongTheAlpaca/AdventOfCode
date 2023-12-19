with open("input.txt") as f:
    lines = f.read().splitlines()

possible_ids_sum = 0
total_power = 0

for idx, line in enumerate(lines):
    counts = {"red": 0, "green": 0, "blue": 0}

    rounds = line.split(": ")[1].split("; ")
    for round in rounds:
        hands = round.split(", ")

        for hand in hands:
            x, y = hand.split(" ")
            counts[y] = max(int(x), counts[y])

    # Part 1
    if counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14:
        possible_ids_sum += idx + 1

    # Part 2
    total_power += counts["red"] * counts["green"] * counts["blue"]


print("part 1:", possible_ids_sum)
print("part 2:", total_power)
