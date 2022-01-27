# PREAMBLE
with open("input") as f:
    cases = [line for line in f.read().split('\n')]


scoring_table = {
    ')': (    3, 1),
    ']': (   57, 2),
    '}': ( 1197, 3),
    '>': (25137, 4)
}

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


total_score = 0
total_autocomplete_score = []
for case in cases:
    left_stack = []
    corrupted = False
    for char in case:
        if char in ['{', '(', '[', '<']:
            left_stack.append(char)
        else:
            if pairs[char] != left_stack.pop():
                total_score += scoring_table[char][0]
                corrupted = True
                break

    if corrupted:
        continue

    missing_parts = list(map(lambda x: pairs[x], reversed(left_stack)))
    autocomplete_score = 0
    for char in missing_parts:
        autocomplete_score = autocomplete_score * 5 + scoring_table[char][1]
    total_autocomplete_score.append(autocomplete_score)

print(total_score)  # PART 1:  339477 is Correct
print(sorted(total_autocomplete_score)[len(total_autocomplete_score) // 2])  # PART 2:  3049320156 is Correct!
