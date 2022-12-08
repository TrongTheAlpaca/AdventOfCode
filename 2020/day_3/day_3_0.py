def navigate_forest(layers, x_strides, y_strides):

    tree_counts = []

    for i in range(len(x_strides)):

        tree_count = 0

        x = x_strides[i]
        y = y_strides[i]

        while y < len(layers):

            if x >= len(layers[0]):  # X-axis: Out of bounds!
                layers = [layer + layer for layer in layers]  # Double forest-length

            current_pos = layers[y][x]
            if current_pos == '#':  # Hit tree
                tree_count += 1

            x += x_strides[i]
            y += y_strides[i]

        tree_counts.append(tree_count)

    # Multiply all tree encounters
    tree_product = 1
    for count in tree_counts:
        tree_product *= count

    return tree_product


if __name__ == '__main__':
    with open('test/puzzle_input.txt') as f:
        values = f.read().splitlines()

    lines = [x for x in values]

    part_1 = navigate_forest(lines, [3], [1])
    part_2 = navigate_forest(lines, [1, 3, 5, 7, 1], [1, 1, 1, 1, 2])

    print(part_1)  # Part 1: 232 is correct!
    print(part_2)  # Part 2: 3952291680 is correct!
