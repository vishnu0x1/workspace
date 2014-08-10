N = 48
p = [0] * (N + 1)

p[0] = 1
for i in range(1, N + 1):
    for j in range(1, i + 1):
        #print(i, j, j * p[i - j])
        p[i] = max(p[i], j * p[i - j])

print(p[N])

