import bisect

def composition(text, k):
    kmers = []
    for i in range(len(text) - k + 1):
        bisect.insort_left(kmers, text[i:i + k])
    return kmers


k = int(input())
text = input()

kmers = composition(text, k)
for kmer in kmers:
    print(kmer)
