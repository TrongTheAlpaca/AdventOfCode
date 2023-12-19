with open("input.txt") as f:
    parts = f.read().split("\n\n")
    moves = parts[0]
    guides = parts[1].splitlines()

guide_map = {}
for guide in guides:
    start, end = guide.split(" = ")
    end = end[1:-1].split(", ")
    guide_map[start] = end

# initial configurations
n_moves = 0
move_idx = 0
current_position = next(iter(guide_map))
path_from = {k: {"L": guide_map[k][0], "R": guide_map[k][1]} for k in guide_map.keys()}
longest_path = {k: 1 for k in guide_map.keys()}
print("STARTED")


def get_next_moves(current_idx: int, n_next_moves: int):
    temp_moves = moves
    while len(temp_moves) < current_idx + n_next_moves:
        temp_moves += moves
    return temp_moves[current_idx : current_idx + n_next_moves]


while current_position != "ZZZ":
    # current_moves: str = moves[move_idx]
    current_moves: str = get_next_moves(move_idx, longest_path[current_position] + 1)
    move_idx = move_idx + longest_path[current_position] + 1
    while move_idx >= len(moves):
        move_idx -= len(moves)

    previous_moves = current_moves
    while current_moves not in path_from[current_position]:
        move_idx -= 1
        if move_idx < 0:
            move_idx = len(moves)

        previous_moves = current_moves
        current_moves = current_moves[:-1]

    last_move = int(previous_moves[-1] == "R")
    second_last_destination = path_from[current_position][previous_moves[:-1]]
    destination = guide_map[second_last_destination][last_move]
    path_from[current_position][previous_moves] = destination

    if longest_path[current_position] < len(previous_moves):
        longest_path[current_position] = len(previous_moves)

    current_position = destination
    n_moves += len(previous_moves)
    move_idx += 1
    if move_idx == len(moves):
        move_idx = 0

    # print(len(current_moves))


print("part 1:", n_moves)


# long_guide_map = {k: dict() for k in guide_map.keys()}

# current = next(iter(guide_map))
# print("START:", current)
# trail = ""
# n_moves = 0
# idx = 0
# while current != "ZZZ":
#     move = int(moves[idx] == "R")
#     previous = current
#     current = guide_map[current][move]

#     trail += move
#     long_guide_map[previous][trail] = current

#     n_moves += 1
#     # print(current)
#     if idx < len(moves) - 1:
#         idx += 1
#     else:
#         idx = 0
