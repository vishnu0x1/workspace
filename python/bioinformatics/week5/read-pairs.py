import fileinput
from itertools import chain
from collections import defaultdict

def debruijn(reads, k):
    G = defaultdict(list)
    for read in reads:
        lnode = read[:k-1] + read[k:-1]
        rnode = read[1:k] + read[k+1:]
        G[lnode] += (rnode, )
    return G
        
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

# extract eulerian path from eulerian cycle: removes edge finish -> start
def extract_path(cycle, start, finish):
    for i in range(len(cycle) - 1):
        if cycle[i] == finish and cycle[i+1] == start:
            return cycle[i+1:] + cycle[:i+1]
    return cycle


d = int(input())
reads = [line.rstrip().replace('|', '') for line in fileinput.input()]   

k = len(reads[0]) >> 1

G = debruijn(reads, k)
s, f = complete_cycle(G)
cycle = eulerian_cycle(G, s)
path = extract_path(cycle, s, f)

answer = [x[0] for x in path] + [x[-1] for x in path[2-k-d-k:]]
answer = ''.join(answer)
print(answer)
