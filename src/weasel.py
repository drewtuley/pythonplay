import random
import string

target = 'methinks it is like a weasel'
genes = string.ascii_lowercase + ' '
CHANCE = 20
CHILDREN = 100


def calculate_difference(s1, s2):
    idx = 0
    dx = 0
    while idx < len(s1):
        if ord(s1[idx]) == ord(s2[idx]):
            dx += 1
        idx += 1
    return dx


def find_closest_match(candidates):
    best_diff = None
    selection = ''
    for c in candidates:
        diff = calculate_difference(target, c)
        if best_diff is None or diff > best_diff:
            best_diff = diff
            selection = c
    return selection


start = ''.join(random.choice(genes) for _ in range(len(target)))
generation = 1
while start != target:
    print('{0:-4d} {1}'.format(generation, start))
    offspring = []
    for child in range(CHILDREN):
        _child = []
        for c in start:
            if 1 == random.randint(1, CHANCE):
                ch = random.choice(genes)
            else:
                ch = c
            _child.append(ch)
        offspring.append(''.join(_child))

    generation += 1

    start = find_closest_match(offspring)
print('{0:-4d} {1}'.format(generation, start))
