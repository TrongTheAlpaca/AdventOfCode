def rotate_cw(array):
    return ["".join(t) for t in list(zip(*array[::-1]))]


with open("test.txt", "r") as f:
    lines = f.read().splitlines()
    lines_R = rotate_cw(lines)

WIDTH = len(lines[0])
HEIGHT = len(lines)

total_weights = 0
for y, row in enumerate(lines_R):
    ball_idx = []
    cube_idx = []
    current_n_ball = 0
    total_row_weight = 0
    for x, cell in enumerate(row):
        if cell == "O":
            current_n_ball += 1
        elif cell == "#":
            for ball_idx in range(current_n_ball):
                total_row_weight += x - ball_idx
            current_n_ball = 0

    if 0 < current_n_ball:
        for ball_idx in range(current_n_ball):
            total_row_weight += HEIGHT - ball_idx

    print(f"Column: {y} -", total_row_weight)
    total_weights += total_row_weight

print("Part 1:", total_weights)  # 109385
