from tqdm import trange

with open("input.txt", "r") as f:
    string = f.read()

file_blocks = []
is_file = True
file_idx = 0
str_idx = 0
while str_idx < len(string):
    val = int(string[str_idx])
    if is_file:
        file_blocks.append((val, file_idx))
        file_idx += 1
        is_file = False
    else:
        file_blocks.append((val, None))
        is_file = True
    str_idx += 1

for i in trange(len(file_blocks) - 1, 0, -1):

    file_length, file_type = file_blocks[i]
    if file_type == None:
        continue
    for j in range(i):
        cur_file_length, cur_file_type = file_blocks[j]
        if cur_file_type != None:
            continue
        elif cur_file_length < file_length:
            continue
        else:
            diff = cur_file_length - file_length
            file_blocks[i] = (file_length, None)
            file_blocks.pop(j)
            file_blocks.insert(j, (diff, None))
            file_blocks.insert(j, (file_length, file_type))
            break

part_2 = 0
cur_idx = 0
for file_len, file_type in file_blocks:
    if file_type:
        for i in range(file_len):
            part_2 += cur_idx * file_type
            cur_idx += 1
    else:
        cur_idx += file_len

print("Part 2:", part_2)  # Part 2: 6469636832766
