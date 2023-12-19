with open("test_2.txt") as f:
    parts = f.read().split("\n\n")
    moves = parts[0]
    guides = parts[1].splitlines()

guide_map = {}
for guide in guides:
    start, end = guide.split(" = ")
    end = end[1:-1].split(", ")
    guide_map[start] = end


# binary_moves = "".join(map(lambda x: str(int(x == "R")), reversed(moves)))

# binary_moves = int(binary_moves, 2)

# trees: dict[str, list[str]] = {}

# for node in guide_map:
#     trees[node] = []
#     visited = set()
#     to_visit = [node]
#     while to_visit:
#         current = to_visit.pop()

#         if current in visited:
#             trees[node].append(None)
#         else:
#             visited.add(current)
#             left, right = guide_map[current]
#             to_visit.append(left)
#             to_visit.append(right)


# for node, tree in trees.items():
#     print(node, "->", tree.index("ZZZ") if "ZZZ" in tree else "NO PATH")
#     print()

# print()


# Find all possible paths to Z from each node
current_end = "ZZZ"
potential_routes: dict[str, set] = {current_end: set()}
for node, guide in guide_map.items():
    if node == current_end:
        continue

    if current_end in guide:
        potential_routes[current_end].add(node)


print()
