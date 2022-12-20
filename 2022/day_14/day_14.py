PART_1 = False

with open("input.txt") as f:
    lines = f.read().splitlines()

lowest_y = 0
abyss = dict()
walls = set()

for line in lines:
    coords = list(map(lambda x: tuple(map(int, x.split(",")[:2])), line.split(" -> ")))

    a, b = coords[0]
    for x, y in coords[1:]:
        dx = -1 if a > x else 1
        for X in range(a, x + dx, dx):
            walls.add((X, y))
            abyss[X] = max(y, abyss[X]) if X in abyss else y
            lowest_y = max(lowest_y, y)

        dy = -1 if b > y else 1
        for Y in range(b, y + dy, dy):
            walls.add((x, Y))
            abyss[X] = max(y, abyss[X]) if X in abyss else y
            lowest_y = max(lowest_y, y)

        a, b = x, y

sands = set()
print("INITIAL")
for Y in range(170):
    print(f"{Y:>3}", end=" ")
    for X in range(470, 560):
        if (X, Y) in walls:
            print("🔲", end="")
        elif (X, Y) in sands:
            print("🔳", end="")
        else:
            print("⬛", end="")
    print()


sand_unit = 0
sand_x, sand_y = 500, 0
while True:

    # (not PART_1 and sand_y < lowest_y)
    if not PART_1:
        if (
            (sand_x, sand_y + 1) not in walls
            and (sand_x, sand_y + 1) not in sands
            and sand_y < lowest_y + 1
        ):
            # print("Sand Down")
            sand_y += 1
        elif (
            (sand_x - 1, sand_y + 1) not in walls
            and (
                sand_x - 1,
                sand_y + 1,
            )
            not in sands
            and sand_y < lowest_y + 1
        ):
            # print("Sand Left")
            sand_x -= 1
            sand_y += 1
        elif (
            (sand_x + 1, sand_y + 1) not in walls
            and (
                sand_x + 1,
                sand_y + 1,
            )
            not in sands
            and sand_y < lowest_y + 1
        ):
            # print("Sand Right")
            sand_x += 1
            sand_y += 1
        else:
            # print("Sand Stop!")
            sand_unit += 1
            print(f"{sand_unit:>10} - {sand_x:>3}, {sand_y:>3}")
            sands.add((sand_x, sand_y))

            if (sand_x, sand_y) == (500, 0):
                print("Safe standing spot created!")
                break

            sand_x, sand_y = 500, 0

            # for Y in range(150):
            #     print(f"{Y:>3}", end=" ")
            #     for X in range(450, 550):
            #         if (X, Y) in walls:
            #             print("🔲", end="")
            #         elif (X, Y) in sands:
            #             print("🔳", end="")
            #         else:
            #             print("⬛", end="")
            #     print()

    elif PART_1:
        if sand_x not in abyss:
            print("MADE IN ABYSS")
            break
        elif abyss[sand_x] < sand_y:
            print("MADE IN ABYSS 2")
            break
        elif (sand_x, sand_y + 1) not in walls and (sand_x, sand_y + 1) not in sands:
            print("Sand Down")
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in walls and (
            sand_x - 1,
            sand_y + 1,
        ) not in sands:
            print("Sand Left")
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in walls and (
            sand_x + 1,
            sand_y + 1,
        ) not in sands:
            print("Sand Right")
            sand_x += 1
            sand_y += 1
        else:
            print("Sand Stop!")
            print("New sand unit:", sand_x, sand_y)
            sands.add((sand_x, sand_y))
            sand_x, sand_y = 500, 0

            # for Y in range(150):
            #     print(f"{Y:>3}", end=" ")
            #     for X in range(450, 550):
            #         if (X, Y) in walls:
            #             print("🔲", end="")
            #         elif (X, Y) in sands:
            #             print("🔳", end="")
            #         else:
            #             print("⬛", end="")
            #     print()

            sand_unit += 1
            print("total sand unit:", sand_unit)

print("PART 1:", sand_unit)  # 655

for Y in range(170):
    print(f"{Y:>3}", end=" ")
    for X in range(470, 560):
        if (X, Y) in walls:
            print("🔲", end="")
        elif (X, Y) in sands:
            print("🔳", end="")
        else:
            print("⬛", end="")
    print()
