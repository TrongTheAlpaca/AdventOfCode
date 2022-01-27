import sys

# PREAMBLE
with open("input") as f:
    crabs_input = [int(n) for n in f.read().split(',')]
    crabs = [0] * (max(crabs_input) + 1)
    for crab in crabs_input:
        crabs[crab] += 1


def calculate_minimum_fuel_usage(_crabs, exponential_cost: bool):
    optimal_fuel_usage = sys.maxsize
    for destination in range(len(_crabs)):
        total_fuel = 0
        for source in range(len(_crabs)):
            distance = (destination - source) if destination > source else (source - destination)
            cost_per_crab = distance if not exponential_cost else distance * (1 + distance) // 2
            total_fuel += _crabs[source] * cost_per_crab

        if optimal_fuel_usage > total_fuel:
            optimal_fuel_usage = total_fuel

    return optimal_fuel_usage


# CONCLUSION
print(calculate_minimum_fuel_usage(crabs, False))  # PART 1:   347449 is CORRECT
print(calculate_minimum_fuel_usage(crabs, True))   # PART 2: 98039527 is CORRECT
