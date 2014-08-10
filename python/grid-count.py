# compute no of monotonic paths in a rectangular grid
# of dimension m x n
from math import factorial as f

n = 5

p = [[0] * (n+1) for i in range(n+1)]
for i in range(n+1):  p[0][i] = 1
for i in range(n+1):  p[i][0] = 1

for l in range(1, n+1):
    for r in range(1, n+1):
        p[l][r] = p[l-1][r] + p[l][r-1]

for x in p:     print(x)

# for m x n grid, no of paths = (m+n)!/(m!*n!)
print(f(2*n) / (f(n) * f(n)))   
