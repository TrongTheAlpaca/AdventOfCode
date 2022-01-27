from collections import Counter

# PREAMBLE
with open("input") as f:
    lines = f.read().split('\n')
    state = lines[0]
    rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in lines[2:]}


def split_into_pairs(seq):
    return [seq[i:i + 2] for i in range(len(seq) - 1)]


counts = Counter(split_into_pairs(state))  # NN:1, NC:1, CB:1
for step in range(40):
    letter_count = Counter((state[0], state[-1]))  # Include first and last element to correctly offset
    temp_count = Counter()
    for pair, count in counts.items():
        inserted = pair[0] + rules[pair] + pair[1]  # NCN
        for p in split_into_pairs(inserted):  # NCN => NC, CN:
            temp_count[p] += count
            letter_count[p[0]] += count
            letter_count[p[1]] += count

    counts = temp_count

    # Fix over-counting
    for k in letter_count:
        letter_count[k] //= 2

    print('Step {:>2}: {:>15}'.format(step + 1, letter_count.most_common()[0][1] - letter_count.most_common()[-1][1]))
