import queue
from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True, order=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True, order=True)
class Move:
    heat: int
    position: Position
    direction: tuple[int, int]
    n_straights: int


with open("test.txt", "r") as f:
    board = [tuple(map(int, row)) for row in f.read().splitlines()]


WIDTH = len(board[0])
HEIGTH = len(board)

NORTH = (+0, -1)
WEST = (-1, +0)
SOUTH = (+0, +1)
EAST = (+1, +0)


ROTATE_LEFT = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}
ROTATE_RIGHT = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}


def move_from(position: Position, direction: tuple[int, int]) -> Position:
    return Position(position.x + direction[0], position.y + direction[1])


def get_heat_loss(position: Position) -> int:
    return board[position.y][position.x]


def is_within_boundaries(position: Position) -> bool:
    return (0 <= position.x < WIDTH) and (0 <= position.y < HEIGTH)


def try_move(
    visited: dict,
    to_visit,
    came_from,
    current_move: Move,
    next_direction: tuple[int, int],
    is_straight: bool,
):
    next_position = move_from(current_move.position, next_direction)
    if is_within_boundaries(next_position):
        next_heat = current_move.heat + get_heat_loss(next_position)
        next_n_straights = current_move.n_straights + 1 if is_straight else 0
        next_move = Move(
            next_heat,
            next_position,
            next_direction,
            next_n_straights,
        )
        if next_position not in visited:
            visited[next_position] = dict()
        if next_direction not in visited[next_position]:
            visited[next_position][next_direction] = dict()
        if next_n_straights not in visited[next_position][next_direction]:
            to_visit.put(next_move)
            visited[next_position][next_direction][next_n_straights] = next_heat
        elif next_heat < visited[next_position][next_direction][next_n_straights]:
            # if next_move not in to_visit:
            to_visit.put(next_move)
            for i in range(next_n_straights, 4):
                visited[next_position][next_direction][i] = next_heat


# visited = [dict(), dict(), dict(), dict()]  # (position, direction) -> lowest heat
to_visit = queue.PriorityQueue()
to_visit.put(Move(0, Position(0, 0), SOUTH, 0))
to_visit.put(Move(0, Position(0, 0), EAST, 0))

# visited = [pos][direction][n_straights] -> optimal_heat
# visited = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: float("inf"))))
visited = dict()
came_from = dict()  # [pos][direction] -> pos

# def get_optimal_origin(visited: dict, came_from: dict, pos: Position):
#     optimal_origin = None
#     optimal_direction = None
#     if pos in visited:
#         for dir, n_straights in visited[pos].items():
#             for heat in n_straights.values():
#                 if not optimal_origin:


# while not to_visit.empty():
#     current = to_visit.get()

#     # Forward
#     if current.n_straights < 3:
#         try_move(
#             visited, to_visit, came_from, current, current.direction, is_straight=True
#         )

#     # Left
#     next_direction = ROTATE_LEFT[current.direction]
#     try_move(visited, to_visit, came_from, current, next_direction, is_straight=False)

#     # right
#     next_direction = ROTATE_RIGHT[current.direction]
#     try_move(visited, to_visit, came_from, current, next_direction, is_straight=False)


goal = Position(WIDTH - 1, HEIGTH - 1)
# for v in visited:
for k, v in visited.items():
    if k == goal:
        print(k, v)

trail = set()
current_backtrail = goal
while current_backtrail != Position(0, 0):
    print(current_backtrail)
    current_backtrail = came_from[current_backtrail]
    trail.add(current_backtrail)

print()
# PART 1
# 883 TOO LOW
# 884 TOO LOW
# 929 TOO HIGH
# 931 TOO HIGH
