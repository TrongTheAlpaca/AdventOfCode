def swap_tuple_indices(original: tuple[int], from_idx: int, to_idx: int) -> tuple[int]:
    lst = list(original)
    lst[to_idx], lst[from_idx] = lst[from_idx], lst[to_idx]
    return tuple(lst)


def recurse_permutate(permutations: set, current: tuple):
    if current[-1] != 0:
        return

    number_idx = [i for i, n in enumerate(current) if n != 0]
    for idx in reversed(number_idx):
        if idx == len(current) - 1:
            continue
        if current[idx + 1] != 0:
            continue
        if idx < len(current) - 2 and current[idx + 2] != 0:
            continue
        current = swap_tuple_indices(current, idx, idx + 1)
        permutations.add(current)
        recurse_permutate(permutations, current)


def get_permutations(case: tuple[int]) -> list[tuple[int]]:
    permutations = {case}
    recurse_permutate(permutations, case)
    return list(sorted(list(permutations), reverse=True))


def convert_case_to_binary(case: str):
    binary_uneditable = int("".join(["1" if c == "." else "0" for c in case]), 2)
    binary_unknowns = int("".join(["1" if c == "?" else "0" for c in case]), 2)
    binary_knowns = int("".join(["1" if c == "#" else "0" for c in case]), 2)
    return binary_uneditable, binary_unknowns, binary_knowns


def convert_permutation_to_binary(permutation: tuple[int]):
    result = ""
    for i in permutation:
        if i == 0:
            result += "0"
        else:
            for _ in range(i):
                result += "1"
    return int(result, 2)


def count_continous_ones(number: int):
    counted = []
    count = 0
    while number != 0:
        if number & 1 == 1:
            count += 1
        else:
            if count != 0:
                counted.append(count)
                count = 0
        number >>= 1
    if count != 0:
        counted.append(count)

    return tuple(reversed(counted))


with open("test.txt", "r") as f:
    lines = f.read().splitlines()
    cases = [l.split() for l in lines]
    cases = [(c[0], tuple(map(int, c[1].split(",")))) for c in cases]
    # part 2
    cases_part_2 = []
    for case, numbers in cases:
        x = "?".join(c for c in [case] * 5)
        y = numbers * 5
        cases_part_2.append((x, y))

# PART 1
all_n_possible_permutations = []
for case, numbers in cases:
    length = len(case)
    n_zeros = length - sum(numbers)

    collection = []
    listed = list(numbers)
    while listed or n_zeros:
        if listed:
            collection.append(listed.pop(0))
        if n_zeros:
            collection.append(0)
            n_zeros -= 1

    all_permutations = get_permutations(tuple(collection))

    n_possible_permutations = 0

    # Get binary values
    binary_uneditable, binary_unknowns, binary_knowns = convert_case_to_binary(case)

    for permutation in all_permutations:
        binary_proposal = convert_permutation_to_binary(permutation)

        if binary_uneditable & binary_proposal != 0:
            continue

        magic = (
            binary_unknowns & binary_proposal
        ) | binary_knowns  # Something wrong here!

        n_continous_ones_found = count_continous_ones(magic)

        if n_continous_ones_found == numbers:
            n_possible_permutations += 1

    all_n_possible_permutations.append(n_possible_permutations)

print("part 1:", sum(all_n_possible_permutations))  # 7922


# PART 2
all_n_possible_permutations = []
for line, (case, numbers) in enumerate(cases_part_2):
    print(line)
    print(all_n_possible_permutations)
    length = len(case)
    n_zeros = length - sum(numbers)

    collection = []
    listed = list(numbers)
    while listed or n_zeros:
        if listed:
            collection.append(listed.pop(0))
        if n_zeros:
            collection.append(0)
            n_zeros -= 1

    all_permutations = get_permutations(tuple(collection))

    n_possible_permutations = 0

    # Get binary values
    binary_uneditable, binary_unknowns, binary_knowns = convert_case_to_binary(case)

    for permutation in all_permutations:
        binary_proposal = convert_permutation_to_binary(permutation)

        if binary_uneditable & binary_proposal != 0:
            continue

        magic = (
            binary_unknowns & binary_proposal
        ) | binary_knowns  # Something wrong here!

        n_continous_ones_found = count_continous_ones(magic)

        if n_continous_ones_found == numbers:
            n_possible_permutations += 1

    all_n_possible_permutations.append(n_possible_permutations)

print(all_n_possible_permutations)
print("part 2:", sum(all_n_possible_permutations))  # 7922
