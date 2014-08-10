import functools
import operator
import fileinput

# translate s to charset indices, inefficient algo but serves the purpose
def translate(s, charset='ACGT'):
    return [charset.index(x) for x in s]

# invert from charset indices to corresponding alphabet
def invert(s, charset='ACGT'):
    return ''.join([charset[i] for i in s])

# calc probability of kmer from the profile table
def probability(kmer, profile):
    pr = 1
    for i in range(len(kmer)):
        pr *= profile[i][kmer[i]]
    return pr

def slide(text, k):
    return (text[i:i + k] for i in range(len(text) - k + 1))
    
def profile_most_probable(text, profile, k):
    return max(slide(text, k), key=lambda x: probability(x, profile))

text = input()
k = int(input())
charset = input().split()

profile = [list(map(float, input().split())) for i in range(k)]
text = translate(text, charset)

res = profile_most_probable(text, profile, k)
answer = invert(res)

print(answer)




    
