pattern = input()
text = input()
d = int(input())

k = len(pattern)
l = len(text)

def check_match(text, pattern, d):
    mismatches = 0
    for j in range(len(pattern)):
        if text[j] != pattern[j]:
            mismatches += 1
            if mismatches > d:
                return False
    return True

indices = []
for i in range(l - k + 1):
    if check_match(text[i:i + k], pattern, d):
        indices.append(i)

answer = ' '.join(str(x) for x in indices)
print(answer)
