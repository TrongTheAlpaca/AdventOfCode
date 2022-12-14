from functools import cmp_to_key
import copy


def compare(left, right):
    stack_x = list(reversed(copy.deepcopy(left)))
    stack_y = list(reversed(copy.deepcopy(right)))

    while stack_x and stack_y:
        x = stack_x.pop()
        y = stack_y.pop()
        print("x:", x)
        print("y:", y)

        if isinstance(x, int):
            x = [x]
        if isinstance(y, int):
            y = [y]

        if y == [] and x == []:
            continue
        if y != [] and x == []:
            return True
        if y == [] and x != []:
            return False

        if isinstance(x, list) and isinstance(y, list):
            i = 0
            while i < len(x) and i < len(y):
                if isinstance(x[i], int) and isinstance(y[i], int):
                    if x[i] < y[i]:
                        return True
                    if x[i] > y[i]:
                        return False
                    if x[i] == y[i]:
                        i += 1
                else:
                    while x[i:]:
                        stack_x.append(x.pop())
                    while y[i:]:
                        stack_y.append(y.pop())
                    break

            else:
                if len(x) < len(y):
                    print("CORRECT: X is smaller than Y")
                    return True
                elif len(x) > len(y):
                    print("WRONG: X is bigger than Y")
                    return False
                else:
                    print("UNKNOWN: X and Y same size, proceed")
                    pass

    else:
        if len(stack_x) < len(stack_y):
            print("CORRECT: X is smaller than Y")
            return True
        elif len(stack_x) > len(stack_y):
            print("WRONG: X is bigger than Y")
            return False
        else:
            print("IMPOSSIBLE STAGE?")
            return 0


with open("input.txt") as f:
    packet_groups = [eval(l) for l in f.read().replace("\n\n", "\n").splitlines()]

# PART 1
correct_indices = []
for gid, (X, Y) in enumerate(zip(packet_groups[0::2], packet_groups[1::2])):
    if compare(X, Y):
        correct_indices.append(gid + 1)
print("PART 1:", sum(correct_indices))  # 6235

# PART 2
packets_p2 = packet_groups + [[[2]]] + [[[6]]]
packets_p2.sort(key=cmp_to_key(lambda x, y: -compare(x, y)))
print("PART 2:", (packets_p2.index([[2]]) + 1) * (packets_p2.index([[6]]) + 1))  # 22866
