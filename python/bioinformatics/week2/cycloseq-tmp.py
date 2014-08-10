import itertools
from itertools import chain

amino_mass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137,
     147, 156, 163, 186]

def cyclic_substrings(iterable):
    n = len(iterable)
    iterable = iterable + iterable[:-1]
    return [iterable[i:i + l] for l in range(1, n) for i in range(n)]

# generate the mass spectrum of the cyclopeptide
def cyclospectrum(peptide):
    subpeptides = [[0]] + cyclic_substrings(peptide) + [peptide]
    return sorted(map(sum, subpeptides))

# check if spectrum 's' is a subset of spectrum 't'
def compare(s, t):
    return set(s).issubset(t)

# expand each peptide in peptide
def expand(peptide_list, kmers):
    for peptide in peptide_list:
        for kmer in kmers:
            yield peptide + [kmer]

spectrum =  map(int, "0 113 128 186 241 299 314 427".split()) #[0, 113, 128, 186, 241, 299, 314, 427]
kmers = [m for m in spectrum if m in amino_mass]
peptide_list = [[]]

res = []
peptide_list = expand(peptide_list, kmers)
#peptide_list = [peptide for peptide in peptide_list
#                    if compare(cyclospectrum(peptide), spectrum)]
print(peptide_list)
