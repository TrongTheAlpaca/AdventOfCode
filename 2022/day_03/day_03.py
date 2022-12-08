# PREAMBLE
def half(l: str):
    half_idx = len(l) // 2
    return set(l[:half_idx]), set(l[half_idx:])


def chunks(lst: list, n: int) -> set:
    """Yield successive n-sized sets from lst, extended on https://stackoverflow.com/a/312464)"""
    for i in range(0, len(lst), n):
        yield map(set, lst[i : i + n])


def priority(item: str):
    value = ord(item)
    return value - ord("a") + 1 if value > ord("Z") else value - ord("A") + 27


with open("input.txt") as f:
    lines = f.read().splitlines()

# PART 1
part_1 = sum(priority((left & right).pop()) for left, right in map(half, lines))
print(part_1)  # 7967 CORRECT

# PART 2
part_2 = sum(priority(set.intersection(*chunk).pop()) for chunk in chunks(lines, 3))
print(part_2)  # 2716 CORRECT
