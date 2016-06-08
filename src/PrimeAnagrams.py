import math
import string
import functools
import operator


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
                        words = list()
                        words.append(word)
                    anaprimes_rev[prime] = words
        except UnicodeDecodeError as err:
            # print('error {} '.format(err))
            pass
        else:
            complete = True
print('Processed {} anaprimes'.format(len(anaprimes)))

# print(anaprimes['enumerations'])
# print(anaprimes['mountaineers'])
# print(len(anaprimes_rev))
# print(anaprimes_rev[anaprimes['mountaineers']])
# for prime in anaprimes_rev:
#     if len(anaprimes_rev[prime]) > 1:
#         print('Prime:{} anagrams={}'.format(prime, anaprimes_rev[prime]))

if -1 in anaprimes_rev:
    anaprimes_rev.pop(-1)
sorted_keys = list(anaprimes_rev.keys())
sorted_keys.sort()

source = ['andrew', 'tuley']
product = 1
for word in source:
    try:
        pval = anaprimes[word]
    except:
        pval = calc_pval(word)
    product *= pval

print('product for {} is {}'.format(source, product))
# for x in sorted_keys:
#     if x>40000:
#         break
#     print('key={} words={}'.format(x, anaprimes_rev[x]))

try:
    anagrams = anaprimes_rev[product]
    print('single word anagrams={}'.format(anagrams))
except:
    print('no single word anagrams')


def inc_indexes(indices, index, index_count, max_index, product, sorted_keys):
    if index == index_count - 1:
        prod = 1
        for x in indices[:-1]:
            prod *= sorted_keys[x]

        if product % prod == 0:
            my_start_idx = int(product / prod)
            if my_start_idx not in sorted_keys:
                return
            my_start = sorted_keys.index(my_start_idx)
            if my_start <= indices[index - 1]:
                return
        else:
            return
    elif index - 1 >= 0:
        my_start = indices[index - 1] + 1
    else:
        my_start = 0

    if index < index_count - 1 and my_start >= max_index:
        return

    indices[index] = my_start
    while indices[index] < max_index:
        if index + 1 < index_count:
            yield from (inc_indexes(indices, index + 1, index_count, max_index, product, sorted_keys))
        else:
            if indices[index_count - 2] != indices[index_count - 1]:
                yield (indices)
        if index == index_count - 1:
            break
        else:
            indices[index] += 1


print(len(anaprimes_rev))
indices = [0 for x in range(3)]
for idxs in inc_indexes(indices, 0, len(indices), len(anaprimes_rev), product, sorted_keys):
    words = ''
    for idx in idxs:
        factor = sorted_keys[idx]
        words = '{} w:{}[{}]'.format(words, anaprimes_rev[factor], factor)
    print(words)
