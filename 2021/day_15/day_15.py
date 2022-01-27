from collections import defaultdict
from queue import PriorityQueue

# PREAMBLE
with open("input") as f:
    lines = f.read().split('\n')
    risks = [[int(x) for x in list(line)] for line in lines]


def increment(n, p):
    return n + p if n + p <= 9 else n + p - 9


# PART 2:
big_boi = []
for s in range(5):
    temp_risks = [[increment(z, s) for z in row] for row in risks]
    for row in temp_risks:
        temp_row = []
        for ss in range(5):
            temp_row.extend([increment(e, ss) for e in row])
        big_boi.append(temp_row)


def dijkstra(risk_matrix):

    start = (0, 0)
    goal = (len(risk_matrix[0]) - 1, len(risk_matrix) - 1)

    open_set = PriorityQueue()
    open_set.put_nowait(start)

    came_from = dict()

    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    while not open_set.empty():
        current = open_set.get()

        if current == goal:
            total_cost = 0
            while current in came_from:
                current = came_from[current]
                total_cost += risk_matrix[current[1]][current[0]]
            return total_cost

        for neighbor in [(current[0] + dx, current[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if not(0 <= neighbor[0] < len(risk_matrix[0]) and 0 <= neighbor[1] < len(risk_matrix)):
                continue

            travel_cost = risk_matrix[neighbor[1]][neighbor[0]]
            temp_g_score = g_score[current] + travel_cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score

                if neighbor not in open_set.queue:
                    open_set.put(neighbor)


print(dijkstra(risks))    # PART 1:  388 is correct
print(dijkstra(big_boi))  # PART 2: 2811 is correct
