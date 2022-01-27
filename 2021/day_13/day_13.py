# PREAMBLE
with open("input") as f:
    dots: set[tuple[int, int]] = set()
    while '\n' != (line := f.readline()):
        dots.add((int(line.split(',')[0]), int(line.split(',')[1])))
    folds = [*map(lambda x: (x.split('=')[0][-1], int(x.split('=')[1])), f.read().split('\n'))]


def print_paper():
    for y in range(max(dots, key=lambda s: s[1])[1] + 1):
        for x in range(max(dots, key=lambda s: s[0])[0] + 1):
            print('█' if (x, y) in dots else '░', end='')
        print()


for step, (direction, mark) in enumerate(folds):
    affected = [dot for dot in dots if dot[0 if direction == 'x' else 1] > mark]
    dots.difference_update(affected)
    dots.update(map(lambda c: (2 * mark - c[0], c[1]) if direction == 'x' else (c[0], 2 * mark - c[1]), affected))

    print(f"Fold {step:>2} - No. of dots: {len(dots):>3}")  # PART 1: 770 is correct!

print_paper()  # PART 2: 'EPUELPBR' is correct!
