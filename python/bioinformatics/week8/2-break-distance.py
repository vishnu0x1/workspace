from ast import literal_eval
from collections import defaultdict
from itertools import chain
from math import copysign

def CC(G):
    global visited
    visited = [False] * len(G)
    count = 0
    for v in G.keys():
        if not visited[v - 1]:
            dfs(G, v)
            count = count + 1
    return count

def dfs(G, v):
    stack = [v]
    while stack:
        v = stack.pop()
        visited[v - 1] = True
        for w in G[v]:
            if not visited[w - 1]:
                stack.append(w)

def two_break_distance2(P, Q):
    P = [(p[k - 1], -p[k]) for p in P for k in range(len(p))]
    Q = [(q[k - 1], -q[k]) for q in Q for k in range(len(q))]
    G = defaultdict(list)
    for u, v in chain(P, Q):
        G[u].append(v)
        G[v].append(u)
    dist = len(Q) - CC(G)    # number of connected components
    return dist

def two_break_distance(P, Q):
    P, Q = identity_transform(P, Q)
    P, Q = collapse_transform(P, Q)
    G = defaultdict(list)
    for u, v in Q:
        G[u].append(v)
        G[v].append(u)
    dist = len(Q) - CC(G)    # number of connected components
    return dist

def collapse_transform(P, Q):
    l = sum(len(x) for x in P)
    T = [0] * (2 * l + 1)
    for i in range(1, l + 1):
        T[i], T[-i] = i, i - 1
    T[-1] = l
    P = [(T[p[k - 1]], T[-p[k]]) for p in P for k in range(len(p))]
    Q = [(T[q[k - 1]], T[-q[k]]) for q in Q for k in range(len(q))]
    return P, Q

def identity_transform(P, Q):
    l = sum(len(x) for x in P)
    T = [0] * (2 * l + 1)
    for i, p in enumerate(chain(*P)):
        T[p] = i + 1
    P = [[T[p] for p in perm] for perm in P]
    Q = [[T[q] or -T[-q] for q in perm] for perm in Q]
    return P, Q


# test dataset: page 12, AreThereFragileRegions.59-74.pdf       
# print(two_break_distance([[1, 2, 3, 4, 5, 6]], [[1, -3, -6, -5], [2, -4]]))

text1, text2 = input(), input()
P = text1.replace(' ', ',').replace(')(', '],[')
P = '[[' + P[1:-1] + ']]'
Q = text2.replace(' ', ',').replace(')(', '],[')
Q = '[[' + Q[1:-1] + ']]'

P, Q = literal_eval(P), literal_eval(Q)
print(two_break_distance2(P, Q))

