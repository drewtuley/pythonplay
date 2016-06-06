import math
import string
from bisect import bisect_left


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1)):
        if n != x and n % x == 0:
            return False
    return True


primes = [p for p in range(3, 150) if is_prime(p)]


def calc_pval(str):
    prod = -1
    for l in str:
        try:
            idx = string.ascii_lowercase.index(l)
            pval = primes[idx]
        except Exception as ex:
            # print('Trouble with: {} in {} because {}'.format(l, str, ex))
            pval = 0
        if prod < 0:
            prod = pval
        else:
            prod *= pval
    return prod


anaprimes = {}
anaprimes_rev = {}
with open('words.txt') as fd:
    complete = False
    while not complete:
        try:
            for line in fd:
                word = line.strip()
                prime = calc_pval(word)
                if prime != 0:
                    # print('{} {}'.format(word, prime))
                    anaprimes[word] = prime
                    if prime in anaprimes_rev:
                        words = anaprimes_rev[prime]
                        words.append(word)
                    else:
                        words = []
                        words.append(word)
                    anaprimes_rev[prime] = words
        except UnicodeDecodeError as err:
            # print('error {} '.format(err))
            pass
        else:
            complete = True
print('Processed {} anaprimes'.format(len(anaprimes)))

print(anaprimes['enumerations'])
print(anaprimes['mountaineers'])
print(len(anaprimes_rev))
print(anaprimes_rev[anaprimes['mountaineers']])
# for prime in anaprimes_rev:
#     if len(anaprimes_rev[prime]) > 1:
#         print('Prime:{} anagrams={}'.format(prime, anaprimes_rev[prime]))

anaprimes_rev.pop(-1)
sorted_keys = list(anaprimes_rev.keys())
sorted_keys.sort()

source = ['treasure', 'hunt']
product = 1
for word in source:
    product *= anaprimes[word]

# for x in sorted_keys:
#     if x>40000:
#         break
#     print('key={} words={}'.format(x, anaprimes_rev[x]))

upper_idx = len(sorted_keys)
for w1 in sorted_keys:
    if w1 > product:
        break
    if w1 < 0:
        next

    w2_lower = product / w1
    w2_idx = bisect_left(sorted_keys, w2_lower) - 1
    if w2_idx >= 0 and w2_idx < upper_idx:
        w2 = sorted_keys[w2_idx]
        while (w1 * w2) <= product and w2 < product and w2 >= w1:
            if w2 < w1:
                next
            if (w1 * w2) == product:
                print('w1:{}[{}] w2:{}[{}]'.format(anaprimes_rev[w1], w1, anaprimes_rev[w2], w2))

            w2_idx += 1
            if w2_idx < upper_idx:
                w2 = sorted_keys[w2_idx]
            else:
                break