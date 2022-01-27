# PREAMBLE
with open("input", "r") as f:
    position = [int(line[-1]) for line in f.read().split('\n')]

n_dice_rolls = 0
current_dice = 1
points = [0, 0]


def roll_dice(times=3) -> int:
    global current_dice, n_dice_rolls
    total = 0
    for roll in range(times):
        total += current_dice
        current_dice = current_dice + 1 if current_dice < 100 else 1
    n_dice_rolls += times
    return total


def move_player(player, steps):
    for s in range(steps):
        position[player] = position[player] + 1 if position[player] < 10 else 1
    points[player] += position[player]


player = False  # False => 0 and True => 1
while points[0] < 1000 and points[1] < 1000:
    steps = roll_dice()
    move_player(player, steps)
    player = not player

print(points)
print(min(points) * n_dice_rolls)  # PART 1: 604998
