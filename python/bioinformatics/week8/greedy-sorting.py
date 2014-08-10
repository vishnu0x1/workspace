
def greedy_sort(perm):
    dist = 0
    for i in range(len(perm)):
        k = None
        try:
            k = perm.index(i + 1)
        except ValueError:
            k = perm.index(-i - 1)

        if i != k:
            perm[i:k + 1] = [-x for x in reversed(perm[i:k + 1])]
            dist = dist + 1
            pretty_print(perm)
        if perm[i] != i + 1:
            perm[i] = -perm[i]
            dist = dist + 1
            pretty_print(perm)
        
    return dist

def pretty_print(perm):
    perm = map('{0:+}'.format, perm)
    print('(' + ' '.join(perm) + ')', sep='')


text = input()
perm = list(map(int, text[1:-1].split()))

greedy_sort(perm)
