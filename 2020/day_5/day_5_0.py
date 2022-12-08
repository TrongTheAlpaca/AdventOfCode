with open('test/puzzle_input.txt') as f:
    values = f.read().splitlines()

ids = []
for line in values:
    current_number = 128
    start = 0
    end = 127
    for y in range(7):

        current_number //= 2

        if line[y] == 'F':
            end -= current_number
        else:
            start += current_number

        # print(line[y], ': ', 'Start:', start, ', End:', end)

    row = start if line[6] == 'F' else end

    current_number = 8
    start = 0
    end = 7
    for y in range(7, 10):

        current_number //= 2

        if line[y] == 'L':
            end -= current_number
        else:
            start += current_number

        # print(line[y], ': ', 'Start:', start, ', End:', end)

    column = start if line[9] == 'L' else end

    # print('ROW:', row, '\tCOL:', column)
    seat_id = row * 8 + column
    ids.append(seat_id)

print(max(ids))  # PART 1: 980

# Part 2
found_ids = set(ids)
mask_ids = set(range(min(ids), max(ids)+1))
print(mask_ids - found_ids)  # PART 2: 607
