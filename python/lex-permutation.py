a = [1, 2, 3, 4]

k = len(a) - 2
i = 1
while k >= 0:
    if a[k] < a[k+1]:
        l = len(a) - 1
        while a[l] < a[k]:
            l = l - 1
        a[k], a[l] = a[l], a[k]
        a[k+1:] = a[:k:-1]
        i = i + 1
        print(i, a)
        k = len(a) - 1        
    k = k - 1

