with open("input.txt", "r") as f:
    robots = []
    for line in f.read().splitlines():
        pos, vel = line.split()
        pos = tuple(map(int, pos.removeprefix("p=").split(",")))
        vel = tuple(map(int, vel.removeprefix("v=").split(",")))
        robots.append((pos, vel))

MAX_X = 101
MAX_Y = 103
CENTER_HORIZONTAL = MAX_X // 2
CENTER_VERTICAL = MAX_Y // 2

robot_positions = {}
for second in range(7200):

    current_robot_positions = {}
    for idx in range(len(robots)):
        (pos_x, pos_y), (vel_x, vel_y) = robots[idx]

        pos_x, pos_y = (pos_x + vel_x, pos_y + vel_y)

        while MAX_X <= pos_x:
            pos_x -= MAX_X

        while pos_x < 0:
            pos_x += MAX_X

        while MAX_Y <= pos_y:
            pos_y -= MAX_Y

        while pos_y < 0:
            pos_y += MAX_Y

        robots[idx] = ((pos_x, pos_y), (vel_x, vel_y))

        if (pos_x, pos_y) not in current_robot_positions:
            current_robot_positions[(pos_x, pos_y)] = 0
        current_robot_positions[(pos_x, pos_y)] += 1

    # Noticed a weird pattern from 51 and for every 103 seconds after
    if (second + 1 - 51) % 103 == 0:
        print("Second:", second + 1)
        drawing = ""
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if (x, y) in current_robot_positions:
                    drawing += str(current_robot_positions[(x, y)])
                else:
                    drawing += "."
            drawing += "\n"
        print(drawing)
        print()

    if second + 1 == 100:
        for pos, _ in robots:
            if pos not in robot_positions:
                robot_positions[pos] = 0
            robot_positions[pos] += 1

quadrant = [0, 0, 0, 0]
for (x, y), count in robot_positions.items():

    if x < CENTER_HORIZONTAL and y < CENTER_VERTICAL:
        quadrant[0] += count
    elif x > CENTER_HORIZONTAL and y < CENTER_VERTICAL:
        quadrant[1] += count
    elif x < CENTER_HORIZONTAL and y > CENTER_VERTICAL:
        quadrant[2] += count
    elif x > CENTER_HORIZONTAL and y > CENTER_VERTICAL:
        quadrant[3] += count

part_1 = quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3]
print("Part 1:", part_1)  # Part 1: 218619120

# Part 2: 7055
