with open("input.txt", "r") as f:
    rows = f.read().splitlines()

paper_rolls = set()
for x, row in enumerate(rows):
    for y, cell in enumerate(row):
        if cell == "@":
            paper_rolls.add((x, y))

# fmt: off
SURROUND = [
    (-1,+1),(+0,+1),(+1,+1),
    (-1,+0),        (+1,+0),
    (-1,-1),(+0,-1),(+1,-1),
]
# fmt: on

n_removed_history = []

while True:
    removable = set()
    for x, y in paper_rolls:
        aoe = {(x + dx, y + dy) for dx, dy in SURROUND}

        if len(paper_rolls & aoe) < 4:
            removable.add((x, y))

    paper_rolls -= removable
    n_removed_history.append(len(removable))

    if len(removable) == 0:
        break


print("Part 1:", n_removed_history[0])  # 1551
print("Part 2:", sum(n_removed_history))  # 9784
