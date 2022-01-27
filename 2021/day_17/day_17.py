from tqdm import trange

# PREAMBLE
with open("input") as f:
    x_, y_ = [n.split('=')[1].split('..') for n in f.readline().removeprefix('target area: ').split(', ')]
    x0, x1, y0, y1 = int(x_[0]), int(x_[1]), int(y_[0]), int(y_[1])


def kobe(_x_vel, _y_vel):
    x, y, current_highest = 0, 0, 0
    while y >= y0:
        x += _x_vel
        y += _y_vel

        if y > current_highest:
            current_highest = y

        _x_vel = 0 if _x_vel == 0 else _x_vel - 1 if 0 < _x_vel else _x_vel + 1  # Drag
        _y_vel -= 1  # Gravity

        if x0 <= x <= x1 and y0 <= y <= y1:
            return current_highest

    return -1


n_hits = 0
highest_y = 0
for init_y in trange(-200, 200):
    for init_x in range(300):
        result = kobe(init_x, init_y)
        if result != -1:
            n_hits += 1
            if highest_y < result:
                highest_y = result


print("Part 1:", highest_y)  # PART 1: 3655 is correct!
print("Part 2:", n_hits)     # PART 2: 1447 is correct!
