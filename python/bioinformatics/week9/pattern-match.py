
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

    def prefixMatch(self, key, val):
        return self.prefixMatchValue(self.root, key, val, 0)

    def prefixMatchValue(self, x, key, val, d):
        if not x:
            return False
        if x.val == val:
            return True
        if d < len(key):
            c = key[d]
            return self.prefixMatchValue(x.next[c], key, val, d + 1)

def indices(text, s='ACTG'):
    return [s.index(x) for x in text]


trie = Trie()
text = input()
text = indices(text)
for line in fileinput.input():
    line = line.rstrip()
    trie.put(indices(line), '$')

answer = [str(k) for k in range(len(text)) if trie.prefixMatch(text[k:], '$')]
answer = ' '.join(answer)
print(answer)
        

