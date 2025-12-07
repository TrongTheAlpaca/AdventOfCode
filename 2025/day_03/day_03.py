with open("input.txt", "r") as f:
    lines = [line for line in f.read().splitlines()]

totals = [0, 0]

for part, size in enumerate([2, 12]):
    for line in lines:
        batteries = line[0:size]

        for i in range(size, len(line)):
            current_battery = line[i]
            current_value = int(batteries)
            batteries += current_battery
            for n in range(size):
                new_batteries = batteries[0:n] + batteries[n + 1 :]
                if current_value <= int(new_batteries):
                    batteries = new_batteries
            batteries = batteries[0:size]  # Remove extra digit

        totals[part] += int(batteries)

print("Part 1:", totals[0])  # 17430
print("Part 2:", totals[1])  # 171975854269367
