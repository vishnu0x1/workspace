import operator

# calc the needleman–wunsch score using linear space
# returns the last row of score matrix
def nw_score(x, y, sigma, score):
    m, n = len(x), len(y)
    c = [-sigma * j for j in range(n + 1)], [0] * (n + 1)

    for i in range(m):
        c[1][0] = -sigma * (i + 1)
        for j in range(n):
            match = c[0][j] + score[x[i] + y[j]]
            insert = c[0][j + 1] - sigma
            delete = c[1][j] - sigma
            c[1][j + 1] = max(match, insert, delete)
        c = c[1], [0] * (n + 1)
    return c[0]

# optimal alignment using linear space : hirschberg algorithm
def hirschberg_align(x, y):
    z, w = '', ''
    m, n = len(x), len(y)
    if m == 0:
        z, w = '-' * n, y
    elif n == 0:
        z, w = x, '-' * m
    elif m == 1:
        z, w = single_align(x, y, sigma, score)
    elif n == 1:
        w, z = single_align(y, x, sigma, score)
    else:
        xmid = m // 2
        ra = nw_score(x[:xmid], y, sigma, score)
        rb = nw_score(x[:xmid - 1:-1], y[::-1], sigma, score)
        ymid = max(range(n + 1), key=lambda p: ra[p] + rb[-p - 1])
        s = hirschberg_align(x[:xmid], y[:ymid])
        t = hirschberg_align(x[xmid:], y[ymid:])
        z, w = s[0] + t[0], s[1] + t[1]
    return z, w

# a is single character, y is a string
def single_align(a, y, sigma, score):
    matches = [score[a + p] for p in y]
    i, s = max(enumerate(matches), key=operator.itemgetter(1))
    if -sigma >= s:
        z = a + '-' * len(y)
        w = '-' + y
    else:
        z = ('-' * i)  +  a  +  ('-' * (len(y) - i - 1))
        w = y
    return z, w          

def read_blosom_data(file):
    symbols = file.readline().rsplit()
    score = {}
    for line in file:
        line = line.split()
        keys = [line[0] + x for x in symbols]
        for key, value in zip(keys, line[1:]):
            score[key] = int(value)
    return score


x = input()
y = input()

file = open('BLOSUM62.txt', 'r')
score = read_blosom_data(file)
sigma = 5

aligned_text1, aligned_text2 = hirschberg_align(x, y)
cost = nw_score(x, y, sigma, score)[-1]

print(cost)
print(aligned_text1)
print(aligned_text2)
