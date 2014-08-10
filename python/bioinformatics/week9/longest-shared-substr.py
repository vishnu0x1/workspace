
class SuffixTree:
    root = ['', []]     # first: label, second: children

    def addText(self, text):
        for k in range(len(text)):
            self.put(text[k:])
    
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

    def f(self, r):
        x, c = r[0], r[1]
        
        if x[-1:] == '$':
            return x[:-1]

        if x[-2:] == '$1' or x[-2:] == '$2':
            return x[-2:]

        cfx = [self.f(cr) for cr in c]
        cfxd = [p for p in cfx if p != '$1' and p != '$2']
        if cfxd:
            return x + max(cfxd, key=len)
        return x


text1 = 'pilosana'
text2 = 'namiloma'

tree = SuffixTree()
tree.addText(text1 + '$1')
tree.addText(text2 + '$2')
tree.collapse()
print(tree.f(tree.root))
print(tree.root)

