with open('test/puzzle_input.txt') as f:
    rules_lines = f.read().splitlines()

# test_0 =  32
# test_1 = 126

rules = {}
for rule in rules_lines:
    outer, inners = rule.replace('.', '').split(' bags contain ')
    inners = [x.replace(' bags', '').replace(' bag', '').split(' ', 1) for x in inners.split(', ')]
    inners = [(int(x[0]) if x[0].isdigit() else 0, x[1]) for x in inners]
    rules[outer] = inners


total_count = 0
current_node = 'shiny gold'
current_list = rules[current_node]

while len(current_list) > 0:

    c, current_node = current_list.pop()

    if current_node == 'other':
        continue

    total_count += c

    c_list = rules[current_node]

    cc = [(x[0] * c, x[1]) for x in c_list]

    current_list.extend(cc)

print(total_count)  # Part 2: 9569
