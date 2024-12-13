with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def report_is_safe(report: list[str]) -> bool:
    for i in range(len(report) - 1):
        prev, current = report[i : i + 2]
        x = current - prev if report[0] < report[1] else prev - current
        if not (1 <= x <= 3):
            return False

    return True


n_safe_reports_1, n_safe_reports_2 = 0, 0
for idx, line in enumerate(lines):
    levels = list(map(int, line.split()))

    is_safe_1 = report_is_safe(levels)

    versions = [levels[:i] + levels[i + 1 :] for i in range(len(levels))]
    is_safe_2 = any([report_is_safe(version) for version in versions])

    n_safe_reports_1 += int(is_safe_1)
    n_safe_reports_2 += int(is_safe_2)

print("Part 1:", n_safe_reports_1)
print("Part 2:", n_safe_reports_2)
