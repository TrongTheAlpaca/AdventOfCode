from pprint import pprint

with open('test/puzzle_input.txt') as f:
    rules_lines = f.read().splitlines()

rules = {}
for rule in rules_lines:
    outer, inners = rule.replace('.', '').split(' bags contain ')
    # inners = [x.rstrip(' bags').rstrip(' bag').split(' ', 1) for x in inners.split(', ')]
    inners = [x.replace(' bags', '').replace(' bag', '').split(' ', 1) for x in inners.split(', ')]
    inners = [(int(x[0]) if x[0].isdigit() else 0, x[1]) for x in inners]
    rules[outer] = inners

pprint(rules)

for color, contents in rules.items():
    temp_list = []
    for content in contents:
        for x in range(content[0]):
            temp_list.append(content[1])
    rules[color] = temp_list


flag = True
while flag:
    flag = False
    for top_color, contents in rules.items():

        if top_color == 'shiny gold':
            continue

        temp_set = set()

        for inner_color in contents:

            if inner_color == 'shiny gold':
                temp_set.add(inner_color)
                continue

            inner_colors = rules[inner_color]

            if len(inner_colors) > 0:
                temp_set.update(inner_colors)
                flag = True

        rules[top_color] = temp_set

# print()
# pprint(rules)

count = 0
for color, contents in rules.items():
    if color == 'shiny gold':
        continue

    if 'shiny gold' in contents:
        count += 1

print(count)  # Part 1: 226
