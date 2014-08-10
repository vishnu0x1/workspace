tree = [8,
            [3,
                 [1, [], []],
                 [6,
                      [4, [], []],
                      [7, [], []]]],
            [10,
                 [],
                 [14,
                      [13, [], []],
                      []]]]
def postorder(tree):
    if not tree:
        return
    sum = tree[0]
    stack = []
    stack.append(tree)
    prevNode = []
    while stack:
        currNode = stack[-1]
        if not prevNode or prevNode[1] == currNode or prevNode[2] == currNode:
            if currNode[1]:
                stack.append(currNode[1])
                sum += currNode[1][0]
            elif currNode[2]:
                stack.append(currNode[2])
                sum += currNode[2][0]
        elif currNode[1] == prevNode:
            if currNode[2]:
                stack.append(currNode[2])
                sum += currNode[2][0]
        else:
            print(currNode[0], sum)
            sum -= currNode[0]
            stack.pop()
        prevNode = currNode

# cut k heavy weight paths in bst, if k < cut_off
def kMinorWeights(node, k, cut_off):
    if not node:
        return k
    lsum = kMinorWeights(node[1], k + node[0], cut_off)
    rsum = kMinorWeights(node[2], k + node[0], cut_off)
    if lsum < cut_off:
        node[1] = []
    if rsum < cut_off:
        node[2] = []
    return max(lsum, rsum)

# cut k heavy weight paths in bst, if k < cut_off
def cutMinorWeights(root, cut_off):
    if kMinorWeights(root, 0, cut_off) < cut_off:
        del root[:]

#postorder(tree)
cutMinorWeights(tree, 22)

print(tree)
