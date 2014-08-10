import operator
import collections
import itertools

class Peptide:
    def __init__(self, name, mass, score):
        self.name = name
        self.mass = mass
        self.score = score

def substrings(iterable):
    n = len(iterable)
    return [iterable[i:i + l] for l in range(1, n) for i in range(n - l + 1)]

# calc the mass of the peptide fragments (ignoring cyclic struct)
def mass_fragments(peptide):
    fragments = [[0]] + substrings(peptide) + [peptide]
    return sorted(map(sum, fragments))

# compute the score of match between s and t
def score(s, t):
    return len(set(s).intersection(t))

# expand each peptide in peptide
def expand(peptide_list, kmers):
    for peptide in peptide_list:
        for kmer in kmers:
            name = peptide.name + [kmer]
            mass = peptide.mass + kmer
            pscore = score(mass_fragments(name), spectrum)
            yield Peptide(name, mass, pscore)

# find the most frequent kmers by spectral convolution
def most_frequent(n, spectrum):
    conv = collections.Counter()
    for i in range(1, len(spectrum)):
        for j in range(i):
            element = spectrum[i] - spectrum[j]
            if element >= 57 and element <= 200:
                conv[element] += 1
    conv = cut(n, conv.most_common(), operator.itemgetter(1))
    return (kmer for kmer, freq in conv)

def cut(n, iterable, key):
    pk = None
    for x in iterable:
        if n:   n, pk = n - 1, key(x)
        if pk != key(x):    break
        yield x
    
M = int(input())
N = int(input())
spectrum = map(int, input().split())
spectrum = sorted(spectrum)
kmers = list(most_frequent(M, spectrum))    # no duplicate kmers

leader_peptide = Peptide([], 0, 0)
leaderboard = [leader_peptide]
parent_mass = spectrum[-1]
while leaderboard:
    leaderboard = list(expand(leaderboard, kmers))
    for peptide in leaderboard:
        if peptide.mass == parent_mass:
            if peptide.score > leader_peptide.score:
                leader_peptide = peptide
        elif peptide.mass > parent_mass:
            peptide.score = 0    # mark for removal
    leaderboard = [peptide for peptide in leaderboard if peptide.score]
    leaderboard = sorted(leaderboard, key=lambda x: x.score, reverse=True)
    leaderboard = list(cut(N, leaderboard, lambda x: x.score) )

answer = '-'.join([str(m) for m in leader_peptide.name])
print(answer)
