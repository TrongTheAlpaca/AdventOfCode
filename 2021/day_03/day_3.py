# PREAMBLE
with open("input") as f:
    lines = [line.rstrip() for line in f.readlines()]

BIT_LENGTH = 12

# PART 1
gamma = ''
epsilon = ''
for position in range(BIT_LENGTH):
    stripped = [line[position] for line in lines]
    n_zeros = stripped.count('0')
    n_ones = len(stripped) - n_zeros
    if n_zeros > n_ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))  # 3009600 is Correct!

# PART 2
oxygen = lines.copy()
co2 = lines.copy()
for position in range(BIT_LENGTH):
    if len(oxygen) > 1:
        stripped = [line[position] for line in oxygen]
        n_zeros = stripped.count('0')
        n_ones = stripped.count('1')

        if n_zeros > n_ones:
            oxygen = [line for line in oxygen if line[position] == '0']
        else:
            oxygen = [line for line in oxygen if line[position] == '1']

    if len(co2) > 1:
        stripped = [line[position] for line in co2]
        n_zeros = stripped.count('0')
        n_ones = stripped.count('1')

        if n_zeros <= n_ones:
            co2 = [line for line in co2 if line[position] == '0']
        else:
            co2 = [line for line in co2 if line[position] == '1']

print(int(oxygen[0], 2) * int(co2[0], 2))  # 6940518 too HIGH!

