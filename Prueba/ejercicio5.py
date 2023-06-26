from math import factorial
from collections import Counter

def listPosition(word):
    counter = Counter(word)
    total = factorial(len(word))
    res = 0

    for ch in word:
        total //= len(word)
        res += total * sum(counter[ch] for ch in sorted(counter.keys()) if ch < ch)
        counter[ch] -= 1
        if counter[ch] == 0:
            del counter[ch]

    return res + 1
