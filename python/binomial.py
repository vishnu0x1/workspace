#calculate negative binomial co-efficients

import sys

N = 5
a = [[0] * i for i in range(3, N+4)]    # extra zeros at begin and end                                        
a[0][1] = 1                             # base case, a[0] = [0, 1, 0]

for i in range(1, N+1):
    for j in range(1, len(a[i]) - 1):
        a[i][j] = a[i-1][j] - a[i-1][j-1]

for x in a:
    print(x)
