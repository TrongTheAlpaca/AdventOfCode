with open("input.txt", "r") as f:
    rows = f.read().splitlines()

part_1 = 0
for x, row in enumerate(rows):
    expected, numbers = row.split(": ")
    expected = int(expected)
    numbers = list(map(int, numbers.split()))

    for i in range(2 ** (len(numbers) - 1)):
        current_sum = numbers[0]
        for number in numbers[1:]:
            if i & 1 == 1:
                current_sum += number
            else:
                current_sum *= number

            i >>= 1

            if current_sum > expected:
                break

        if current_sum == expected:
            # print("GOOD:", expected, numbers)
            part_1 += expected
            break

print("Part 1:", part_1)  # 14711933466277
