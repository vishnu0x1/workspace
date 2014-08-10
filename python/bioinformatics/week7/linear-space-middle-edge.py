
def nw_score(x, y, sigma, score):
    m, n = len(x), len(y)
    c = [-sigma * j for j in range(n + 1)], [0] * (n + 1)
    
    for i in range(m):
        c[1][0] = -sigma * (i + 1)
        for j in range(n):
            match = c[0][j] + score[x[i]][y[j]]
            insert = c[0][j + 1] - sigma
            delete = c[1][j] - sigma
            c[1][j + 1] = max(match, insert, delete)
        c = c[1], [0] * (n + 1)
    return c[0]

def middle_edge(x, y):
    m, n = len(x), len(y)

    xmid = len(x) // 2
    ra = nw_score(x[:xmid], y, sigma, score)
    rb = nw_score(x[:xmid:-1], y[::-1], sigma, score)[::-1]

    diag = lambda z: ra[z] + rb[z + 1] + score[x[xmid]][y[z]]
    vert = lambda z: ra[z + 1] + rb[z + 1] - sigma

    head = ra[0] + rb[0] - sigma, 0, 0
    for j in range(n):
        head = max(head, (vert(j), j + 1, j + 1), (diag(j), j,  j + 1))

    return (xmid, head[1]), (xmid + 1, head[2])

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
sigma = 5

# problem definition states that the split should occur at middle column
# current impl splits at middle row, so swap inputs and reverse o/p coordinates
node1, node2 = middle_edge(y, x)
print(node1[::-1], node2[::-1])

