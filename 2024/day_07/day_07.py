from itertools import product
from tqdm import tqdm

with open("input.txt", "r") as f:
    rows = [r.split(": ") for r in f.read().splitlines()]
    rows = [(int(x), list(map(int, y.split()))) for x, y in rows]

for part_i, symbols in enumerate((["+", "*"], ["+", "*", "||"])):

    result = 0
    for x, (expected, numbers) in tqdm(enumerate(rows), total=len(rows), leave=False):
        for perm in product(symbols, repeat=len(numbers) - 1):
            current_sum = numbers[0]
            perm_idx = 0
            for number in numbers[1:]:
                if perm[perm_idx] == "+":
                    current_sum += number
                elif perm[perm_idx] == "*":
                    current_sum *= number
                else:
                    current_sum = int(str(current_sum) + str(number))

                perm_idx += 1

                if current_sum > expected:
                    break

            if current_sum == expected:
                result += expected
                break

    print(f"Part {part_i + 1}:", result)
# PART 1: 14711933466277
# PART 2: 286580387663654
