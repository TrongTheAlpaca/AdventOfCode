import math

with open('test/test_1.txt') as f:
    jolts = [int(x) for x in f.read().splitlines()]

jolts.append(max(jolts)+3)  # Our device's built-in adapter


def get_valid_adapters(cur_joltage, cur_jolts):
    valid_adapters = [cur_joltage + 1 <= x <= cur_joltage + 3 for x in cur_jolts]

    if not any(valid_adapters):
        print('WRONG SEQUENCE')
        return None

    return [i for i, x in enumerate(valid_adapters) if x]


current_joltage = 0
current_jolts = jolts.copy()
chain = []
n_diff_1 = 0
n_diff_3 = 0
count = 0
while len(current_jolts) > 0:
    valid_indices = get_valid_adapters(current_joltage, current_jolts)
    valid_adapters = [current_jolts[i] for i in valid_indices]
    selected_adapter = min(valid_adapters)
    chain.append(selected_adapter)

    diff = selected_adapter - current_joltage
    if diff == 1:
        n_diff_1 += 1
    else:
        if n_diff_1 > 1:
            count += math.factorial(n_diff_1)
        n_diff_1 = 0

    current_joltage = selected_adapter
    current_jolts.remove(selected_adapter)

print('Part 1:', count)
