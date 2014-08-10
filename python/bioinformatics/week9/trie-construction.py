
import fileinput

class Node:
    def __init__(self):
        self.val = None
        self.next = [None] * 4

class Trie:
    root = None
    radix = 4
    
    def put(self, key, val):
        self.root = self.putValue(self.root, key, val, 0)

    def putValue(self, x, key, val, d):
        if not x:
            x = Node()
        if d == len(key):
            x.val = val
            return x
        c = key[d]
        x.next[c] = self.putValue(x.next[c], key, val, d + 1)
        return x

    def printTrie(self):
        self.printNode(self.root, 1)

    def printNode(self, root, v):
        u, v = v, v + 1
        for i in range(self.radix):
            if root.next[i]:
                output_edge(u, v, i)
                v = self.printNode(root.next[i], v)
        return v

def indices(text, s='ACTG'):
    return [s.index(x) for x in text]

def output_edge(u, v, i, s='ACTG'):
    print(u, v, s[i])
    

trie = Trie()
for line in fileinput.input():
    line = line.rstrip()
    trie.put(indices(line), None)
    
trie.printTrie()

