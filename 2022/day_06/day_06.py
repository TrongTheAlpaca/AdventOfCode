s = lambda n, l: [i + n for i in range(0, len(l)) if len(set(l[i : i + n])) == n]
print(s(4, d := open("input.txt", "r").read())[0], s(14, d)[0], sep="\n")
