from itertools import takewhile

def change(money, coins):
    coins = sorted(coins)
    N = [0] + [money] * (money + 1)
    for m in range(money + 1):
        for coin in takewhile(lambda c: c <= m, coins):
            N[m] = min(N[m], N[m - coin] + 1)
    return N[money]


money = int(input())
coins = map(int, input().split(','))

print(change(money, coins))
        
