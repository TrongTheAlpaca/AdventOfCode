from timeit import default_timer as timer


def invert_MUL(a, b, result):
    if b.isnumeric() and int(b) == 0:
        return result.replace(str(a), '0')
    else:
        return result.replace(str(a), f"({a} * {b})")


def invert_ADD(a, b, result):
    return result.replace(str(a), f"({a} + {b})")


def invert_DIV(a, b, result):
    return result.replace(str(a), f"({a} / {b})")


def invert_MOD(a, b, result):
    return result.replace(str(a), f"({a} % {b})")


def invert_EQL(a, b, result):
    return result.replace(str(a), f"(1 if ({a} == {b}) else 0)")


def process_new(_statements):
    resulting_strings = "z"  # This works as long as last statement contains 'z'
    for statement in reversed(_statements):
        match statement[0]:
            case 'add':
                a, b = statement[1:]
                resulting_strings = invert_ADD(a, b, resulting_strings)
            case 'mul':
                a, b = statement[1:]
                resulting_strings = invert_MUL(a, b, resulting_strings)
            case 'div':
                a, b = statement[1:]
                resulting_strings = invert_DIV(a, b, resulting_strings)
            case 'mod':
                a, b = statement[1:]
                resulting_strings = invert_MOD(a, b, resulting_strings)
            case 'eql':
                a, b = statement[1:]
                resulting_strings = invert_EQL(a, b, resulting_strings)
            case _:
                raise ProcessLookupError

    return resulting_strings


def textual_to_functions(statements):
    formulae = [process_new(statement) for statement in statements]
    return [eval(f"lambda w, z: int({formula})") for formula in formulae]


if __name__ == '__main__':
    with open("input", 'r') as f:
        statements = f.read().split('inp w\n')[1:]
        statements = [c.split('\n') for c in statements]
        statements = [[x.split(' ') for x in c] for c in statements]
        statements[-1].append([''])
        statements = [s[:-1] for s in statements]

    funcs = textual_to_functions(statements)

    bad_z_depth = set()

    def calculate(ws='', z=0, depth=0):
        if (depth, z) in bad_z_depth:
            return False

        if depth == 14:
            if z == 0:
                print('CORRECT:', ws)
                return ws
            return False

        z_backup = z
        for w in range(1, 10, 1):
            z = funcs[depth](w, z_backup)
            result = calculate(ws + str(w), z, depth+1)
            if result:
                return

        bad_z_depth.add((depth, z_backup))

    start = timer()
    calculate()
    end = timer()
    print(end - start)

# PART 1: 91599994399395
# PART 2: 71111591176151
# 734.8620453000003 seconds
