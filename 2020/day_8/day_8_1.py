with open('test/puzzle_input.txt') as f:
    original_instructions = f.read().splitlines()

# PART 1
accumulator = 0
pointer = 0
visited_addresses = set()
while 0 <= pointer < len(original_instructions):
    operation, argument = original_instructions[pointer].split(' ')
    argument = int(argument)

    if pointer not in visited_addresses:
        visited_addresses.add(pointer)
    else:
        break

    if operation == 'nop':
        pointer += 1

    elif operation == 'acc':
        accumulator += argument
        pointer += 1

    elif operation == 'jmp':
        pointer += argument


print("PART 1:", accumulator)  # PART 1: 1816

# PART 2
# Retrieve all possible corrupted addresses
corrupted_addresses = []
for i in range(len(original_instructions)):
    operation, _ = original_instructions[i].split(' ')
    if operation == 'nop' or operation == 'jmp':
        corrupted_addresses.append(i)

for corrupted in corrupted_addresses:

    # Add corruption
    instructions = original_instructions.copy()
    operation, argument = instructions[corrupted].split(' ')
    operation = 'jmp' if operation == 'nop' else 'nop'
    instructions[corrupted] = f'{operation} {argument}'

    # Reset values
    flag = False
    pointer = 0
    accumulator = 0
    visited_addresses = set()

    # Execute instructions
    while 0 <= pointer < len(instructions):

        if pointer not in visited_addresses:
            visited_addresses.add(pointer)
        else:
            flag = True  # Duplicated Detected!
            break

        operation, argument = instructions[pointer].split(' ')
        argument = int(argument)

        if operation == 'nop':
            pointer += 1

        elif operation == 'acc':
            accumulator += argument
            pointer += 1

        elif operation == 'jmp':
            pointer += argument

    if not flag:
        print("PART 2:", accumulator)  # PART 2: 1149
        break
