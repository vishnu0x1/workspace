
def lcs(x, y):
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for j in range(m + 1)]
    b = [['↺'] * n for j in range(m)]     # '↺', '←', '↑', '↖'
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i + 1][j + 1], b[i][j] = c[i][j] + 1, '↖'
            else:
                c[i + 1][j + 1], b[i][j] = max((c[i + 1][j], '←'),
                                               (c[i][j + 1], '↑'))
    return c, b

def construct_lcs(b, x):
    s = ''
    i, j = len(b) - 1, len(b[0]) - 1, 
    while i >= 0 and j >= 0:
        if b[i][j] == '↖':
            s = x[i] + s
            i, j = i - 1, j - 1
        elif b[i][j] == '←':
            j = j - 1
        else:
            i = i - 1
    return s
    
text1 = input()
text2 = input()
cost, backtrack = lcs(text1, text2)
lcs_text = construct_lcs(backtrack, text1)

print(lcs_text)
            
