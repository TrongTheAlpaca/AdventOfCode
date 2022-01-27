# PREAMBLE
with open("input") as f:
    cases = [line.split(' | ') for line in f.read().split('\n')]
    cases = [[[set(x) for x in case[0].split(' ')], [set(x) for x in case[1].split(' ')]] for case in cases]


def pop_digit_by_length(_hints: list, length: int) -> set[int]:
    return _hints.pop(_hints.index(next(filter(lambda x: len(x) == length, _hints))))


def pop_digit_by_subtraction(_hints: list, length: int, digit: set[int]) -> set[int]:
    return _hints.pop(_hints.index(next(filter(lambda x: len(x - digit) == length, _hints))))


total_uniques = 0
total_all = 0
for hints, display in cases:

    digits: list[set[int]] = [set()] * 10

    digits[1] = pop_digit_by_length(hints, 2)
    digits[7] = pop_digit_by_length(hints, 3)
    digits[4] = pop_digit_by_length(hints, 4)
    digits[8] = pop_digit_by_length(hints, 7)
    digits[6] = pop_digit_by_subtraction(hints, 5, digits[1])
    digits[3] = pop_digit_by_subtraction(hints, 2, digits[7])
    digits[0] = pop_digit_by_subtraction(hints, 2, digits[3])
    digits[5] = pop_digit_by_subtraction(hints, 0, digits[6])
    digits[2], digits[9] = hints if len(hints[0]) < len(hints[1]) else reversed(hints)

    total_uniques += sum(display.count(digits[n]) for n in [1, 4, 7, 8])
    total_all += int(''.join([str(digits.index(d)) for d in display]))

print(total_uniques)  # Part 1:    261 is Correct
print(total_all)      # Part 2: 987553 is Correct
