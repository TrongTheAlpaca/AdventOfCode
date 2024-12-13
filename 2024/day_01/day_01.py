with open("input.txt", "r") as f:
    lines = f.read().splitlines()

l0, l1 = [], []
d0, d1 = {}, {}
for line in lines:
    x, y = map(int, line.split())
    l0.append(x)
    l1.append(y)
    if x not in d0:
        d0[x] = 0
    d0[x] += 1

    if y not in d1:
        d1[y] = 0
    d1[y] += 1

l0.sort()
l1.sort()

result = [abs(x - y) for x, y in zip(l0, l1)]
print("Part 1:", sum(result))  # 3246517

total = sum(a * d1.get(a, 0) for a in l0)
print("Part 2:", total)  # 29379307
