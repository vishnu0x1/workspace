
# suffix tree builder
# generates suffix tree using the naive algo

# input dataset already contains the termination symbol '$'

class Node:
    def __init__(self, label, children, leaf):
        self.label = label
        self.children = children
        self.leaf = leaf

    def __repr__(self):
        return '(' + self.label + ', [' \
               + ','.join(str(x) for x in self.children) + '], ' \
               + str(self.leaf) + ')'

class SuffixTree:
    root = Node('#root', [], None)

    def __init__(self, text):
        for k in range(len(text)):
            self.put(text[k:], k)

    def put(self, suf, k):
        j = 0
        x = self.root
        while j < len(suf):
            for child in x.children:
                for i in range(len(child.label)):
                    if child.label[i] != suf[j]:
                        if i > 0:
                            new_node = Node(child.label[i:],
                                            child.children, child.leaf)
                            leaf_node = Node(suf[j:], [], k)
                            child.label = child.label[:i]
                            child.children = [new_node, leaf_node]
                            child.leaf = None
                            return
                        break
                    j += 1
                else:
                    x = child
                    break
            else:
                leaf_node = Node(suf[j:], [], k)
                print (leaf_node, k)
                x.children.append(leaf_node)
                return

    def print_edges(self):
        nodes = self.root.children
        while nodes:
            x = nodes.pop()
            if not x:   continue
            print(x.label)
            nodes.extend(x.children)

##text = input()
##tree = SuffixTree(text)
##tree.print_edges()

s = SuffixTree('')
s.put('a$1', 1)
s.put('a$1', 2)
print(s.root)
