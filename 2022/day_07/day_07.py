with open("input.txt") as f:
    all_lines = f.read().splitlines()

ROOT_DIRECTORY = ""

content_map: dict[str, list[str]] = dict()
file_sizes: dict[str, int] = dict()
dir_sizes: dict[str, int] = dict()

current_folder: str = ROOT_DIRECTORY
parent_folders: list[str] = []

lines = iter(all_lines)
line = next(lines, None)
while line != None:

    if line.startswith("$ cd"):
        if line == "$ cd ..":
            current_folder = parent_folders.pop()
        elif line == "$ cd /":
            current_folder = ROOT_DIRECTORY
            parent_folders = []
        else:
            parent_folders.append(current_folder)
            current_folder = line.split(" ")[-1]

        line = next(lines, None)

    elif line == "$ ls":
        content = []
        while True:
            path = "/".join(parent_folders + [current_folder])
            line = next(lines, None)
            if line is None:
                break
            elif line.startswith("$"):
                break
            elif line.startswith("dir"):
                content.append("DIR " + path + "/" + line.removeprefix("dir "))
            else:
                size, filename = line.split(" ")
                total_path = path + "/" + filename
                file_sizes[total_path] = int(size)
                content.append(total_path)

        content_map["DIR " + path] = content


def try_calc_size(blob):
    if blob in dir_sizes:
        return dir_sizes[blob]
    elif blob in file_sizes:
        return file_sizes[blob]
    else:
        return None


while True:
    for name, content in content_map.items():
        if name in dir_sizes:
            continue

        trial = [try_calc_size(c) for c in content]
        if all(isinstance(x, int) for x in trial):
            dir_sizes[name] = sum(trial)

    if len(dir_sizes.keys()) == len(content_map.keys()):
        break

small_directories = [size for size in dir_sizes.values() if size <= 100_000]
print("PART 1:", sum(small_directories))  # 1118405


target = 30_000_000 - (70_000_000 - dir_sizes[f"DIR {ROOT_DIRECTORY}"])
relevant_directories = filter(lambda x: x >= target, dir_sizes.values())
print("PART 2:", min(relevant_directories))  # 12545514
