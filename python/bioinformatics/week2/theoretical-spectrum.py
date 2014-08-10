import itertools
from itertools import chain

def build_mass_table():
    mass_table = {}
    f = open('integer_mass_table.txt', 'r')
    for line in f:
        amino_acid, mass = line.split()
        mass_table[amino_acid] = int(mass)
    return mass_table
    
def cyclic_substrings(iterable):
    n = len(iterable)
    iterable = iterable + iterable[:-1]
    return iter(iterable[i:i + l] for l in range(1, n) for i in range(n))

def molecular_mass(peptide):
    return sum(mass_table[amino_acid] for amino_acid in peptide)

# theoretical spectrum = 0, mass(subpeptides...), mass(entire peptide)
def construct_mass_spectrum(peptide):
    mass = []
    for subpeptide in cyclic_substrings(peptide):
        mass.append(molecular_mass(subpeptide))
    mass = [0] + sorted(mass) + [molecular_mass(peptide)]
    return mass

peptide = input()
mass_table = build_mass_table()
mass_spectrum = construct_mass_spectrum(peptide)
answer = ' '.join(map(str, mass_spectrum))
print(answer)

