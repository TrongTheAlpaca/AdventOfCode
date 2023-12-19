with open("input.txt") as f:
    lines = [l.split(": ")[1].split(" | ") for l in f.read().splitlines()]

scratchcards_counts = [1] * len(lines)

total_rewards = 0
for idx, (left, right) in enumerate(lines):
    winning, drawn = set(map(int, left.split())), set(map(int, right.split()))
    n_hits = len(winning.intersection(drawn))

    # Part 1
    reward = 0 if n_hits == 0 else 2 ** (n_hits - 1)
    total_rewards += reward

    # Part 2
    for i in range(idx + 1, idx + 1 + n_hits):
        scratchcards_counts[i] += scratchcards_counts[idx]


print("part 1:", total_rewards)  # 24733
print("part 2:", sum(scratchcards_counts))  # 5422730
