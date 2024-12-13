import tqdm

with open("input.txt", "r") as f:
    rows = f.read().splitlines()

MAX_X = len(rows[0])
MAX_Y = len(rows)


UP = complex(0, -1)
DOWN = complex(0, 1)
RIGHT = complex(1, 0)
LEFT = complex(-1, 0)

ROTATE_CLOCKWISE = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}

start_pos: complex = None
current_pos: complex = None
current_dir: complex = UP
initial_walls = set()
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == "^":
            start_pos = complex(x, y)
        elif cell == "#":
            initial_walls.add(complex(x, y))

obstructions = {None}
loop_obstructions = set()
progress_bar = None
while obstructions:
    obstruction = obstructions.pop()
    walls = initial_walls | {obstruction}
    current_dir: complex = UP
    current_pos = start_pos
    visited_with_dir = {(start_pos, current_dir)}

    while True:
        is_out = False
        while next_pos := current_pos + current_dir:
            if not (0 <= next_pos.real < MAX_X and 0 <= next_pos.imag < MAX_Y):
                is_out = True
                break

            if next_pos in walls:
                current_dir = ROTATE_CLOCKWISE[current_dir]
            else:
                break

        if is_out:
            if obstruction == None:
                visited_pos_only = set(v[0] for v in visited_with_dir)
                print("Part 1:", len(visited_pos_only))
                obstructions = visited_pos_only - {start_pos}
                progress_bar = tqdm.tqdm(total=len(obstructions) + 1)
            break

        if (next_pos, current_dir) in visited_with_dir:
            loop_obstructions.add(obstruction)
            break

        visited_with_dir.add((next_pos, current_dir))
        current_pos = next_pos

    progress_bar.update(1)

progress_bar.close()
print("Part 2:", len(loop_obstructions))  # 1995
