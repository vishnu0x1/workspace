from itertools import chain

spectrum = map(int, input().split())
spectrum = sorted(spectrum)

l = len(spectrum)
conv = [[0] * i for i in range(1, l)]

for i in range(1, l):
    for j in range(i):
        conv[i - 1][j] = spectrum[i] - spectrum[j] 

answer = map(lambda x: str(x) if x else '', chain.from_iterable(conv))
answer = ' '.join(answer)
print(answer)
