from timeit import default_timer as timer


with open("example.txt") as f:
    lines = [l.split(" ") for l in f.read().splitlines()]

    costs = []

    for line in lines:
        ore = int(line[6])
        clay = int(line[12])
        obsidian = int(line[18]), int(line[21])
        geode = int(line[27]), int(line[30])
        costs.append((ore, clay, obsidian, geode))


ORE, CLAY, OBSIDIAN, GEODE = 0, 1, 2, 3


COSTS = costs[0]  # TODO: Loop for each blueprint
initial = (1, COSTS, (0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0))

# fmt: off
start = timer()

queue = [initial]
geode_counts = []
while queue:
    minute, costs, resources, robots, recruits = queue.pop(0)

    n_ore = resources[ORE] + robots[ORE]
    n_clay = resources[CLAY] + robots[CLAY]
    n_obsidian = resources[OBSIDIAN] + robots[OBSIDIAN]
    n_geode = resources[GEODE] + robots[GEODE]

    if minute == 24:
        # if n_geode > 5:
        print("GEODES:", n_geode)
        geode_counts.append(n_geode)
        continue

    new_robots = (
        robots[ORE] + recruits[ORE],
        robots[CLAY] + recruits[CLAY],
        robots[OBSIDIAN] + recruits[OBSIDIAN],
        robots[GEODE] + recruits[GEODE],
    )

    if costs[GEODE][0] <= n_ore and costs[GEODE][1] <= n_obsidian:
        # print(f"{minute}: BUY {robots[GEODE]} ROBOT")
        new_resources = (n_ore - costs[GEODE][0], n_clay, n_obsidian - costs[GEODE][1], n_geode)
        queue.append((minute + 1, costs, new_resources, new_robots, (0, 0, 0, 1)))
    if costs[OBSIDIAN][0] <= n_ore and costs[OBSIDIAN][1] <= n_clay:
        #print("BUY OBSIDIAN ROBOT")
        new_resources = (n_ore - costs[OBSIDIAN][0], n_clay - costs[OBSIDIAN][1], n_obsidian, n_geode)
        queue.append((minute + 1, costs, new_resources, new_robots, (0, 0, 1, 0)))
    if costs[CLAY] <= n_ore:
        # print("BUY CLAY ROBOT")
        new_resources = (n_ore - costs[CLAY], n_clay, n_obsidian, n_geode)
        queue.append((minute + 1, costs, new_resources, new_robots, (0, 1, 0, 0)))
    # if costs[ORE] <= n_ore:
    #     # print("BUY ORE ROBOT")
    #     new_resources = (n_ore - costs[ORE], n_clay, n_obsidian, n_geode)
    #     queue.append((minute + 1, costs, new_resources, new_robots, (1, 0, 0, 0)))

    queue.append((minute + 1, costs, (n_ore, n_clay, n_obsidian, n_geode), new_robots, (0, 0, 0, 0)))
# fmt: on
end = timer()

print(sorted(filter(lambda x: x > 0, geode_counts), reverse=True))

print(end - start)
