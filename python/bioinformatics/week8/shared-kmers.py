
from collections import defaultdict
from itertools import product

def complement(pattern, s = {'A':'T', 'T':'A', 'G':'C', 'C':'G' }):    
    complement = pattern[::-1]  # create a copy & reverse it
    complement = [s[c] for c in complement]
    return ''.join(complement)

def shared_kmers(genome1, genome2):
    kmer_dict = defaultdict(lambda: ([], []))
    for i in range(len(genome1) - k + 1):
        kmer = genome1[i:i + k]
        kmer_dict[kmer][0].append(i)
        kmer_dict[complement(kmer)][0].append(i)

    for i in range(len(genome2) - k + 1):
        kmer = genome2[i:i + k]
        kmer_dict[kmer][1].append(i)

    kmer_matches = [x for x in kmer_dict.values() if x[0] and x[1]]
    return kmer_matches


k = int(input())
text1 = input()
text2 = input()
kmer_matches = shared_kmers(text1, text2)

for match in kmer_matches:
    for pair in product(*match):
        print(pair)
