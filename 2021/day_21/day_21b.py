from collections import Counter, defaultdict

# PREAMBLE
with open("input", "r") as f:
    init_position = tuple([int(line[-1]) for line in f.read().split('\n')])


def move(pos, steps):
    pos += steps
    return pos if pos <= 10 else pos - 10


n_wins = [0, 0]
player_point_counts: list[dict[tuple[int, int], Counter[tuple[int, int]]]] = [defaultdict(Counter), defaultdict(Counter)]
player_point_counts[0][(0, 0)][init_position] = 1

P = 1  # Current Player (0 or 1)
while len(player_point_counts[0]) > 0 or len(player_point_counts[1]) > 0:
    print("N_WINS:", n_wins)
    P = not P
    while len(player_point_counts[P]) > 0:
        points, position_counter = player_point_counts[P].popitem()
        for position, count in position_counter.items():
            for x, y, z in [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]:
                new_pos = move(position[P], x+y+z)
                updated_points = (points[0], points[1] + new_pos) if P else (points[0] + new_pos, points[1])
                updated_positions = (position[0], new_pos) if P else (new_pos, position[1])

                if updated_points[P] >= 21:
                    n_wins[P] += count
                else:
                    player_point_counts[not P][updated_points][updated_positions] += count

print(f"Most winning: Player {1 if n_wins[0] > n_wins[1] else 2}: {max(n_wins)} wins")  # PART 2: 157253621231420
