import random

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

def calc_motifs(profile, dna, k):
    return [profile_most_probable(seq, profile, k) for seq in dna]

def calc_profile(motifs):
    k, t = len(motifs[0]), len(motifs)
    unit = 1 / (t + 4)
    profile = [[unit] * 4 for i in range(k)]
    for m in motifs:
        for i in range(k):
            profile[i][m[i]] += unit
    return profile

# calculate the score of motifs from the profile
def motifs_score(profile, t):
    return sum((1 - max(p)) * t for p in profile)

# select random motifs from each of the dna sequences
def random_motifs(dna, k):
    motifs = []
    for seq in dna:
        i = int(random.random() * (len(seq) - k))
        motifs.append(seq[i:i + k])
    return motifs

def randomized_motif_search(dna, k, t):
    best_motifs = random_motifs(dna, k)
    best_score = t * k      # max possible score
    while True:
        profile = calc_profile(best_motifs)
        motifs = calc_motifs(profile, dna, k)
        score = motifs_score(profile, t)
        if score < best_score:
            best_score = score
            best_motifs = motifs
        else:
            return best_motifs
    

k, t = map(int, input().split())
dna = [input() for i in range(t)]

dna = [translate(seq) for seq in dna]
best_motifs = randomized_motif_search(dna, k, t)

for motif in best_motifs:
    print(invert(motif))




    
