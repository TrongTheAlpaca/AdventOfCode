import math
from typing import Union


class Fish:
    def __init__(self, parent, value):
        self.parent: Pair = parent
        self.value: int = value
        self.depth = self.get_depth()

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        assert isinstance(other, Fish)
        return Fish(self.parent, self.value + other.value)

    # TODO: Move to PAIR?
    def split(self):
        assert 10 <= self.value
        temp_pair = Pair(self.parent, None, None)
        temp_pair.left = Fish(temp_pair, math.floor(self.value / 2))
        temp_pair.right = Fish(temp_pair, math.ceil(self.value / 2))
        if self.parent.left == self:
            self.parent.left = temp_pair
        else:
            self.parent.right = temp_pair

        return self.parent


    def get_depth(self):
        depth = 0
        cur = self
        while cur:
            depth += 1
            cur = cur.parent
        return depth


class Pair:
    def __init__(self, parent, left, right):
        self.parent: Pair = parent
        self.left: Union[Pair, Fish] = left
        self.right: Union[Pair, Fish] = right

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def is_simple(self):
        """ Simple pair = left and right child are both integers. """
        return isinstance(self.left, Fish) and isinstance(self.right, Fish)

    def get_depth(self):
        depth = 0
        cur = self
        while cur:
            depth += 1
            cur = cur.parent
        return depth

    def __add__(self, other):
        assert isinstance(other, Pair)
        return map_fish([self.to_list(), other.to_list()])

    def explode(self):
        # CHILD POV
        assert self.is_simple()

        # LEFT VALUE EXPLOSION
        curr = self.parent
        if isinstance(curr.left, Fish):
            curr.left += self.left
        else:
            prev = self
            while curr and curr.left == prev:  # Find valid off-branching
                prev = curr
                curr = curr.parent

            if curr is not None:
                if isinstance(curr.left, Fish):
                    curr.left += self.left
                else:
                    curr = curr.left  # Valid left branch
                    while not isinstance(curr.right, Fish):
                        curr = curr.right
                    curr.right += self.left

        # RIGHT VALUE EXPLOSION
        curr = self.parent
        if isinstance(curr.right, Fish):
            curr.right += self.right
        else:
            prev = self
            while curr and curr.right == prev:  # Find valid off-branching
                prev = curr
                curr = curr.parent

            if curr is not None:
                if isinstance(curr.right, Fish):
                    curr.right += self.right
                else:
                    curr = curr.right  # Valid right branch
                    while not isinstance(curr.left, Fish):
                        curr = curr.left
                    curr.left += self.right

        # Final action
        if self.parent.left == self:
            self.parent.left = Fish(self.parent, 0)
        else:
            self.parent.right = Fish(self.parent, 0)

    def to_list(self):
        return eval(str(self))


def map_fish(snailfish: list, parent: Pair = None) -> Pair:
    pair = Pair(parent, None, None)
    pair.left = Fish(pair, snailfish[0]) if isinstance(snailfish[0], int) else map_fish(snailfish[0], pair)
    pair.right = Fish(pair, snailfish[1]) if isinstance(snailfish[1], int) else map_fish(snailfish[1], pair)
    return pair


def calc_magnitude(snailfish: Union[Pair, Fish]) -> int:
    if type(snailfish) is Pair:
        return 3 * calc_magnitude(snailfish.left) + 2 * calc_magnitude(snailfish.right)
    elif type(snailfish) is Fish:
        return snailfish.value


# x = map_fish(root)


def reduce_step(root_fish) -> bool:
    unvisited = [root_fish]
    while unvisited:
        current = unvisited.pop()

        assert isinstance(current, (Fish, Pair)), f"TYPE ERROR? FOUND: {type(current)}"

        if isinstance(current, Pair):
            unvisited.append(current.right)
            unvisited.append(current.left)
            # print(current, '- DEPTH:', current.get_depth())

            if current.get_depth() > 4 and current.is_simple():
                # if not reduce_step(current.left) and not reduce_step(current.right):
                current.explode()
                return True

        elif isinstance(current, Fish) and 10 <= current.value:
            current.split()
            return True

    return False


def reduce_step_explosion(root_fish) -> bool:
    unvisited = [root_fish]
    while unvisited:
        current = unvisited.pop()

        assert isinstance(current, (Fish, Pair)), f"TYPE ERROR? FOUND: {type(current)}"

        if isinstance(current, Pair):
            unvisited.append(current.right)
            unvisited.append(current.left)
            # print(current, '- DEPTH:', current.get_depth())

            if current.get_depth() > 4 and current.is_simple():
                current.explode()
                return True

    return False


def reduce_step_split(root_fish) -> bool:
    unvisited = [root_fish]
    while unvisited:
        current = unvisited.pop()

        assert isinstance(current, (Fish, Pair)), f"TYPE ERROR? FOUND: {type(current)}"

        if isinstance(current, Pair):
            unvisited.append(current.right)
            unvisited.append(current.left)
            # print(current, '- DEPTH:', current.get_depth())

        elif isinstance(current, Fish) and 10 <= current.value:
            current.split()
            return True

    return False


def reduce(root_fish) -> Pair:
    while True:
        if not reduce_step_explosion(root_fish):
            if not reduce_step_split(root_fish):
                break

    return root_fish


def reduce_(root_fish) -> Pair:
    step = 0
    print('\nINIT:    -', root_fish)
    while reduce_step(root_fish):
        print(f"step:{step:>3}", '-', root_fish)
        step += 1
    return root_fish


if __name__ == '__main__':

    with open("input") as f:
        fishes = [eval(line) for line in f.readlines()]
        fishes = [map_fish(fish) for fish in fishes]

    final = fishes[0]
    for fish in fishes[1:]:
        final += fish
        final = reduce(final)

    print("Part 1:", calc_magnitude(final))  # PART 1: 4088

    magnitudes = []
    for fish_1 in fishes:
        for fish_2 in fishes:
            if fish_1 != fish_2:
                magnitudes.append(calc_magnitude(reduce(fish_1 + fish_2)))

    print("Part 2:", max(magnitudes))  # PART 2: 4536
