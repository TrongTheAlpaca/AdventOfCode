with open('input', 'r') as f:
    lines = f.read().splitlines()

HEIGHT = len(lines)
WIDTH = len(lines[0])
print(f"{HEIGHT}x{WIDTH}")


def print_board(_cucumbers_h, _cucumbers_v):
    for y in range(HEIGHT):
        print()
        for x in range(WIDTH):
            if (x, y) in _cucumbers_h:
                print('>', end='')
            elif (x, y) in _cucumbers_v:
                print('v', end='')
            else:
                print('.', end='')
    print()


def step(_cucumbers_h, _cucumbers_v):
    new_cucumbers_h = set()
    for c in _cucumbers_h:
        x, y = c
        next_x = x + 1 if x < WIDTH - 1 else 0
        next_pos = (next_x, y)
        if next_pos in _cucumbers_h or next_pos in _cucumbers_v:
            new_cucumbers_h.add((x, y))
        else:
            new_cucumbers_h.add(next_pos)

    new_cucumbers_v = set()
    for c in _cucumbers_v:
        x, y = c
        next_y = y + 1 if y < HEIGHT - 1 else 0
        next_pos = (x, next_y)
        if next_pos in new_cucumbers_h or next_pos in _cucumbers_v:
            new_cucumbers_v.add((x, y))
        else:
            new_cucumbers_v.add(next_pos)

    return new_cucumbers_h, new_cucumbers_v


cucumbers_h = set()
cucumbers_v = set()
for y, line in enumerate(lines):
    for x, tile in enumerate(line):
        if tile == '>':
            cucumbers_h.add((x, y))
        elif tile == 'v':
            cucumbers_v.add((x, y))

for epoch in range(1000):
    n_cucumbers_h, n_cucumbers_v = step(cucumbers_h, cucumbers_v)
    if n_cucumbers_h == cucumbers_h and n_cucumbers_v == cucumbers_v:
        print(epoch + 1)
        break
    cucumbers_h, cucumbers_v = n_cucumbers_h, n_cucumbers_v

# PART 1: 557
