import operator

IS_PART_1 = False
DEBUG = False


def print_monkeys(ms: list):
    for i, m in enumerate(ms):
        print(f"monkey {i}:", m)
    print()


with open("input.txt") as f:
    monkeys = [l.split("\n") for l in f.read().split("\n\n")]

OPERATOR_MAP = {
    "+": operator.add,
    "*": operator.mul,
}

n_inspected = [0 for _ in range(len(monkeys))]
monkey_items = []
monkey_operation = []
monkey_test = []

for monkey in monkeys:
    monkey_items.append(
        list(map(int, monkey[1].removeprefix("  Starting items: ").split(", ")))
    )

    v = monkey[2].removeprefix("  Operation: new = old ")
    operator, value = v.split(" ")[:2]
    monkey_operation.append((OPERATOR_MAP[operator], value))

    predicate = int(monkey[3].removeprefix("  Test: divisible by "))
    if_true = int(monkey[4].removeprefix("    If true: throw to monkey "))
    if_false = int(monkey[5].removeprefix("    If false: throw to monkey "))
    test = (predicate, if_true, if_false)
    monkey_test.append(test)

mod = 1
for div, _, _ in monkey_test:
    mod *= div

for epoch in range(20 if IS_PART_1 else 10_000):

    for idx, (items, op, test) in enumerate(
        zip(monkey_items, monkey_operation, monkey_test)
    ):

        if DEBUG:
            print(f"BEFORE monkey {idx}:")
            print_monkeys(monkey_items)

        n_inspected[idx] += len(monkey_items[idx])

        while items := monkey_items[idx]:
            item = items.pop(0)
            if op[1] != "old":
                item = op[0](item, int(op[1]))
            else:
                item *= item

            if IS_PART_1:
                item = item // 3  # Stress relief
            else:
                item = item % mod

            receiver = test[1] if item % test[0] == 0 else test[2]

            if DEBUG:
                print(f"Give {item} to monkey {receiver}")

            monkey_items[receiver].append(item)

        if DEBUG:
            print(f"\nAFTER monkey {idx}:")
            print_monkeys(monkey_items)
            print()

    print(f"END EPOCH {epoch}:")


print("\nCONCLUSION:")
print_monkeys(n_inspected)
s = sorted(n_inspected, reverse=True)
print("ANSWER", s[0] * s[1])
# PART 1:       62491
# PART 2: 17408399184
