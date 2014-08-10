import sys

Infinity = sys.maxsize

def affine_gap_global_align(x, y, sigma, eps, score):
    m, n = len(x), len(y)
    g = lambda m, n, p: [[p] * (n + 1) for j in range(m + 1)]
    b = g(m - 1, n - 1, '↺')     # '↺', '←', '↑', '↖'

    # M[0][0] = 0, L[0][*] = -inf, U[0][*] = -inf
    M, L, U = g(m, n, 0), g(m, n, -Infinity), g(m, n, -Infinity)

    for i in range(1, m + 1):
        M[i][0] = L[i][0] = -sigma - eps * (i - 1)
    for j in range(1, n + 1):
        M[0][j] = U[0][j] = -sigma - eps * (j - 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            L[i][j] = max(L[i - 1][j] - eps, M[i - 1][j] - sigma)
            U[i][j] = max(U[i][j - 1] - eps, M[i][j - 1] - sigma)

            match = M[i- 1][j - 1] + score[x[i - 1]][y[j - 1]], '↖'
            insert = L[i][j], '↑'
            delete = U[i][j], '←'
            M[i][j], b[i - 1][j - 1] = max(match, insert, delete)

    return M[m][n], b

def construct_alignment(b, x, y):
    s, t = '', ''
    i, j = len(b) - 1, len(b[0]) - 1
    while i >= 0 or j >= 0:
        if i < 0 or (j >= 0 and b[i][j] == '←'):
            s, t = '-' + s, y[j] + t
            j = j - 1
        elif j < 0 or (i >= 0 and b[i][j] == '↑'):
            s, t = x[i] + s, '-' + t
            i = i - 1
        else:
            s, t = x[i] + s, y[j] + t
            i, j = i - 1, j - 1
    return s, t

def read_blosom_data(file):
    symbols = file.readline()
    amino_acids, score = [], []
    for line in file:
        line = line.split()
        amino_acids.append(line[0])
        amino_acid_score = list(map(int, line[1:]))
        score.append(amino_acid_score)
    return amino_acids, score


text1 = input()
text2 = input()

file = open('BLOSUM62.txt', 'r')
amino_acids, score = read_blosom_data(file)
x = [amino_acids.index(m) for m in text1]
y = [amino_acids.index(m) for m in text2]

score, backtrack = affine_gap_global_align(x, y, 11, 1, score)
aligned_text1, aligned_text2 = construct_alignment(backtrack, text1, text2)

print(score)
print(aligned_text1)
print(aligned_text2)








