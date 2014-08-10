#print the k-th permutation

import math
k = 11
n = 5
f = [0] * n

k = k - 1
for j in range(1, n+1):
    print(j, k, k % j)
    f[n - j] = k % j
    k = k // j                  # in jth step, k = order / fact(j)

print(f)

s = ['a', 'b', 'c', 'd', 'e']
print([s.pop(j) for j in f])


