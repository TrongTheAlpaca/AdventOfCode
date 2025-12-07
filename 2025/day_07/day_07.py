with open("input.txt", "r") as f:
    rows = f.read().splitlines()

splitters = []
for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == "^":
            splitters.append((x, y))

children = {s: set() for s in splitters}
n_visited = {s: 0 for s in splitters}
n_visited[splitters[0]] = 1

while splitters:
    parent = splitters.pop(0)
    (x, y) = parent
    for bx, by in [(x - 1, y), (x + 1, y)]:
        dy = 0
        while dy < len(rows):
            dy += 1
            child = (bx, by + dy)
            if child in splitters:
                children[parent].add(child)
                n_visited[child] += n_visited[parent]
                break

part_1 = sum(map(lambda n: 0 < n, n_visited.values()))
part_2 = sum([(2 - len(c)) * n_visited.get(s, 0) for s, c in children.items()])

print("Part 1:", part_1)  # 1560
print("Part 2:", part_2)  # 25592971184998
