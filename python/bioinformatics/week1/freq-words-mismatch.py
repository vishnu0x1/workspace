import itertools

text,k,d = input().split()
k = int(k)
d = int(d)
l = len(text)

def check_match(text, pattern, d):
    mismatches = 0
    for j in range(len(pattern)):
        if text[j] != pattern[j]:
            mismatches += 1
            if mismatches > d:
                return False
    return True

def mutations(word, hamming_distance, charset='ATCG'):
    for indices in itertools.combinations(range(len(word)), hamming_distance):
        for replacements in itertools.product(charset, repeat=hamming_distance):
            mutation = list(word)
            for index, replacement in zip(indices, replacements):
                mutation[index] = replacement
            yield ''.join(mutation)

kmer_dict = {}
for i in range(l - k + 1):
    kmer = text[i:i + k]
    for mutation in mutations(kmer, d):
        kmer_dict[mutation] = 0

for kmer in kmer_dict.keys():
    for i in range(l - k + 1):
        if check_match(text[i:i + k], kmer, d):
            kmer_dict[kmer] += 1

max_freq = max(kmer_dict.values())
max_kmers = [kmer for kmer, freq in kmer_dict.items() if freq == max_freq]

answer = ' '.join(max_kmers)
print(answer)
