
cards = [10, 20, 21, 30, 31]
cards = sorted(cards)

l = 1   # base case: cards will contain atleast one element
        # so l is atleast 1

# scan from second element onwards
for i in range(len(cards) - 1):
    if cards[i + 1] == cards[i] + 1:
        cards[i + 1] = 0
    else:
        l += 1

print(l)
