
def suffix_array(text):
    suffixes = sorted(range(len(text)), key=lambda k: text[k:])
    return suffixes

text = input()
suffixes = suffix_array(text)
answer = ', '.join(str(x) for x in suffixes)
print(answer)
    
