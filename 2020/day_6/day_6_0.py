with open('test/puzzle_input.txt') as f:
    groups = [x.split('\n') for x in f.read().split('\n\n')]

# Part 1
total_yes = 0
for group in groups:
    n_yes = 0
    answered = set()  # Contains letters that has been answered by current group
    for person in group:
        for question in person:
            if question not in answered:
                answered.add(question)
                n_yes += 1

    total_yes += n_yes

print(total_yes)  # PART 1: 6763


# Part 2
total_common_yes = 0
for group in groups:
    common_yes = set.intersection(*[set(x) for x in group])
    total_common_yes += len(common_yes)

print(total_common_yes)  # PART 2: 3512
