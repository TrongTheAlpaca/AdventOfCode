DEBUG = False

with open("input.txt") as f:
    lines = f.read().splitlines()
    commands = iter(lines)

X = 1
cooldown = 1
signals = []
current = "INIT"
CRT_screen = ""
suspend = 0
cycle = 0
while True:

    cooldown -= 1
    cycle += 1

    if cooldown == 0:

        X += suspend
        suspend = 0
        current = next(commands, None)

        if current is None:
            break

        if current == "noop":
            cooldown += 1
        else:
            suspend = int(current.split(" ")[1])
            cooldown += 2

    if DEBUG:
        print(f"{cycle:>3}", f"{X:>3}", current)

    if cycle in [20, 60, 100, 140, 180, 220]:
        signals.append(X * cycle)

    # Draw CRT
    crt_x = cycle - 1
    while crt_x >= 40:
        crt_x -= 40
    CRT_screen += "⬜" if crt_x in [X - 1, X, X + 1] else "⬛"

    if DEBUG:
        print("CRT:", CRT_screen)
        print(
            "CUR:",
            "".join((["#" if i in [X - 1, X, X + 1] else "." for i in range(40)])),
        )

if DEBUG:
    print("\nFINAL:")
    for i, signal in enumerate(signals):
        print(i, signal)
print("PART 1:", sum(signals))  # 16480


print("PART 2:")
for Y in range(6):
    print(CRT_screen[Y * 40 : Y * 40 + 40])  # PLEFULPB
