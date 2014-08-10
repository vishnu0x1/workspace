import fileinput

def overlap(patterns):
    left_dict = {}
    right_dict = {}
    for i, p in enumerate(patterns):
        lstr, rstr = p[:-1], p[1:]
        
        if rstr not in left_dict:
            right_dict[rstr] = i
        else:
            q = patterns[left_dict.pop(rstr)]
            yield p, q
            
        if lstr not in right_dict:
            left_dict[lstr] = i
        else:
            q = patterns[right_dict.pop(lstr)]
            yield q, p


patterns = [line.rstrip() for line in fileinput.input()]
for p, q in overlap(patterns):
    print(p, '->', q)
