with open("input.txt", "r") as f:
    rules, tasks = [s.splitlines() for s in f.read().split("\n\n")]
    tasks = [list(map(int, line.split(","))) for line in tasks]

ruleset: dict[str, set] = {}
for rule in rules:
    x, y = map(int, rule.split("|"))
    if x not in ruleset:
        ruleset[x] = set()
    ruleset[x].add(y)

results = [0, 0]
for task in tasks:
    is_correct = True
    for i, current in enumerate(task):
        if current in ruleset:
            for j in range(i + 1):
                if task[j] in ruleset[current]:
                    is_correct = False
                    task[i], task[j] = task[j], task[i]
                    j = 0

    results[0 if is_correct else 1] += task[len(task) // 2]

print("part 1:", results[0])  # 4905
print("part 2:", results[1])  # 6204
