# 100 people at a party, 90 speak Italian, 80 speak Spanish and 75 Mandarin.
# What's the least number of people that speak all three....
#
# I imagine it should be a 'simple' maths/Venn type solution, but i'm going to try a brute force approach

from random import choice
import sys


class PartyGoer:
    it = False
    sp = False
    ma = False

    def __init__(self):
        it = False
        sp = False
        ma = False

    def set_language(self, language):
        if 'italian' == language:
            self.it = True
        elif 'spanish' == language:
            self.sp = True
        elif 'mandarin' == language:
            self.ma = True

    def has_language(self, language):
        if 'italian' == language and self.it:
            return True
        elif 'spanish' == language and self.sp:
            return True
        elif 'mandarin' == language and self.ma:
            return True
        else:
            return False

    @property
    def has_all_three(self):
        return self.it and self.sp and self.ma

    @property
    def has_none(self):
        return (not self.it and not self.sp and not self.ma)

    def show(self):
        print('Italian: {0} Spanish: {1} Mandarin: {2}'.format(self.it, self.sp, self.ma))


def set_random_language(language, max_speakers):
    speakers = 0
    while speakers < max_speakers:
        p = choice(people)
        if not p.has_language(language):
            p.set_language(language)
            speakers += 1

max_attempt = 1e4
if len(sys.argv) > 1:
    max_attempt=int(sys.argv[1])

best = 100
for attempt in range(0, max_attempt):
    people = []
    for x in range(0, 99):
        people.append(PartyGoer())

    set_random_language('mandarin', 75)
    set_random_language('italian', 90)
    set_random_language('spanish', 80)

    stats = {'spanish': 0, 'italian': 0, 'mandarin': 0}
    all_three = 0
    none = 0
    for x in range(0, 99):
        for stat in stats:
            if people[x].has_language(stat):
                stats[stat] += 1
        # people[x].show()
        if people[x].has_all_three:
            all_three += 1
        if people[x].has_none:
            none += 1

    if none == 0 and all_three < best:
        best = all_three
    #print('# with all three {0} - best {1}'.format(all_three, best))
    # for stat in stats:
    # print('{0} has {1}'.format(stat, stats[stat]))
print(best)
