def subsetPermutationBySubtraction():
    mask = 0b11001110
    sub = 0b10000000

    while sub > 0:
        print('sub - 1', bin(sub - 1))
        print('(sub - 1) & mask', bin((sub - 1) & mask))
        sub = (sub - 1) & mask
        print('sub', bin(sub), '\n');

def susbsetPermutationByAddition():
    mask = 0b10101
    add = 0

    while add != mask:
        add = ((~mask | add) + 1) & mask
        print(bin(add)[2:].rjust(5, '0'))


susbsetPermutationByAddition()
