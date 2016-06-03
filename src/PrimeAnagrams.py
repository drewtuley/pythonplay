import math
import string


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1)):
        if n != x and n % x == 0:
            return False
    return True


primes = [p for p in range(11, 150) if is_prime(p)]


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
            print('error {} '.format(err))
        else:
            complete = True
print('Processed {} anaprimes'.format(len(anaprimes)))

print(anaprimes['enumerations'])
print(anaprimes['mountaineers'])
print(len(anaprimes_rev))
print(anaprimes_rev[anaprimes['mountaineers']])
for prime in anaprimes_rev:
    if len(anaprimes_rev[prime]) > 1:
        print('Prime:{} anagrams={}'.format(prime, anaprimes_rev[prime]))

treasure = anaprimes['treasure']
hunt = anaprimes['hunt']
product = treasure * hunt
l=[(w1,w2) for w1 in anaprimes_rev.keys() for w2 in anaprimes_rev.keys() if w1*w2 == product]
for w1,w2 in l:
    print('w1:{} w2:{}'.format(anaprimes_rev[w1], anaprimes_rev[w2]))