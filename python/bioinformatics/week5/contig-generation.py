import fileinput
from itertools import chain
from collections import defaultdict

def debruijn(patterns):
    G = defaultdict(list)
    for kmer in patterns:
        lnode, rnode = kmer[:-1], kmer[1:]
        G[lnode] += (rnode, )
        G[rnode]
    return G

def generate_contigs(G):
    B = find_branching_nodes(G)
    for u, adj in G.items():
        if not B[u]:    continue
        while adj:
            yield list(traverse_contig(G, B, u))

def traverse_contig(G, B, v):
    proceed = True
    yield v
    while proceed:
        v = G[v].pop()
        yield v
        proceed = G[v] and not B[v]
        
def find_branching_nodes(G):
    in_deg, out_deg = compute_degree(G)
    branching = {}
    for u in set().union(in_deg, out_deg):
        branching[u] = not (in_deg[u] == out_deg[u] == 1)
    return branching

# compute the degree of nodes in graph G
def compute_degree(G):
    in_deg, out_deg = defaultdict(int), defaultdict(int)
    for v in chain(*G.values()):
        in_deg[v] += 1
    for u, adj in G.items():
        out_deg[u] += len(adj)
    return in_deg, out_deg

def extract_contig(contig):
    contig = [x[0] for x in contig[:-1]] + [contig[-1]]
    return ''.join(contig)


patterns = [line.rstrip() for line in fileinput.input()]

##patterns = ['TAA', 'AAT', 'ATG', 'TGC', 'GCC', 'CCA', 'CAT', 'ATG',
##            'TGG', 'GGG', 'GGA', 'GAT', 'ATG', 'TGT', 'GTT']

G = debruijn(patterns)
contigs = generate_contigs(G)
contigs = map(extract_contig, contigs)

for contig in sorted(contigs):
    print(contig)
