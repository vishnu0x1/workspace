import math

h,u,d,ff = 4,4,3,18
f = ff / 100

n = 1
climb = u   # distance climbed on nth day
ht = u      # ht = current height of snail

# if ht exceeds h, then snail climbs out
# if ht < d, then snail will slide down to ht - d by end of day
#           which is negative, then it's failure
while ht >= d and ht <= h:
    print(n, climb, ht)
    n = n + 1
    climb = max(0, climb - f*u)     # max(x, 0) = x & -(x > 0)
    ht += climb - d
    
print(n, climb, ht)



