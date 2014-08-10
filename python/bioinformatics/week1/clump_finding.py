text = input()
k,L,t = map(int, input().split())

d = {}
for i in range(len(text) - k + 1):
    kmer = text[i:i + k]
    if kmer in d:
        d[kmer].append((i, i + k - 1))  # save start and end indices
    else:
        d[kmer] = [(i, i + k - 1)]

clumps = []
for kmer, indices in d.items():
    for i in range(t - 1, len(indices)):
        if indices[i][1] - indices[i - t + 1][0] + 1 <= L:
           clumps.append(kmer)
           break

answer = ' '.join(clumps)
print(answer)
