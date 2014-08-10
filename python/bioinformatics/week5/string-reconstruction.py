import fileinput
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
        lc = lc[i:] + lc[:i]
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

# create a eulerian cycle in the graph G containing a eulerian path
def complete_cycle(G):
    in_deg, out_deg = defaultdict(int), defaultdict(int)
    start, finish = None, None
    for v in chain(*G.values()):
        in_deg[v] += 1
    for u, adj in G.items():
        out_deg[u] += len(adj)
    for v in set().union(out_deg, in_deg):
        if in_deg[v] < out_deg[v]:
            start = v
        elif in_deg[v] > out_deg[v]:
            finish = v
    G[finish].append(start)
    return start, finish

# extract eulerian path from eulerian cycle        
def extract_path(cycle, start, finish):
    for i in range(len(cycle) - 1):
        if cycle[i] == finish and cycle[i+1] == start:
            return cycle[i+1:] + cycle[:i+1]
    return cycle

G = defaultdict(list)
for line in fileinput.input():
    u, sep, v = line.rsplit()
    G[u].append(v)

s, f = complete_cycle(G)
cycle = eulerian_cycle(G, s)
answer = extract_path(cycle, s, f)
answer = [x[0] for x in answer[:-1]] + [answer[-1]]
answer = ''.join(answer)
print(answer)
