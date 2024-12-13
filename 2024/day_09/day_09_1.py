with open("input.txt", "r") as f:
    string = f.read()

file_blocks = []
is_file = True
file_idx = 0
str_idx = 0
while str_idx < len(string):
    val = int(string[str_idx])
    if is_file:
        for i in range(val):
            file_blocks.append(file_idx)
        file_idx += 1
        is_file = False
    else:
        for i in range(val):
            file_blocks.append(None)
        is_file = True
    str_idx += 1

print(file_blocks)

part_1 = 0
cur_idx = 0
while cur_idx < len(file_blocks):
    block = file_blocks[cur_idx]
    if block is None:
        last_entry = None
        while not last_entry:
            last_entry = file_blocks.pop()
        file_blocks[cur_idx] = last_entry
        block = file_blocks[cur_idx]

    part_1 += cur_idx * block
    cur_idx += 1

print(file_blocks)
print("Part 1:", part_1)  # Part 1: 6435922584968
