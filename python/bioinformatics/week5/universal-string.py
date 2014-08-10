from itertools import chain
from collections import defaultdict

def eulerian_cycle(G, v):
    lc = []    
    proceed = True
    while proceed:
        lc = list(remove_cycle(G, v)) + lc
        i = find_next_unexplored(G, lc)
        if i is None:
            i, proceed = 0, False
        v = lc[i]
        #print('b:', lc)
        lc = lc[i:] + lc[:i]
        #print('a:', lc)
    return lc

def find_next_unexplored(G, c):
    for i in range(len(c)):
        if G[c[i]]:     return i

# remove a cycle from G, starting at node u
def remove_cycle(G, u):
    v, proceed = u, True
    while proceed:
        yield v
        v = G[v].pop()
        proceed = (u != v)


k = int(input())

l = 2 ** k
G = defaultdict(list)
for i in range(l):
    u = i >> 1
    v = i & ~(l >> 1)   # print(u, v) to understand this seq
    G[u].append(v)

# cycle will be of the form:
# 123456 -> 234567 -> 345678 -> 456789 -> 567891 -> 678912
# -> 789123 -> 891234 -> 912345, note last k - 2 cycles (k = 7 here)
# extracting first/last bit from every node will give the universal string
 
answer = eulerian_cycle(G, 0)
answer = [str(x & 1) for x in answer]
print(''.join(answer))


