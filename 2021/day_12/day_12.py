from collections import defaultdict

# PREAMBLE
with open("input") as f:
    rows: list[tuple[str]] = [tuple(line.split('-')) for line in f.read().split('\n')]

graph = defaultdict(list)
for row in rows:
    graph[row[0]].append(row[1])
    graph[row[1]].append(row[0])


def traverse(allow_double_visit: bool = False, current='start', visited=None):

    if visited is None:
        visited = []

    if current.islower():
        visited.append(current)

    if current == 'end':
        return 1

    has_double_visited = len(set(visited)) < len(visited) if allow_double_visit else True

    n_paths = 0
    for child in [child for child in graph[current] if child != 'start']:
        if not has_double_visited or child not in visited:
            n_paths += traverse(allow_double_visit, child, visited.copy())

    return n_paths


print(traverse(False))  # PART 1:  3802 is correct
print(traverse( True))  # PART 2: 99448 is correct
