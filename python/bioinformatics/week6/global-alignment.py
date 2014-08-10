
def global_align(x, y, sigma, score):
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for j in range(m + 1)]
    b = [['↺'] * n for j in range(m)]     # '↺', '←', '↑', '↖'

    for i in range(m + 1):
        c[i][0] = -sigma * i
    for j in range(n + 1):
        c[0][j] = -sigma * j
    for i in range(m):
        for j in range(n):
            match = c[i][j] + score[x[i]][y[j]], '↖'
            insert = c[i][j + 1] - sigma, '↑'
            delete = c[i + 1][j] - sigma, '←'            
            c[i + 1][j + 1], b[i][j] = max(match, insert, delete)
    return c, b

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
cost, backtrack = global_align(x, y, 5, score)

aligned_text1, aligned_text2 = construct_alignment(backtrack, text1, text2)

print(cost[-1][-1])
print(aligned_text1)
print(aligned_text2)








