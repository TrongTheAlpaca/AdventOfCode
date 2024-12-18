import re

with open("input.txt", "r") as f:
    registers, program = f.read().split("\n\n")
    A, _, _ = map(int, re.findall(r"\d+", registers))
    program = list(map(int, program.removeprefix("Program: ").split(",")))


def run_program(a: int) -> list[int]:

    A = a
    B = 0
    C = 0

    def get_combo_operand(code):
        if 0 <= code <= 3:
            return code
        elif code == 4:
            return A
        elif code == 5:
            return B
        elif code == 6:
            return C
        elif code == 7:
            raise ("CODE 7 FOUND, BREAK!")

    pointer = 0
    outputs = []

    while True:

        if pointer >= len(program):
            break

        opcode, operand = program[pointer : pointer + 2]

        if opcode == 0:
            A = A // (2 ** get_combo_operand(operand))
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = get_combo_operand(operand) % 8
        elif opcode == 3:
            if A != 0:
                pointer = operand  # Skip default +2 jump
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            outputs.append(get_combo_operand(operand) % 8)
        elif opcode == 6:
            B = A // (2 ** get_combo_operand(operand))
        elif opcode == 7:
            C = A // (2 ** get_combo_operand(operand))

        pointer += 2

    return outputs


print("Part 1:", ",".join(map(str, run_program(A))))  # Part 1: 1,4,6,1,6,4,3,0,3


# PART 2
# NOTE: I think this solution will work for specific inputs only and is therefore imperfect!!!
# I am wondering if a normal binary search is doable here?

addends = [0] * len(program)
addends[0] = 1
current_A = 0
current_adder = 1
current_digit = 1
while True:

    _A = current_A
    outputs = run_program(_A)

    if current_digit == len(program):
        break
    elif not addends[current_digit] and len(outputs) == current_digit + 1:
        addends[current_digit] = current_A
        print(f"#{current_digit + 1}:", current_A)
        current_adder = current_A
        current_digit += 1

    current_A += current_adder


current_digit -= 1
current_A = addends[current_digit]
current_adder = addends[current_digit]
while 0 <= current_digit:
    outputs = run_program(current_A)

    print(f"\rJESUS TAKE THE WHEEL: {current_A}", end="", flush=True)
    print(f"\nFound output: {outputs}", end="", flush=True)
    print(f"\nExpected:     {program}", end="", flush=True)
    print("\033[2A", end="")  # Move the print cursor 2 lines up

    current_output_digit = outputs[current_digit]
    current_program_digit = program[current_digit]
    if (
        current_output_digit != current_program_digit
        or outputs[current_digit:] != program[current_digit:]
    ):
        current_A += current_adder
    else:
        current_digit -= 1
        current_adder = addends[current_digit]

print("\033[2B", end="")  # Reset print cursor
print("\nPart 2:", current_A)  # Part 2: 265061364597659
outputs = run_program(current_A)
