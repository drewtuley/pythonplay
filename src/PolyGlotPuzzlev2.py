# 100 people at a party, 90 speak Italian, 80 speak Spanish and 75 Mandarin.
# What's the least number of people that speak all three....
#
# I imagine it should be a 'simple' maths/Venn type solution, but i'm going to try a brute force approach
# by randomly assigning each of the 3 languages to the correct proportions.

import random
import sys

italian = 1
spanish = 1 << 1
mandarin = 1 << 2
all_languages = italian | spanish | mandarin


def set_random_language(pop, language, speakers):
    for v in random.sample(pop, speakers):
        t = (v[0], v[1] | language)
        people[v[0]] = t


best = 100
max_attempts = 1000000
if len(sys.argv) > 1:
    max_attempts = int(sys.argv[1])

for attempt in range(1000000):
    people = [(_, 0) for _ in range(100)]
    set_random_language(people, italian, 90)
    set_random_language(people, spanish, 80)
    set_random_language(people, mandarin, 75)

    all_three = 0
    none = 0
    for p in people:
        if p[1] == 0:
            none += 1
        elif p[1] == all_languages:
            all_three += 1
    if none == 0 and all_three < best:
        best = all_three
    if best == 45:
        print('Found on attempt {0}'.format(attempt))
        exit(1)
        # print(all_three, none)
print(best)
