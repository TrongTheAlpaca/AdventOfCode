# PREAMBLE
with open("input") as f:
    lines = [int(x) for x in f.readlines()]

# PART 1
n_increase = 0
prev_value = -1
for i in range(len(lines) - 1):
    prev_value = lines[i]
    next_value = lines[i + 1]
    if prev_value < next_value:
        n_increase += 1

print(n_increase)  # 1759 is correct!


# PART 2
n_increase = 0
prev_value = -1
for i in range(len(lines)):
    prev_value = sum(lines[i:i+3])
    next_value = sum(lines[i+1:i+4])
    if prev_value < next_value:
        n_increase += 1

print(n_increase)  # 1805 is correct!
