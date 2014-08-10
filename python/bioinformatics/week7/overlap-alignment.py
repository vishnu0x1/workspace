
def overlap_align(x, y):
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for j in range(m + 1)]
    b = [['↺'] * n for j in range(m)]     # '↺', '←', '↑', '↖'

    for j in range(n + 1):
        c[0][j] = -j
    for i in range(m):
        for j in range(n):
            match = c[i][j] + 3 * (x[i] == y[j]) - 2, '↖'
            insert = c[i][j + 1] - 2, '↑'
            delete = c[i + 1][j] - 2, '←'            
            c[i + 1][j + 1], b[i][j] = max(match, insert, delete)
    return c, b

def construct_alignment(c, b, x, y):
    s, t = '', ''
    i = len(b) - 1
    j = max(range(len(b)), key=lambda k: c[-1][k + 1])
    print(c[-1][j + 1])
    while j >= 0:
        if i < 0 or b[i][j] == '←':
            s, t = '-' + s, y[j] + t
            j = j - 1
        elif b[i][j] == '↑':
            s, t = x[i] + s, '-' + t
            i = i - 1
        else:
            s, t = x[i] + s, y[j] + t
            i, j = i - 1, j - 1
    return s, t

text1 = input()
text2 = input()

cost, backtrack = overlap_align(text1, text2)
o1, o2 = construct_alignment(cost, backtrack, text1, text2)

print(o1)
print(o2)








