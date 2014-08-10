
def manhattan_tourist(n, m, down, right):
    s = [[0] * (m + 1) for j in range(n + 1)]
    for i in range(m):
        s[0][i + 1] = s[0][i] + right[0][i]
    for i in range(n):
        s[i + 1][0] = s[i][0] + down[i][0]
    for i in range(n):
        for j in range(m):
            s[i + 1][j + 1] = max(s[i][j + 1] + down[i][j + 1],
                                  s[i + 1][j] + right[i + 1][j])
    return s[n][m]
        
    
n, m = int(input()), int(input())
down = [list(map(int, input().rsplit())) for j in range(n)]
input() # skip separator
right = [list(map(int, input().rsplit())) for j in range(n + 1)]

print(manhattan_tourist(n, m, down, right))
