# PREAMBLE
light_pixels = set()
with open("input", "r") as f:
    algorithm, image = f.read().split('\n\n')
    image = image.split('\n')
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == '#':
                light_pixels.add((x, y))

print(f"Image Dimensions: {len(image[0])}x{len(image)}")


def calc_next_pixel(pixels, x, y):
    delta = ((-1, -1), (0, -1), (1, -1),
             (-1,  0), (0,  0), (1,  0),
             (-1,  1), (0,  1), (1,  1))

    binary = ''.join(['1' if (x + dx, y + dy) in pixels else '0' for dx, dy in delta])
    decimal = int(binary, 2)

    return algorithm[decimal] == '#'


def print_image(pixels, x0, y0, x1, y1):
    print()
    for y in range(y0, y1):
        for x in range(x0, x1):
            print('#' if (x, y) in pixels else '.', end='')
        print()


def update_pixels(pixels: set[tuple[int, int]], x0, y0, x1, y1):
    temp_set = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            result = calc_next_pixel(pixels, x, y)
            if result:
                temp_set.add((x, y))

    return temp_set


border_offset = 100  # Limits infinity
for i in range(1, 51):
    light_pixels = update_pixels(light_pixels, -border_offset, -border_offset, len(image) + border_offset, len(image) + border_offset)
    print_image(light_pixels, -i, -i, len(image) + i + 2, len(image) + i + 2)
    offset = i + 1
    temp_filter = set(
        filter(lambda x: -offset < x[0] < len(image) + offset and -offset < x[1] < len(image) + offset, light_pixels))
    print(f"{i:>2}: No. of Light Pixels: {len(temp_filter):>5}")  # PART 1: 5432 - PART 2: 16016
