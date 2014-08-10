import fileinput

def debrujin(kmers):
    node_dict = {}
    for i, kmer in enumerate(kmers):
        lnode, rnode = kmer[:-1], kmer[1:]
        if lnode in node_dict:
            node_dict[lnode] += (i, )
        else:
            node_dict[lnode] = [i]
    for lnode, rnode_indices in node_dict.items():
        yield lnode, rnode_indices
        

kmers = [line.rstrip() for line in fileinput.input()]

# sorting logic necessary for test acceptance
for lnode, rnode_indices in sorted(debrujin(kmers)):
    rnodes = [kmers[i][1:] for i in rnode_indices]
    rnodes = sorted(rnodes)
    rnodes = ','.join(rnodes)
    print(lnode, '->', rnodes)
