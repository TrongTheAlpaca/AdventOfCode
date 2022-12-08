import math

with open('test/test_1.txt') as f:
    jolts = [int(x) for x in f.read().splitlines()]

# print(jolts)
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
count = 0
# while len(current_jolts) > 0 or max(current_jolts) < current_joltage:
while len(current_jolts) > 0:
    valid_indices = get_valid_adapters(current_joltage, current_jolts)

    if not valid_indices:
        # No more valid adapters exist
        break
    elif len(valid_indices) > 1:
        count += math.factorial(len(valid_indices))

    valid_adapters = [current_jolts[i] for i in valid_indices]
    selected_adapter = min(valid_adapters)
    chain.append(selected_adapter)
    current_joltage = selected_adapter
    current_jolts.remove(selected_adapter)

print(chain)
print('Part 2:', count)  # Part 1: 1920

