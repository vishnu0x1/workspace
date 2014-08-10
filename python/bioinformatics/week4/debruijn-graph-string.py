
def debruijn(text, k):
    node_dict = {}
    for i in range(len(text) - k + 1):
        lnode = text[i:i + k - 1]
        rnode = text[i + 1:i + k]
        if lnode in node_dict:
            node_dict[lnode] += (i + 1, )
        else:
            node_dict[lnode] = [i + 1]
    for lnode, rnode_indices in node_dict.items():
        yield lnode, rnode_indices
        

k = int(input())
text = input()

# sorting logic necessary for test acceptance
for lnode, rnode_indices in sorted(debruijn(text, k)):
    rnodes = [text[i:i + k - 1] for i in rnode_indices]
    rnodes = sorted(rnodes)
    rnodes = ','.join(rnodes)
    print(lnode, '->', rnodes)
