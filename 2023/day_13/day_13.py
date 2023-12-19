with open("input.txt", "r") as f:
    cases = [c.splitlines() for c in f.read().split("\n\n")]


def transpose(array: list[list[str]]):
    return ["".join(t) for t in [*zip(*array)]]


def is_mirrored_on_idx(row: str, index: int):
    left = row[:index]
    right = row[index:][::-1]
    if left.endswith(right) or right.endswith(left):
        return True
    else:
        return False


def flip_cell(_case, x, y):
    cell = _case[y][x]
    new_cell = "#" if cell == "." else "."
    _case[y] = _case[y][:x] + new_cell + _case[y][x + 1 :]
    return _case


def solve(_case, ignore_index: tuple = None):
    length = len(_case[0])
    height = len(_case)
    mirror_index = None
    is_mirrored = False
    for x in range(1, length):
        is_mirrored = True
        for y, row in enumerate(_case):
            if not is_mirrored_on_idx(row, x):
                is_mirrored = False
                break

        if is_mirrored:
            if ignore_index is not None and (True, x) == ignore_index:
                continue
            else:
                mirror_index = x
                break

    if mirror_index is not None:
        return (True, mirror_index)

    case_T = transpose(_case)
    for y in range(1, height):
        is_mirrored = True
        for x, col in enumerate(case_T):
            if not is_mirrored_on_idx(col, y):
                is_mirrored = False
                break

        if is_mirrored:
            if ignore_index is not None and (False, y) == ignore_index:
                continue
            else:
                mirror_index = y
                break

    if mirror_index is not None:
        return (False, mirror_index)

    print("NO MIRROR INDEX FOUND!")
    return (None, 0)


INCLUDE_PART_2 = True

part_1_result = 0
part_2_result = 0

part_1_mirror_indices = []

for case_number, case in enumerate(cases):
    print("case:", case_number)
    result_1 = solve(case)
    is_horizontal, index_part_1 = result_1
    part_1_result += index_part_1 if is_horizontal else index_part_1 * 100

    if not INCLUDE_PART_2:
        continue

    all_permutations = []
    for y, row in enumerate(case):
        for x, col in enumerate(row):
            permutation = case.copy()
            permutation = flip_cell(permutation, x, y)
            all_permutations.append(permutation)

    for permutation in all_permutations:
        result_2 = solve(permutation, ignore_index=result_1)
        is_horizontal_2, index_part_2 = result_2
        if index_part_2 != 0:
            part_2_result += index_part_2 if is_horizontal_2 else index_part_2 * 100
            break

    print()


print("part 1:", part_1_result)  # 33356
print("part 2:", part_2_result)  # 28475
