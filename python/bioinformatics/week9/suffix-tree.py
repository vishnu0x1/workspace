
# suffix tree builder
# generates suffix tree by collapsing edges of suffix trie

# input dataset already contains the termination symbol '$'

class SuffixTree:
    root = ['', []]     # first: label, second: children

    def __init__(self, text):
        for k in range(len(text)):
            self.put(text[k:])
        self.collapse()
    
    def put(self, suffix):
        root = self.root
        for x in suffix:
            for child in root[1]:
                if x == child[0]:
                    # child label matches suffix char x
                    root = child
                    break
            else:
                # root has empty children, or no child has label x
                new_child = [x, []]
                root[1].append(new_child)
                root = new_child
        
    def collapse(self):
        nodes = [self.root]
        while nodes:
            x = nodes.pop()
            children = x[1]
            if len(children) == 1:
                # collapse node with its only child
                x[0] += children[0][0]
                x[1] = children[0][1]
                nodes.append(x)
            elif len(children) > 1:
                # scan deeper
                nodes.extend(children)

    def print_edges(self):
        nodes = self.root[1]
        while nodes:
            x = nodes.pop()
            if not x: continue
            print (x[0])
            nodes.extend(x[1])
               

text = input()
tree = SuffixTree(text)
tree.print_edges()
