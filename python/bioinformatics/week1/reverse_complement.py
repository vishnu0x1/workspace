
pattern = list(input())

d = {'A':'T', 'T':'A', 'G':'C', 'C':'G' }
complement = pattern[::-1]  # create a copy & reverse it
complement = [d[c] for c in complement]

answer = ''.join(complement)
print(answer)
