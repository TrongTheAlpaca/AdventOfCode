def transform_tuple(
    original_tuple: tuple[int], from_idx: int, to_idx: int
) -> tuple[int]:
    # original_tuple = (1, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0)

    # Convert tuple to list
    lst = list(original_tuple)

    # Remove 3 and insert it at the new position
    lst[to_idx], lst[from_idx] = lst[from_idx], lst[to_idx]

    # Convert list back to tuple
    return tuple(lst)


a = [1, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0]


permutations = {tuple(a)}


def recurse_permutate(current: tuple):
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
        current = transform_tuple(current, idx, idx + 1)
        permutations.add(current)
        recurse_permutate(current)


def get_permutations(case: tuple[int]) -> list[tuple[int]]:
    return list(sorted(list(recurse_permutate(case)), reverse=True))


sorty = list(sorted(list(permutations), reverse=True))
print()
# def begin_recursion(current_permutation: list):
#     # if current_permutation[-1] != 0:
#     #     return

#     number_idx = [i for i, n in enumerate(current_permutation) if n != 0]
#     for n in number_idx:
#         if (n < len(current_permutation) - 1 and current_permutation[n + 1] == 0) and (
#             n + 2 < len(current_permutation) - 1 or current_permutation[n + 2] == 0
#         ):
#             # check if current number can move rightwise
#             righty_until_tighty(current_permutation.copy(), n)
#             begin_recursion(current_permutation.copy())

#     current_permutation.pop()
#     current_permutation.insert(0, 0)
#     begin_recursion(current_permutation.copy())


# def righty_until_tighty(current_permutation: list, current_idx):
#     while current_permutation[-1] == 0:
#         current_permutation[current_idx + 1] = current_permutation[current_idx]
#         current_permutation[current_idx] = 0
#         permutations.append(tuple(current_permutation))
#         current_idx += 1


# begin_recursion(a)
