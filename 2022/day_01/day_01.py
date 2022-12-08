# PREAMBLE
with open("input.txt") as f:
    calories = [list(map(int, elf.split("\n"))) for elf in f.read().split("\n\n")]

calorie_sums = sorted([sum(elf) for elf in calories])

# PART 1
print(max(calorie_sums))

# PART 2
print(sum(calorie_sums[-3:]))
