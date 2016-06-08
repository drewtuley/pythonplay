import math
import string
from itertools import combinations
from functools import reduce
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
            #print('Trouble with: {} in {} because {}'.format(l, str, ex))
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
            print('error {} '.format(err))
            pass
        else:
            complete = True
print('Processed {} anaprimes'.format(len(anaprimes)))


if -1 in anaprimes_rev:
    anaprimes_rev.pop(-1)
sorted_keys = list(anaprimes_rev.keys())
sorted_keys.sort()

source = ['treasure']
product = 1
for word in [s.strip().lower() for s in source]:
    try:
        pval = anaprimes[word]
    except:
        pval = calc_pval(word)
    product *= pval

print('product for {} is {}'.format(source, product))

try:
    anagrams = anaprimes_rev[product]
    print('single word anagrams={}'.format(anagrams))
except:
    print('no single word anagrams')


matching_prime_products = list()
for k in sorted_keys:
    if product % k == 0:
        matching_prime_products.append(k)

print('Found {} matching prime products'.format(len(matching_prime_products)))

for r in combinations(matching_prime_products, 2):
    if reduce(operator.mul, r, 1) == product:
        words = ''
        for factor in r:
            words = '{} w:{}[{}]'.format(words, anaprimes_rev[factor], factor)
        print(words)

