import re
import fileinput
from itertools import filterfalse

# global vars associated with algo
explored = None
time = None
dist = None
parent = None

class Edge:
    def __init__(self, fro, to, weight):
        self.fro = fro
        self.to = to
        self.weight = weight

def topological_sort(u):
    global explored, time
    time, explored = [], [False] * len(G)
    dfs_visit(u)
    time = time[::-1]

def dfs_visit(u):
    global explored, time
    explored[u] = True
    for edge in filterfalse(lambda e: explored[e.to], G[u]):
        dfs_visit(edge.to)
    time.append(u)


def longest_path(u):
    global dist, parent
    dist, parent = [0] * len(G), [0] * len(G)
    topological_sort(u)
    for u in time:
        for edge in G[u]:
            d = dist[u] + edge.weight
            if d > dist[edge.to]:
                dist[edge.to], parent[edge.to] = d, u

def extract_path(source, sink):
    u, path = sink, [sink]
    while u !=  source:
        u = parent[u]
        path.append(u)
    return path[::-1]


source, sink = int(input()), int(input())
G = [[] for _ in range(100)]        # limit pre-decided

# with help of debuggex.com: '(\d+)->(\d+):(\d+)'
for line in fileinput.input():
    m = re.match('(\d+)->(\d+):(\d+)', line)
    u, v, w = int(m.group(1)), int(m.group(2)), int(m.group(3))
    G[u].append(Edge(u, v, w))


longest_path(source)
path = extract_path(source, sink)

answer = '->'.join(map(str, path))
print(dist[sink])
print(answer)

