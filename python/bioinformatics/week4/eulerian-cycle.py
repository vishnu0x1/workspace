import fileinput
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


G = defaultdict(list)
for line  in fileinput.input():
    u, sep, adj = line.rsplit()
    u, adj = int(u), map(int, adj.split(","))
    for v in adj:
        G[u].append(v)

answer = eulerian_cycle(G, 0)
answer.append(answer[0])
answer = '->'.join(map(str, answer))
print(answer)
