# Regex is very smooth to use here, but let's try without!

with open("input.txt") as f:
    lines = f.read().splitlines()

numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def solve(is_part_2: bool):
    total = 0
    for line in lines:
        left = None
        for c in range(len(line)):
            if line[c].isdigit():
                left = line[c]
            elif is_part_2:
                for i, n in enumerate(numbers):
                    if line[c:].startswith(n):
                        left = str(i + 1)
                        break

            if left:
                break

        right = None
        for c in range(len(line) - 1, -1, -1):
            if line[c].isdigit():
                right = line[c]
            elif is_part_2:
                for i, n in enumerate(numbers):
                    if line[: c + 1].endswith(n):
                        right = str(i + 1)
                        break

            if right:
                break

        total += int(left + right)

    return total


print("part 1:", solve(is_part_2=False))
print("part 2:", solve(is_part_2=True))
