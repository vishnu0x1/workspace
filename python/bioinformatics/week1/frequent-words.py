
text = input()
k = int(input())
l = len(text)

d = {}
for i in range(l - k + 1):
    kmer = text[i:i + k]
    d[kmer] = d[kmer] + 1 if kmer in d else 1

max_freq = max(d.values())
max_kmers = [kmer for kmer, freq in d.items() if freq == max_freq]

answer = ' '.join(max_kmers)
print(answer)
        
