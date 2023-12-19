from collections import Counter


CARD_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

HAND_RANKS = {
    (5,): 7,  # Five of a kind
    (1, 4): 6,  # Four of a kind
    (2, 3): 5,  # Full House
    (1, 1, 3): 4,  # Three of a kind
    (1, 2, 2): 3,  # Two pair
    (1, 1, 1, 2): 2,  # Two pair
    (1, 1, 1, 1, 1): 1,  # High card
}


def get_hand_rank(hand: str, is_part_2: bool) -> int:
    counts = sorted(Counter(hand).values())
    if is_part_2:
        n_jokers = hand.count("J")
        if 0 < n_jokers < 5:
            counts.remove(n_jokers)
            counts[-1] += n_jokers

    return HAND_RANKS[tuple(counts)]


def get_hand_value(hand: str, is_part_2: bool) -> tuple[int]:
    hand_rank = get_hand_rank(hand, is_part_2=is_part_2)
    card_ranks = CARD_RANKS if not is_part_2 else ["J"] + CARD_RANKS
    card_translated = tuple(map(lambda x: card_ranks.index(x), hand))
    return (hand_rank,) + card_translated


with open("input.txt") as f:
    lines = [(x[0], int(x[1])) for x in map(lambda l: l.split(), f.read().splitlines())]
    lines_part_1 = sorted(lines, key=lambda x: get_hand_value(x[0], False))
    lines_part_2 = sorted(lines, key=lambda x: get_hand_value(x[0], True))

print("part 1:", sum([h[1] * (i + 1) for i, h in enumerate(lines_part_1)]))  # 248113761
print("part 2:", sum([h[1] * (i + 1) for i, h in enumerate(lines_part_2)]))  # 246285222
