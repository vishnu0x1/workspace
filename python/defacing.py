#!/usr/bin/python3.2

import sys

G = [ 0b1111110,
      0b1100000,
      0b1011011,
      0b1110011,
      0b1100101,
      0b0110111, 
      0b0111111, 
      0b1100010,
      0b1111111, 
      0b1110111, 
      0b0000000 ]   # all off: state 10 or state -1

L = [x[:] for x in [[]] * len(G)]

def init():
    # j E L(i), iff i can be transformed into j
    for i in range(len(G)):
        L[i] = [j for j in range(10) if (~G[j] & G[i] == 0)]


##def borrow(x, m, k):
##    s = m[:]
##    
##    for i in range(k, -1, -1):
##        if m[i] <= L[x[i]][0]:
##            s[i] = L[x[i]][-1]
##        else:
##            s[i] = next(t for t in reversed(L[x[i]]) if t < m[i])
##            break
##            
##    for i in range(k + 1, len(m)):
##        s[i] = L[x[i]][-1]
##        
##    return s    
##
##
##def floor2(x, m):
##    for k in range(len(m)):
##        if m[k] not in L[x[k]]:
##            return borrow(x, m, k)
##    return m

	
def floor(x, m):
    
    # initial condition: le < sl
    # necessary for the following update logic
    sl = -1
    le = 0

    for i in range(len(m)):
        # loop invariant
        # le = max { z : z E perm(X[0..i-1]), z <= M }
        # sl = max { z : z E perm(X[0..i-1]) z < M }
        
        q1 = q2 = -1

        # find q1 and q2
        # q1 = max { z : z E L(Xi), z <= Mi }
        # q2 = max { z : z E L(Xi), z < Mi }
        for t in L[x[i]]:
            if t < m[i]:
                q1 = q2 = t
            elif t == m[i]:
                q1 = t
            else:
                break

        ple = le    # save current value of le
        psl = sl    # save current value of sl
        
        # update le
        if ple > psl and q1 != -1:
            le = ple * 10 + q1
        else:
            le = psl * 10 + L[x[i]][-1]     # L(Xi, -1) = max {L(Xi)}
        
        # update se
        if ple > psl and q2 != -1:
            sl = ple * 10 + q2
        else:
            sl = psl * 10 + L[x[i]][-1]     # L(Xi, -1) = max {L(Xi)}
    
    return le


def solve(x, m):
    # pad with state -1, L(-1) = last vector in L
    N = len(m) - len(x)
    x = [-1] * N + x

    res = 0
    for i in range(N+1):
        res = max(res, floor(x, m))
        x.append(-1)
        x.pop(0)    

    return res



init()

sys.stdin.buffer.readline()

for input_bytes in sys.stdin.buffer.readlines():
    input_bytes = input_bytes.split()
    x = [int(t) for t in map(chr, list(input_bytes[0]))]
    m = [int(t) for t in map(chr, list(input_bytes[1]))]

    print(solve(x, m))


	