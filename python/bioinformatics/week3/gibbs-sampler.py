import random
import itertools

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
    
def profile_random_kmer(text, profile, k):
    return pick_random(slide(text, k), lambda x: probability(x, profile))

# apply laplace's rule of succession to form profile
# see equivalent func in greedy-motif-search.py
def calc_profile(motifs):
    k, t = len(motifs[0]), len(motifs)
    unit = 1 / (t + 4)
    profile = [[unit] * 4 for i in range(k)]
    for m in motifs:
        for i in range(k):
            profile[i][m[i]] += unit
    return profile

def add_to_profile(profile, motif, t):
    res = []
    for p, m in zip(profile, motif):
        p = [(q * ((t - 1) + 4) + (m == i)) / (t + 4) for i, q in enumerate(p)]
        res.append(p)
    return res

def remove_from_profile(profile, motif, t):
    res = []
    for p, m in zip(profile, motif):
        p = [(q * (t + 4) - (m == i)) / ((t - 1) + 4) for i, q in enumerate(p)]
        res.append(p)
    return res

# calculate the score of motifs from the profile
def motifs_score(profile, t):
    norm = lambda x: t + 1 - (x * (t + 4))
    return sum(norm(max(p)) for p in profile)

# pick random element from iterable, given PDF f
def pick_random(iterable, f):
    iterable = list(iterable)
    cdf = list(itertools.accumulate(f(x) for x in iterable))
    r = random.random() * cdf[-1]
    return next(x for x, p in zip(iterable, cdf) if p >= r)

# select random motifs from each of the dna sequences
def random_motifs(dna, k):
    motifs = []
    for seq in dna:
        i = int(random.random() * (len(seq) - k))
        motifs.append(seq[i:i + k])
    return motifs

def gibbs_sampler(dna, k, t, N):
    best_score = t * k      # max possible score
    best_motifs = None
    for p in range(20):
        motifs = random_motifs(dna, k)
        profile = calc_profile(motifs)
        for q in range(N):
            i = int(random.random() * t)

            # calc ith motif from profile
            profile = remove_from_profile(profile, motifs[i], t)
            motifs[i] = profile_random_kmer(dna[i], profile, k)

            # calc score of motifs from profile
            profile = add_to_profile(profile, motifs[i], t)
            score = motifs_score(profile, t)
            if score < best_score:
                best_score = score
                best_motifs = motifs[:]
    return best_motifs

k, t, N = map(int, input().split())
dna = [input() for i in range(t)]

dna = [translate(seq) for seq in dna]
best_motifs = gibbs_sampler(dna, k, t, N)

print(motifs_score(calc_profile(best_motifs), len(best_motifs)))

for motif in best_motifs:
    print(invert(motif))




    
