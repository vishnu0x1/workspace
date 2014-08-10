def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = 1 - parity
        int_type = int_type & (int_type - 1)
    return(parity)

parity_bits = []

for i in range(32):
    i_str = bin(i)[2:]
    i_str = i_str.rjust(5, '0')
    i_parity = parityOf(i)
    print(i_str, " ", i_parity)
    parity_bits.append(str(i_parity))

print(''.join(parity_bits))


