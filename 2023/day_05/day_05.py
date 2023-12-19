with open("input.txt") as f:
    lines = f.read().split("\n\n")

seeds = list(map(int, lines[0].split(": ")[1].split()))

all_guides: list[tuple[int, int, int]] = []
guides = list(map(lambda x: x.split(":\n")[1].split("\n"), lines[1:]))

for guide_idx, guide in enumerate(guides):
    all_guides.append([])
    for entry in guide:
        destination, source, range_length = map(int, entry.split())

        all_guides[guide_idx].append((destination, source, range_length))

    all_guides[guide_idx].sort(key=lambda x: x[1])


all_locations = []
for seed in seeds:
    current_destination = seed
    for guide in all_guides:
        for destination, source, range_length in guide:
            if source <= current_destination < source + range_length:
                current_destination = destination + current_destination - source
                break

    all_locations.append(current_destination)


print("part 1:", min(all_locations))  # 282277027


min_location = float("inf")
for seed in zip(seeds[::2], seeds[1::2]):
    # print("Current seed:", seed)
    init_start_seed, init_end_seed = seed[0], seed[0] + seed[1] - 1
    # print("Current seed range:", (init_start_seed, init_end_seed))

    next_stack = [(init_start_seed, init_end_seed)]
    current_stack = None
    for guide in all_guides:
        current_stack = next_stack
        next_stack = []
        # print("current guide:", guide)
        while current_stack:
            start_seed, end_seed = current_stack.pop()

            min_soil, max_soil = min(guide, key=lambda x: x[1]), max(
                guide, key=lambda x: x[1] + x[2] - 1
            )
            min_soil = min_soil[1]
            max_soil = max_soil[1] + max_soil[2] - 1

            # Whole A is before B
            if end_seed < min_soil:
                next_stack.append((start_seed, end_seed))
                continue
            # Whole A is after B
            if start_seed > max_soil:
                next_stack.append((start_seed, end_seed))
                continue

            # A begins before B but terminates in B
            if start_seed < min_soil and end_seed < max_soil:
                next_stack.append((start_seed, min_soil - 1))
                start_seed = min_soil

            # A is inside B but terminates outside B
            if end_seed > max_soil and start_seed > min_soil:
                next_stack.append((max_soil + 1, end_seed))
                end_seed = max_soil

            for destination, source, range_length in guide:
                # whole A is after B
                if source + range_length < start_seed:
                    continue
                # A is fully within B
                elif (
                    source <= start_seed < source + range_length
                    and source <= end_seed < source + range_length
                ):
                    difference = end_seed - start_seed
                    new_start_seed = start_seed - source + destination
                    new_end_seed = new_start_seed + difference
                    next_stack.append((new_start_seed, new_end_seed))
                    break

                # A is within and also after B
                else:
                    difference = source + range_length - start_seed
                    new_start_seed = start_seed - source + destination
                    new_end_seed = new_start_seed + difference
                    next_stack.append((new_start_seed, new_end_seed))

                    start_seed = start_seed + difference

    current_seed_min_location = min(next_stack, key=lambda x: x[0])
    min_location = min(current_seed_min_location[0], min_location)

print("part 2:", min_location)  # 11554135
