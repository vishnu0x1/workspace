
def count_breakpoints(perm):
    count = 0
    for i in range(len(perm) - 1):
        if perm[i] + 1 != perm[i + 1]:
            count = count + 1
    return count


text = input()
perm = list(map(int, text[1:-1].split()))

print(count_breakpoints(perm))
