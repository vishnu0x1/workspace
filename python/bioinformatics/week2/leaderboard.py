import itertools
import heapq

amino_mass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137,
     147, 156, 163, 186]

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


N = int(input())
spectrum = [int(s) for s in input().split()]

kmers = [m for m in amino_mass if m in spectrum]    # no duplicate kmers
leader_peptide = Peptide([], 0, 0)
leaderboard = [leader_peptide]
parent_mass = spectrum[-1]

while leaderboard:
    leaderboard = list(expand(leaderboard, kmers))
    for peptide in leaderboard:
        # donot remove peptides with mass == parent_mass, their score is
        # still required in eliminating the low scoring peptides
        if peptide.mass == parent_mass:
            if peptide.score > leader_peptide.score:
                leader_peptide = peptide
        elif peptide.mass > parent_mass:
            peptide.score = 0    # mark for removal
    leaderboard = heapq.nlargest(N, leaderboard, key=lambda x: x.score)
    leaderboard = [peptide for peptide in leaderboard if peptide.score]

answer = '-'.join([str(m) for m in leader_peptide.name])
print(answer)
