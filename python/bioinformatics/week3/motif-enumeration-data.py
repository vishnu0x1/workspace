import itertools
import fileinput

def mutations(word, hamming_distance, charset='ATCG'):
    for indices in itertools.combinations(range(len(word)), hamming_distance):
        for replacements in itertools.product(charset, repeat=hamming_distance):
            mutation = list(word)
            for index, replacement in zip(indices, replacements):
                mutation[index] = replacement
            yield ''.join(mutation)

def motif_enumeration(dna, k, d):
    kmer_dict = {}
    for j in range(len(dna)):
        dna_subseq = dna[j]
        for i in range(len(dna_subseq) - k + 1):
            kmer = dna_subseq[i:i + k]
            for mutation in mutations(kmer, d):
                kmer_dict[mutation] = kmer_dict.get(mutation, 0) | (1 << j)

    all_flags = (1 << len(dna)) - 1
    return (kmer for kmer, flag in kmer_dict.items() if flag == all_flags)


k, d = map(int, input().split())
# var dna := list of subsequences of biological dna
dna = [line.rstrip() for line in fileinput.input()]
result = motif_enumeration(dna, k, d)

print(' '.join(result))
                        
                
