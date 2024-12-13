from tqdm import trange
from collections import Counter

with open("input.txt", "r") as f:
    stones = list(map(int, f.read().split()))

stone_counts = [0]
next_queue = Counter()
queue = Counter(stones)
for blink in trange(1000):
    for current_stone, count in queue.items():
        if current_stone == 0:
            next_queue[current_stone + 1] += count
        elif current_stone == 1:
            next_queue[2024] += count
        else:
            stone_str = str(current_stone)
            if len(stone_str) % 2 == 0:
                half_idx = len(stone_str) // 2
                left, right = int(stone_str[:half_idx]), int(stone_str[half_idx:])
                next_queue[left] += count
                next_queue[right] += count
            else:
                next_queue[current_stone * 2024] += count

    queue = next_queue
    next_queue = Counter()
    stone_counts.append(sum(queue.values()))


print("Part 1:", stone_counts[25])  # Part 1: 218079
print("Part 2:", stone_counts[75])  # Part 2: 259755538429618
