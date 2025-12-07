with open("input.txt", "r") as f:
    id_ranges = [tuple(map(int, part.split("-"))) for part in f.read().split(",")]

part_1 = 0
part_2 = 0

for range_start, range_end in id_ranges:
    for current in range(range_start, range_end + 1):
        s = str(current)
        length = len(s)

        for n in range((length // 2), 0, -1):
            if len(set([s[i : i + n] for i in range(0, len(s), n)])) == 1:
                if length % 2 == 0 and n == (length // 2):
                    part_1 += current
                part_2 += current
                break

print("Part 1:", part_1)  # 28846518423
print("Part 2:", part_2)  # 31578210022
