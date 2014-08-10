
k = 4
n = 10

s = [[0] * (n + 1) for i in range(k + 1)]
s[0][:] = range(n + 1)

for i in range(1, k + 1):
    for j in range(1, n + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1]

print(s[k][n])
