import itertools
import fileinput

def generator(k, charset='ACGT'):
    for x in itertools.product(charset, repeat=k):
        yield ''.join(x)

def hamdist(str1, str2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def score(pattern, dna):
    D = 0
    for seq in dna:
        D += min(hamdist(seq[i:i + k], pattern)
                 for i in range(len(seq) - k + 1))
    return D

def median_string(dna, k):
    return min(generator(k), key=lambda x: score(x, dna))


k = int(input())
# var dna := list of subsequences of biological dna
dna = [line.rstrip() for line in fileinput.input()]
print(median_string(dna, k))
