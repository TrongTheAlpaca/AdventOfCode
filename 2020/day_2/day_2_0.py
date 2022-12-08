with open('test/puzzle_input.txt') as f:
    values = f.read().splitlines()

lines = [x.split() for x in values]

part_1_count = 0
part_2_count = 0
for line in lines:
    left, right = line[0].split('-')
    left = int(left)
    right = int(right)
    letter = line[1][0]

    # Part 1
    occurrences = line[2].count(letter)
    if left <= occurrences <= right:
        part_1_count += 1

    # Part 2
    occurrence_left = line[2][left-1]
    occurrence_right = line[2][right-1]
    if (occurrence_left, occurrence_right).count(letter) == 1:
        part_2_count += 1

print(part_1_count)
print(part_2_count)


