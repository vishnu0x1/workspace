
def local_align(x, y, sigma, score):
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for j in range(m + 1)]
    b = [['↺'] * n for j in range(m)]     # '↺', '←', '↑', '↖'

    best = (0, )        # save the best score and its indices
    for i in range(m):
        for j in range(n):
            zero = 0, '↺'
            match = c[i][j] + score[x[i]][y[j]], '↖'
            insert = c[i][j + 1] - sigma, '↑'
            delete = c[i + 1][j] - sigma, '←'            
            c[i + 1][j + 1], b[i][j] = max(zero, match, insert, delete)
            best = max(best, (c[i + 1][j + 1], i, j))
    return c, b, best[1], best[2]

def construct_alignment(b, i, j, x, y):
    s, t = '', ''
    while b[i][j] != '↺':
        if b[i][j] == '←':
            s, t = '-' + s, y[j] + t
            j = j - 1
        elif b[i][j] == '↑':
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

file = open('PAM250.txt', 'r')
amino_acids, score = read_blosom_data(file)
x = [amino_acids.index(m) for m in text1]
y = [amino_acids.index(m) for m in text2]
cost, backtrack, m, n = local_align(x, y, 5, score)

aligned1, aligned2 = construct_alignment(backtrack, m, n, text1, text2)

print(cost[m + 1][n + 1])
print(aligned1)
print(aligned2)








