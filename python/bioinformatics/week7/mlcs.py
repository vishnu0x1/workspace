import sys

Infinity = sys.maxsize

def mlcs(x, y, z):
    l, m, n = len(x), len(y), len(z)
    c = [[[0] * (n + 1) for j in range(m + 1)] for i in range(l + 1)]
    b = [[[0] * (n + 1) for j in range(m + 1)] for i in range(l + 1)]

    for i in range(l + 1):
        for j in range(m + 1):
            for k in range(n + 1):
                c1 = c2 = c3 = c4 = c5 = c6 = c7 = (-Infinity, )
                if k > 0:   c1 = c[i][j][k - 1], 1
                if j > 0:   c2 = c[i][j - 1][k], 2
                if i > 0:   c4 = c[i - 1][j][k], 4
                if j > 0 and k > 0:     c3 = c[i][j - 1][k - 1], 3
                if i > 0 and k > 0:     c5 = c[i - 1][j][k - 1], 5
                if i > 0 and j > 0:     c6 = c[i - 1][j - 1][k], 6
                if i > 0 and j > 0 and k > 0:
                    c7 = c[i-1][j-1][k-1] + (x[i-1] == y[j-1] == z[k-1]), 7
                if i > 0 or j > 0 or k > 0:
                    c[i][j][k], b[i][j][k] = max(c1, c2, c3, c4, c5, c6, c7)
    return c, b

def construct_alignment(b, x, y, z):
    r, s, t = '', '', ''
    i, j, k = len(b) - 1, len(b[0]) - 1, len(b[0][0]) - 1

    d = -1
    while d != 0:
        d = b[i][j][k]
        
        if d & 4:
            r = x[i - 1] + r
            i = i - 1
        else:
            r = '-' + r
            
        if d & 2:
            s = y[j - 1] + s
            j = j - 1
        else:
            s = '-' + s
            
        if d & 1:
            t = z[k - 1] + t
            k = k - 1
        else:
            t = '-' + t

    return r, s, t


#text1 = 'a'
#text2 = 'ab'
#text3 = 'aac'
#
# backtrack:
#[[0, 1, 1, 1], [2, 3, 3, 3], [2, 3, 3, 3]]
#[[4, 5, 5, 5], [6, 7, 7, 1], [6, 2, 3, 3]]
#
# cost:
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#[[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1]]

text1 = input()
text2 = input()
text3 = input()

cost, backtrack = mlcs(text1, text2, text3)
o1, o2, o3 = construct_alignment(backtrack, text1, text2, text3)

print(cost[-1][-1][-1])
print(o1)
print(o2)
print(o3)

