mass = 1420

a = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137,
     147, 156, 163, 186]

f = [0] * (mass + 1)
for j in a:     f[j] = 1

for n in range(mass + 1):
    for j in a:
        if n > j:   f[n] += f[n - j]

print(f[mass])
