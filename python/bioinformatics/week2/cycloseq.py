import itertools
from itertools import chain

amino_mass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137,
     147, 156, 163, 186]

def substrings(iterable):
    n = len(iterable)
    return [iterable[i:i + l] for l in range(1, n) for i in range(n - l + 1)]

def cyclic_substrings(iterable):
    n = len(iterable)
    iterable = iterable + iterable[:-1]
    return [iterable[i:i + l] for l in range(1, n) for i in range(n)]

# generate the mass spectrum of the cyclopeptide
def cyclospectrum(peptide):
    subpeptides = [[0]] + cyclic_substrings(peptide) + [peptide]
    return sorted(map(sum, subpeptides))

# calc the mass of the peptide fragments (ignoring cyclic struct)
def mass_fragments(peptide):
    subpeptides = [[0]] + substrings(peptide) + [peptide]
    return sorted(map(sum, subpeptides))

# check if spectrum 's' is a subset of spectrum 't'
def compare(s, t):
    return set(s).issubset(t)

# expand each peptide in peptide
def expand(peptide_list, kmers):
    for peptide in peptide_list:
        for kmer in kmers:
            yield peptide + [kmer]


spectrum = [int(s) for s in input().split()]
kmers = [m for m in amino_mass if m in spectrum]    # no duplicate kmers
peptide_list = [[]]
res = []

while peptide_list:
    peptide_list = expand(peptide_list, kmers)
    peptide_list = [peptide for peptide in peptide_list
                    if compare(mass_fragments(peptide), spectrum)]
    res += [peptide for peptide in peptide_list
                    if compare(spectrum, cyclospectrum(peptide))]

# crazy concatenation
res = ' '.join(['-'.join([str(m) for m in peptide]) for peptide in res])
print(res)
