import re
from fractions import Fraction

with open("input.txt", "r") as f:
    claw_machines = f.read().split("\n\n")

for part in range(1, 3):
    total_cost = 0
    for idx, claw_machine in enumerate(claw_machines):
        numbers = tuple(map(int, re.findall(r"(\d+)", claw_machine)))
        button_a, button_b, prize = numbers[0:2], numbers[2:4], numbers[4:6]

        if part == 2:
            prize = (prize[0] + 10_000_000_000_000, prize[1] + 10_000_000_000_000)

        # Gauss-Jordan elimination
        matrix = [
            [button_a[0], button_b[0], prize[0]],
            [button_a[1], button_b[1], prize[1]],
        ]

        # [1, *, *]
        # [*, *, *]
        matrix[0] = [
            1,
            button_b[0] * Fraction(1, matrix[0][0]),
            prize[0] * Fraction(1, matrix[0][0]),
        ]

        # [1, *, *]
        # [0, *, *]
        matrix[1] = [
            0,
            button_b[1] - (matrix[0][1] * matrix[1][0]),
            prize[1] - (matrix[0][2] * matrix[1][0]),
        ]

        # [1, *, *]
        # [0, 1, B]
        matrix[1] = [0, 1, matrix[1][2] / matrix[1][1]]

        # [1, 0, A]
        # [0, 1, B]
        matrix[0] = [1, 0, matrix[0][2] - (matrix[1][2] * matrix[0][1])]

        n_pressed_a = matrix[0][2]
        n_pressed_b = matrix[1][2]
        if n_pressed_a.is_integer() and n_pressed_b.is_integer():
            total_cost += n_pressed_a * 3 + n_pressed_b

    print(f"Part {part}:", total_cost)

# Part 1: 39290
# Part 2: 73458657399094
