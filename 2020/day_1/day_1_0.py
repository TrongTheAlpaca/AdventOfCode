with open('day_1/test/puzzle_input.txt') as f:
    values = [int(line) for line in f]

### Part 1
for i_0 in range(len(values)):
    for i_1 in range(i_0 + 1, len(values)):
        s = values[i_0] + values[i_1]
        if s == 2020:
            print(values[i_0] * values[i_1])
            break
 
### Part 2
for i_0 in range(len(values)):
    for i_1 in range(i_0 + 1, len(values)):
        for i_2 in range(i_1 + 1, len(values)):
            s = values[i_0] + values[i_1] + values[i_2]
            if s == 2020:
                print(values[i_0] * values[i_1] * values[i_2])
                break
