text = input()

skew = 0
min_skew = len(text)    # max possible value, string of all Gs or Cs
min_skew_index = []

for i in range(len(text)):
    if text[i] == 'G':
        skew += 1
    elif text[i] == 'C':
        skew -= 1
    if skew < min_skew:
        min_skew = skew
        min_skew_index = [i]
    elif skew == min_skew:
        min_skew_index.append(i)

# output required is over one based indices
answer = ' '.join(str(x + 1) for x in min_skew_index)
print(answer)
    
