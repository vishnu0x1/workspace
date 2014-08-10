
s = "a"

# let x = prefix of s, y = suffix : y = s - x
# s  = x +     y  + rev(x), and s' = rev(s)
# s' = x + rev(y) + rev(x)
# find largest suffix y : y == rev(y)

i = 0
for i in range(len(s)):
    if (s[i:]) == (s[:i-1:-1]):
        break

print(len(s) + i)
