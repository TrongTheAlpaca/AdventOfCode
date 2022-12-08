with open('test/puzzle_input.txt') as f:
    sums = [int(x) for x in f.read().splitlines()]

PREAMBLE = 25

current_scope = sums[:PREAMBLE]

part_1 = 0
for s in sums[PREAMBLE:]:

    safe = False
    for i in range(PREAMBLE):
        for j in range(i, PREAMBLE):
            temp_sum = current_scope[i] + current_scope[j]
            if s == temp_sum:
                safe = True
                break
        if safe:
            break

    if not safe:
        print('Part 1:', s)  # Part 1: 144381670
        part_1 = s
        break

    del current_scope[0]
    current_scope.append(s)

current_list = set()
found = False
for i in range(len(sums)):
    # print(i)
    current_list.add(sums[i])

    for j in range(i, len(sums)):
        current_list.add(sums[j])

        if sum(current_list) > part_1:
            current_list = set()
            break
        elif sum(current_list) == part_1:
            print(current_list)
            found = True
            break

    if found:
        break

print(min(current_list))
print(max(current_list))
print('Part 2:', sum([min(current_list), max(current_list)]))
