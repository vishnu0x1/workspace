from itertools import chain

class Node:
    def __init__(self, label, children, leaf):
        self.label = label
        self.children = children
        self.leaf = leaf

    def __repr__(self):
        return '(' + self.label + ', [' \
               + ','.join(str(x) for x in self.children) + '], ' \
               + str(self.leaf) + ')'

class RadixTree:
    root = Node('#root', [], [])     # first: label, second: children, third: leaf#

    def put(self, suf, k):
        j = 0
        x = self.root
        while True:
            for child in x.children:
                for i in range(len(child.label)):
                    if child.label[i] != suf[j]:
                        if i > 0:
                            new_node = Node(child.label[i:],
                                            child.children, child.leaf)
                            leaf_node = Node(suf[j:], [], [k])
                            child.label = child.label[:i]
                            child.children = [new_node, leaf_node]
                            child.leaf = []
                            return
                        break
                    j += 1
                else:
                    x = child
                    break
            else:
                if x.leaf:
                    x.leaf.append(k)
                else:
                    leaf_node = Node(suf[j:], [], [k])
                    x.children.append(leaf_node)
                return

    def find(self, text):
        x = self.root
        j = 0
        while not x.leaf:
            for child in x.children:
                if text.startswith(child.label, j):
                    x = child
                    j += len(child.label)
                    break
            else:
                return []
        return x.leaf
                    

    def lcs(self, text1, text2):
        maxn = min(len(text1), len(text2))
        r1, r2 = range(len(text1)), range(len(text2))
        
        for n in range(1, maxn + 1):
            self.root = Node('#root', [], [])
           
            for k in r1:
                self.put(text1[k:k + n] + '$', k)
                    
            nr1, nr2 = set(), set()
            for k in r2:
                for j in self.find(text2[k:k + n] + '$'):
                    if j <= len(text1) - n and k <= len(text2) - n:
                        nr1.add(j)
                        nr2.add(k)

            if not nr1:   break
            
            r1, r2 = nr1, nr2

        return r1, r2
            

s = RadixTree()
s.lcs(input(), input())
# choose any of the lcs, here zeroth one
print(s.root.children[0].label[:-2])

