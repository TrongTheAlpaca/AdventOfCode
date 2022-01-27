# PREAMBLE
with open("input") as f:
    fishes = [int(n) for n in f.read().split(',')]


def count_fish(_fishes, days):

    fish_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in _fishes:
        fish_counts[fish] += 1

    for _ in range(days):
        children = fish_counts.pop(0)
        fish_counts.append(children)
        fish_counts[6] += children

    return sum(fish_counts)


print(count_fish(fishes, 80))   # PART 1:        379114 is Correct!
print(count_fish(fishes, 256))  # PART 2: 1702631502303 is Correct!
