with open("input.txt", "r") as f:
    parts = f.read().strip().split(",")


def calc_hash(string) -> int:
    current_hash = 0
    for char in string:
        current_hash += ord(char)
        current_hash *= 17
        current_hash %= 256
    return current_hash


total_hash_value = 0
for part in parts:
    total_hash_value += calc_hash(part)

print("Part 1:", total_hash_value)  # 513214


label_locator = {}

boxes = [[] for _ in range(256)]

total_hash_value = 0
for part in parts:
    if "-" in part:
        lens = part.removesuffix("-")
        label = calc_hash(lens)
        box_exists = False
        for i, old_lens in enumerate(boxes[label]):
            if old_lens[0] == lens:
                box_exists = True
                break

        if box_exists:
            del boxes[label][i]
    else:
        lens, focal = part.split("=")
        focal = int(focal)
        label = calc_hash(lens)

        box_exists = False
        for i, old_lens in enumerate(boxes[label]):
            if old_lens[0] == lens:
                box_exists = True
                break

        if box_exists:
            boxes[label][i] = (lens, focal)
        else:
            boxes[label].append((lens, focal))


total_focal_length = 0
for box_idx, box in enumerate(boxes):
    if len(box) > 0:
        for i, part in enumerate(box):
            current_focal_length = (box_idx + 1) * (i + 1) * part[1]
            total_focal_length += current_focal_length

print("Part 2:", total_focal_length)  # 258826
