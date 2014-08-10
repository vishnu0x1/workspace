
import sys

class Node:
    def __init__(self):
        self.val = None
        self.next = [None] * radix

class Trie:
    root = None
    
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
    
    def get(self, key):
        return self.getValue(self.root, key, 0)
    
    def getValue(self, x, key, d):
        if not x:   return
        if d == len(key):
            return x.val
        c = key[d]
        return self.getValue(x.next[c], key, d + 1)
         

def longestRepeat(text):
    l = len(text)
    srange = range(l)
    for n in range(1, l + 1):
        trie = Trie()
        nsrange = set()
        for k in srange:
            search_str = text[k:k + n]
            val = trie.get(search_str)
            if val is None:
                trie.put(search_str, k)
            elif val <= l - n:
                nsrange |= { val, k }
        if not nsrange:
            s = srange.pop()
            return s, n - 1
        srange = nsrange
    
def indices(text, s='ACTG'):
    return [s.index(x) for x in text]


radix = 4
text = input()
sys.setrecursionlimit(2**14)    # 2^10 * 16

kmer_indices = indices(text.rstrip())
s, n = longestRepeat(kmer_indices)
print(text[s:s + n])


