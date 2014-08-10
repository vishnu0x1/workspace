
def edit_distance(x, y):
    m, n = len(x), len(y)
    c = [[0] * (n + 1) for j in range(m + 1)]
    for i in range(m + 1):
        c[i][0] = i
    for j in range(n + 1):
        c[0][j] = j
    for i in range(m):
        for j in range(n):
            match = c[i][j] + (x[i] != y[j])
            insert = c[i][j + 1] + 1
            delete = c[i + 1][j] + 1
            c[i + 1][j + 1] = min(match, insert, delete)
    return c[m][n]


text1 = input()
text2 = input()

print(edit_distance(text1, text2))
