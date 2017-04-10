from random import sample

italian = 1
spanish = 2
mandarin = 4
all = italian | spanish | mandarin


def set_random_language(pop, language, speakers):
    samp = sample(pop, speakers)
    for v in samp:
        t = (v[0], v[1] | language)
        people[v[0]] = t


best = 100
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
        elif p[1] == all:
            all_three += 1
    if none == 0 and all_three < best:
        best = all_three
    if best == 45:
        print('Found on attempt ', attempt)
        exit(1)
        # print(all_three, none)
print(best)
