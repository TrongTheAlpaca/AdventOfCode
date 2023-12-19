with open("input.txt") as f:
    histories = [list(map(int, l.split())) for l in f.read().splitlines()]

PART_1, PART_2 = 0, 1

diff_sum = [0, 0]
for history in histories:
    sequences = [history]
    current_sequence = history
    while any(current_sequence):
        diffs = []
        for i in range(len(current_sequence) - 1):
            diff = current_sequence[i + 1] - current_sequence[i]
            diffs.append(diff)

        sequences.append(diffs)
        current_sequence = diffs

    current_diff = [0, 0]  # Part 1 and Part 2
    for seq in reversed(sequences):
        current_diff[PART_1] = seq[-1] + current_diff[PART_1]
        current_diff[PART_2] = seq[0] - current_diff[PART_2]

    diff_sum[PART_1] += current_diff[PART_1]
    diff_sum[PART_2] += current_diff[PART_2]

print("part 1:", diff_sum[0])  # 1834108701
print("part 2:", diff_sum[1])  # 993
