import itertools

text = input()
k, d = map(int, input().split())
l = len(text)

def check_match(text, pattern, d):
    mismatches = 0
    for x, y in zip(text, pattern):
        if x != y:
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

def complement(pattern, s = {'A':'T', 'T':'A', 'G':'C', 'C':'G' }):    
    complement = pattern[::-1]  # create a copy & reverse it
    complement = [s[c] for c in complement]
    return ''.join(complement)

kmer_dict = {}
for i in range(l - k + 1):
    kmer = text[i:i + k]
    for mutation in mutations(kmer, d):
        kmer_dict[mutation] = 0
        kmer_dict[complement(mutation)] = 0
        
for kmer in kmer_dict.keys():
    for i in range(l - k + 1):
        if check_match(text[i:i + k], kmer, d):
            kmer_dict[kmer] += 1

count_dict = {}
for kmer in kmer_dict.keys():
    count_dict[kmer] = kmer_dict[kmer] + kmer_dict[complement(kmer)]

max_freq = max(count_dict.values())
max_kmers = [kmer for kmer, freq in count_dict.items() if freq == max_freq]

answer = ' '.join(max_kmers)
print(answer)
