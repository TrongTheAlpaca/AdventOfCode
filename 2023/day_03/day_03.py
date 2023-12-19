with open("input.txt") as f:
    lines = f.read().splitlines()

MAX_HEIGHT = len(lines) - 1
MAX_WIDTH = len(lines[0]) - 1
is_within_boundaries = lambda c: 0 < c[1] < MAX_HEIGHT and 0 < c[0] < MAX_WIDTH

valid_part_numbers = []

# fmt: off
AoE = [
    (-1, -1), (+0,-1), (+1,-1),
    (-1, +0),          (+1,+0),
    (-1, +1), (+0,+1), (+1,+1),
]
# fmt: on


class Number:
    """
    Used to ensure uniqueness (via reference) between numbers despite sharing having equal values.
    """

    def __init__(self, value: int):
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


unique_numbers: dict[Number] = dict()

# Part 1 and Part 2: Fetch all Part Numbers
for y, row in enumerate(lines):
    coords: list[tuple[int]] = []
    for x, cell in enumerate(row + "."):  # offset to include numbers at the end of rows
        if cell.isdigit():
            coords.append((x, y))
        else:
            if coords:
                value = int("".join([lines[y][x] for x, y in coords]))
                unique_number = Number(value)
                is_part_number = False
                for coord in coords:
                    # Part 2
                    unique_numbers[coord] = unique_number

                    # Part 1
                    for dx, dy in AoE:
                        _x = coord[0] + dx
                        _y = coord[1] + dy
                        if (
                            is_within_boundaries((_x, _y))
                            and lines[_y][_x] != "."
                            and not lines[_y][_x].isdigit()
                        ):
                            is_part_number = True
                            break

                # Part 1
                if is_part_number:
                    valid_part_numbers.append(value)

            coords.clear()

# Part 2: Calculate total gear product
total_gear_product = 0
for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        if lines[y][x] == "*":  # Check if current cell is a Gear
            adjacent = set()
            for dx, dy in AoE:
                current_cell = (x + dx, y + dy)
                if (
                    is_within_boundaries(current_cell)
                    and current_cell in unique_numbers
                ):
                    adjacent.add(unique_numbers[current_cell])

            if len(adjacent) == 2:
                total_gear_product += adjacent.pop().value * adjacent.pop().value

print("part 1:", sum(valid_part_numbers))  # 532331
print("part 2:", total_gear_product)  # 82301120
