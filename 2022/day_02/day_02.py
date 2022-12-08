# PREAMBLE
ROCK = 0
PAPER = 1
SCISSOR = 2

ROTATIONS = [
    [SCISSOR, ROCK, PAPER],
    [ROCK, PAPER, SCISSOR],
    [PAPER, SCISSOR, ROCK],
]

SCORE = [0, 3, 6]  # LOSE, DRAW, WIN

hand = {"A": ROCK, "B": PAPER, "C": SCISSOR, "X": ROCK, "Y": PAPER, "Z": SCISSOR}

worth = lambda move: move + 1

with open("input.txt") as f:
    rounds: tuple[str, str] = [
        tuple(map(hand.get, match.split())) for match in f.readlines()
    ]

part_1 = 0
for (p1, p2) in rounds:
    part_1 += worth(p2)  # Hand worth
    if p1 == p2:
        part_1 += SCORE[1]  # DRAW
    elif (p1, p2) in [(ROCK, PAPER), (PAPER, SCISSOR), (SCISSOR, ROCK)]:
        part_1 += SCORE[2]  # WIN
    else:
        part_1 += SCORE[0]  # LOSE

# PART 1
print(part_1)  # 8933 CORRECT

# PART 2
print(sum(SCORE[p2] + worth(ROTATIONS[p1][p2]) for (p1, p2) in rounds))  # 11998 CORRECT
