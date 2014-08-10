import functools
import operator
import fileinput

# translate s to charset indices, inefficient algo but serves the purpose
def translate(s, charset='ACGT'):
    return [charset.index(x) for x in s]

# invert from charset indices to corresponding alphabet
def invert(s, charset='ACGT'):
    return ''.join([charset[i] for i in s])

# calc probability of kmer from the profile table
def probability(kmer, profile):
    pr = 1
    for i in range(len(kmer)):
        pr *= profile[i][kmer[i]]
    return pr

def slide(text, k):
    return (text[i:i + k] for i in range(len(text) - k + 1))
    
def profile_most_probable(text, profile, k):
    return max(slide(text, k), key=lambda x: probability(x, profile))

def add_to_profile(profile, motif, t):
    res = []
    for p, m in zip(profile, motif):
        p = [(q * (t - 1) + (m == i)) / t for i, q in enumerate(p)]
        res.append(p)
    return res

# calculate the score of motifs from the profile
def motifs_score(profile, t):
    return sum((1 - max(p)) * t for p in profile)

def greedy_motif_search(dna, k, t):
    best_motifs = None
    best_score = t * k
    for motif_0 in slide(dna[0], k):
        profile = [[0] * 4 for i in range(k)]
        profile = add_to_profile(profile, motif_0, 1)
        motifs = [motif_0]
        for i in range(1, len(dna)):
            motif = profile_most_probable(dna[i], profile, k)
            profile = add_to_profile(profile, motif, i + 1)
            motifs.append(motif)
        score = motifs_score(profile, t)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs

k, t = map(int, input().split())
dna = [input() for i in range(t)]

dna = [translate(seq) for seq in dna]
best_motifs = greedy_motif_search(dna, k, t)

for motif in best_motifs:
    print(invert(motif))




    
