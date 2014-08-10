w = 7
d = 5
q = 23
dsum = 0
for i in range(d):
    avg = q / w
    ravg = ((q * 10) // w) / 10
    delta = avg - ravg
    dsum += delta
    print(q, avg, ravg, delta)

print(dsum, dsum * w)
