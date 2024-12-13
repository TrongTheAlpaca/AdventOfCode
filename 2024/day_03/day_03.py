import re

with open("input.txt", "r") as f:
    string = f.read()

operations = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", string)

total_1 = 0
total_2 = 0
dont = False
for operation in operations:
    if operation == "do()":
        dont = False
    elif operation == "don't()":
        dont = True

    if operation.startswith("mul("):
        x, y = map(int, operation.removeprefix("mul(").removesuffix(")").split(","))
        total_1 += x * y
        if not dont:
            total_2 += x * y

print("part 1:", total_1)  # 175700056
print("part 2:", total_2)  # 71668682
