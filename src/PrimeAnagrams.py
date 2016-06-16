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
with open('20k.txt') as fd:
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


try:
    anaprimes_rev.pop(-1)
except:
    pass

sorted_keys = list(anaprimes_rev.keys())
sorted_keys.sort()


top_ten = dict()
for key in anaprimes_rev:
    words = anaprimes_rev[key]
    len_words = len(words)
    if len(top_ten) > 0:
        if len_words > max(top_ten.keys()):
            top_ten[len_words] = words
    else:
        top_ten[len_words] = words

    if len(top_ten) > 5:
        min_idx = min(top_ten.keys())
        del top_ten[min_idx]

for count in top_ten:
    print('#{} words:{}'.format(count, top_ten[count]))


source = ['ian', 'malone']


def calculate_total_product(source):
    product = 1
    for word in [s.strip().lower() for s in source]:
        try:
            pval = anaprimes[word]
        except:
            pval = calc_pval(word)
        product *= pval
    return product

product = calculate_total_product(source)

print('product for {} is {}'.format(source, product))

try:
    anagrams = anaprimes_rev[product]
    if len(anagrams) > 1:
        print('single word anagrams={}'.format(anagrams))
except KeyError:
    print('no single word anagrams')

# find those keys that are factors of our target product
matching_prime_factors = [k for k in sorted_keys if product % k == 0]

print('Found {} matching prime factors'.format(len(matching_prime_factors)))

count = 0
for r in combinations(matching_prime_factors, 3):
    if reduce(operator.mul, r, 1) == product:
        words = ''
        for factor in r:
            words = 'w:{}[{}] {}'.format(anaprimes_rev[factor], factor, words)
        print('{}: {}'.format(count,words))
        count += 1

