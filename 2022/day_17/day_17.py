DEBUG = False

from tqdm import trange

LEFT_OFFSET = 2
WIDTH = 7

# fmt: off

def LINE():
    return [(0,0),(1,0),(2,0),(3,0)]

def PLUS():
    return [
              (1,2), 
        (0,1),(1,1),(2,1),
              (1,0)
    ]

def STEEP():
    return [
                    (2,2), 
                    (2,1),
        (0,0),(1,0),(2,0)
    ]

def STANDING():
    return [
        (0,3), 
        (0,2), 
        (0,1), 
        (0,0)
    ]

def CUBE():
    return [
        (0,1),(1,1), 
        (0,0),(1,0)
    ]


# fmt: on


def reset_iterator():
    return iter([LINE, PLUS, STEEP, STANDING, CUBE])


with open("input.txt") as f:
    jet_string = f.read()


def reset_jet_iterator():
    return iter(list(jet_string))


C = len(jet_string)
rocks = set()


def print_board(piece=None):
    if piece is None:
        piece = set()
    else:
        piece = set(piece)

    painting = []
    for Y in range(100):
        new_layer = []
        for X in range(WIDTH):
            if (X, Y) in piece:
                new_layer.append("X")
            else:
                new_layer.append("." if (X, Y) not in rocks else "#")
        painting.append(new_layer)

    for layer in reversed(painting):
        print("".join(layer))


def move(piece: list[tuple], x: int, y: int) -> list[tuple]:

    new_piece = list(map(lambda p: (p[0] + x, p[1] + y), piece))

    if (
        all(map(lambda p: 0 <= p[0] < WIDTH, new_piece))
        and all(map(lambda p: 0 <= p[1], new_piece))
        and all(map(lambda p: p not in rocks, new_piece))
    ):
        return new_piece
    else:
        return piece


def calc_height() -> int:
    return max(rocks, key=lambda p: p[1])[1] + 1


current_tallest = 0
current_piece_iterator = reset_iterator()
current_jet_iterator = reset_jet_iterator()
current_jet_wind = None

heights = []

# PART 2 metrics
FIRST_BENCHMARK = None
SECOND_BENCHMARK = None
HEIGHT_OFFSET = 0

PART = 2
EPOCHS = 2022 if PART == 1 else 1000000000000
epoch = 0
while epoch < EPOCHS + 1:
    # for i in trange(EPOCHS + 1):
    current_piece = next(current_piece_iterator, None)
    if current_piece is None:
        current_piece_iterator = reset_iterator()
        current_piece = next(current_piece_iterator)

    current_piece = current_piece()

    if rocks:
        current_tallest = calc_height()
        heights.append(current_tallest)
    print(epoch, current_tallest)
    current_piece = move(
        current_piece, LEFT_OFFSET, current_tallest + 3
    )  # Initial offset

    original_piece = current_piece

    if DEBUG:
        print_board(original_piece)

    # if rocks:
    #     if i % (9 + 1431 + 1720 * 3) == 0:
    #         VV = calc_height()
    #         print()

    while True:

        # JET
        current_jet_wind = next(current_jet_iterator, None)
        if current_jet_wind is None:
            current_jet_iterator = reset_jet_iterator()
            current_jet_wind = next(current_jet_iterator)

            if PART == 2:
                if not FIRST_BENCHMARK:
                    FIRST_BENCHMARK = (epoch, calc_height())  # 2773, 5511, 8249, 10987
                elif not SECOND_BENCHMARK:

                    # Jesus take the wheel
                    SECOND_BENCHMARK = (epoch, calc_height())
                    DIFFERENCE_EPOCH = SECOND_BENCHMARK[0] - FIRST_BENCHMARK[0]
                    DIFFERENCE_HEIGHT = SECOND_BENCHMARK[1] - FIRST_BENCHMARK[1]
                    times_left, rest = divmod(EPOCHS - epoch, DIFFERENCE_EPOCH)
                    HEIGHT_OFFSET = times_left * DIFFERENCE_HEIGHT
                    epoch += times_left * DIFFERENCE_EPOCH
                    print()

        if DEBUG:
            print("LEFT" if current_jet_wind == "<" else "RIGHT")
        dx = -1 if current_jet_wind == "<" else +1
        c = move(original_piece, dx, 0)

        # DOWNWARD
        new_c = move(c, 0, -1)

        # CONFIRM MOVEMENT
        if new_c == c:
            new_rock_set = set(c)
            rocks |= new_rock_set

            break
        else:
            original_piece = new_c

    if DEBUG:
        print_board()

    epoch += 1
    # print(rocks)
    # print()


print("END")

for rock in rocks:
    print(rock)

print("PART 1:", current_tallest)  # 3235

print("PART 2:", current_tallest + HEIGHT_OFFSET)  # 1591860465110
