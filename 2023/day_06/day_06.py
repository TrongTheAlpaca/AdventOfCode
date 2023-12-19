import math


def calc_number_solutions(time: int, distance: int) -> int:
    # Quadratic formula
    a = -1
    b = time
    c = -distance

    d = (b**2) - (4 * a * c)
    left = (-b + math.sqrt(d)) / (2 * a)
    right = (-b - math.sqrt(d)) / (2 * a)

    min_time = math.floor(left) + 1
    max_time = math.ceil(right) - 1

    return max_time - min_time + 1


with open("input.txt") as f:
    lines = f.read().splitlines()

times = map(int, lines[0].split(":")[1].strip().split())
distances = map(int, lines[1].split(":")[1].strip().split())

time_2 = int(lines[0].split(":")[1].replace(" ", ""))
distance_2 = int(lines[1].split(":")[1].replace(" ", ""))


n_solutions_product = 1
for time, distance in zip(times, distances):
    n_solutions_product *= calc_number_solutions(time, distance)

print("part 1:", n_solutions_product)  # 316800
print("part 2:", calc_number_solutions(time_2, distance_2))  # 45647654
