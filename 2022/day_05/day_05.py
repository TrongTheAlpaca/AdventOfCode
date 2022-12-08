with open("input.txt") as f:
    cells, commands = f.read().split("\n\n")
    T = list(zip(*cells.splitlines()[:-1][::-1]))[1::2][0::2]  # pop -> T -> odd -> even
    extract = lambda s: tuple(map(int, map(s.split(" ").__getitem__, [1, 3, 5])))
    commands = [extract(c) for c in commands.splitlines()]

stacks_p1, stacks_p2 = [[list("".join(t).rstrip()) for t in T][:] for _ in range(2)]
for N, X, Y in commands:
    stacks_p1[Y - 1].extend([stacks_p1[X - 1].pop() for _ in range(N)])
    stacks_p2[Y - 1].extend(stacks_p2[X - 1][-N:])
    stacks_p2[X - 1] = stacks_p2[X - 1][:-N]

print("".join([s[-1] for s in stacks_p1]))  # Part 1
print("".join([s[-1] for s in stacks_p2]))  # Part 2
