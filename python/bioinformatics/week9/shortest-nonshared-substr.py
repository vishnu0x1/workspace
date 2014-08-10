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
                    

    def nlcs(self, text1, text2):
        lt1, lt2 = len(text1), len(text2)
        
        for n in range(1, min(lt1, lt2) + 1):
            self.root = Node('#root', [], [])
           
            r1, r2 = range(lt1 - n + 1), range(lt2 - n + 1)

            for k in r2:
                self.put(text2[k:k + n] + '$', k)
                    
            for k in r1:
                search_str = text1[k:k + n]
                if not self.find(search_str + '$'):
                    return search_str
                    

            

s = RadixTree()
print(s.nlcs(input(), input()))


