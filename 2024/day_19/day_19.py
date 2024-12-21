from collections import defaultdict
from tqdm import tqdm
from queue import PriorityQueue

with open("input.txt", "r") as f:
    t, p = f.read().split("\n\n")
    towels = t.split(", ")
    patterns = p.splitlines()

n_valid = 0
total_combinations = 0
for i, pattern in enumerate(tqdm(patterns)):
    pqueue = PriorityQueue()
    pqueue.put((0, pattern))
    counts = defaultdict(lambda: 0)
    counts[pattern] = 1
    is_good = False
    while not pqueue.empty():

        _, current_pattern = pqueue.get()

        if current_pattern == "":
            n_valid += 1
            is_good = True
            break

        for towel in towels:
            if current_pattern.startswith(towel):
                result = current_pattern.removeprefix(towel)
                if result not in counts:
                    pqueue.put((len(pattern) - len(result), result))

                counts[result] += counts[current_pattern]

    if is_good:
        total_combinations += counts[""]

print("Part 1:", n_valid)  # Part 1: 278
print("Part 2:", total_combinations)  # Part 2: 569808947758890
