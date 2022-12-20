import itertools
import networkx as nx
from tqdm import tqdm
import matplotlib.pyplot as plt

G = nx.Graph()

MINUTES = 30
DEBUG = False

tunnels = dict()
rates = dict()
opened = dict()
optimised_distance = dict()
nodes = []

with open("example.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.replace(";", "").replace("=", " ").replace(",", "").split(" ")

        valve = line[1]
        rate = int(line[5])
        road = line[10:]

        rates[valve] = rate
        opened[valve] = False
        tunnels[valve] = road

        nodes.append(valve)


for valve in nodes:
    G.add_node(nodes.index(valve), name=valve)
    for r in tunnels[valve]:
        G.add_edge(nodes.index(valve), nodes.index(r))

# subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight="bold")
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(10, 20), range(70)], with_labels=True, font_weight="bold")
plt.show()
# CALCULATE OPTIMAL PATH FROM EVERYWHERE TO EVERYWHERE
for valve_x in tunnels:

    optimised_distance[valve_x] = dict()

    for valve_y in tunnels:

        if valve_x == valve_y:
            continue

        print(f"CALC: {valve_x} <-> {valve_y}:", end=" ")
        if valve_y not in optimised_distance[valve_x]:

            # BFS
            queue = [valve_x]
            visited = {valve_x}
            previous = dict()
            previous[valve_x] = None

            while len(queue) > 0:
                current = queue.pop(0)
                for neighbor in tunnels[current]:
                    if neighbor not in previous:
                        queue.append(neighbor)
                        previous[neighbor] = current

            current = valve_y
            path = []
            while current != valve_x:
                path.append(current)
                current = previous[current]
            path.reverse()
            distance = len(path)
            optimised_distance[valve_x][valve_y] = distance

            if valve_y not in optimised_distance:
                optimised_distance[valve_y] = dict()

            optimised_distance[valve_y][valve_x] = distance
            print(distance)

print()


def calculate_potential(x, y, total_minutes_left):

    # Calc distance in minutes from current
    d = optimised_distance[x][y]

    # Calc valve opened * minutes_left
    minutes_left = total_minutes_left - d
    potential = rates[y] * minutes_left
    return potential


print("START:")

BEST = 0
BESTS = []

valueables = [valve for valve, rate in rates.items() if rate > 0]

print(len(valueables))
# valueables = ["DD", "BB", "JJ", "HH", "EE", "CC"]  # MOCK CORRECT
valueables = itertools.permutations(valueables)

for V in tqdm(valueables):
    current_valuables = list(V)
    current = "AA"
    pressure_released = 0
    current_rate = []

    total_minutes_left = MINUTES - 1
    while current_valuables and total_minutes_left > 0:
        pressure_released += sum(current_rate)

        if DEBUG:
            print(
                "\nMINUTE:",
                30 - total_minutes_left,
                f"- (total: {pressure_released})",
            )
            print(f"rate: {sum(current_rate)} ({current_rate})")

            print("Current:", current)
        # best_destination = None
        # best_potential = 0

        # for value in valueables:
        #     if opened[value] == False:
        #         potential = calculate_potential(current, value, total_minutes_left)
        #         print(f"-> {value} >> potential: {potential}")
        #         if potential > best_potential:
        #             best_destination = value
        #             best_potential = potential
        best_destination = current_valuables.pop(0)

        # if best_destination:

        if DEBUG:
            print(
                f"selected: {current} -> {best_destination} ({optimised_distance[current][best_destination]}): +rate: {rates[best_destination]}"
            )
        # current_valuables.remove(best_destination)

        distance_cost = optimised_distance[current][best_destination]
        total_minutes_left -= distance_cost
        pressure_released += distance_cost * sum(current_rate)
        total_minutes_left -= 1
        current = best_destination
        current_rate.append(rates[best_destination])

    if DEBUG:
        print(sum(current_rate))

    pressure_released += sum(current_rate) * (total_minutes_left + 1)
    if pressure_released > BEST:
        BEST = pressure_released
    print((pressure_released, V))
    BESTS.append((pressure_released, V))

    if DEBUG:
        print(pressure_released)

print("PART 1:", BEST)
# for i in BESTS:
#     print(i)

for i in sorted(BESTS):
    print(i)
print()
# for minute in range(MINUTES):

#     print("\nminute:", minute)
#     pressure_released += current_rate
#     print(f"releasing: {current_rate} => total: {pressure_released}")

#     print("Current:", current)
#     best_destination = None
#     best_potential = 0

#     for value in valueables:
#         if opened[value] == False:
#             total_minutes_left = MINUTES - minute - 1
#             potential = calculate_potential(current, value, total_minutes_left)
#             print(f"-> {value} >> potential: {potential}")
#             if potential > best_potential:
#                 best_destination = value
#                 best_potential = potential

#     if best_destination:
#         print(
#             f"selected: {current} -> {best_destination} ({optimised_distance[current][best_destination]}): +rate: {rates[best_destination]}"
#         )
#         valueables.remove(best_destination)
#         current = best_destination
#         current_rate += rates[best_destination]


# print(pressure_released)
