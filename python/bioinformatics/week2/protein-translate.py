
# prepare the codon - amino_acid dict

f = open('RNA_codon_table_1.txt', 'r')

codon_dict = {}

for line in f:
    line = line.split()
    codon = line[0]
    amino_acid = line[1] if len(line) == 2 else ''
    codon_dict[codon] = amino_acid


# read & translate rna

rna = input()
peptide = []
for i in range(0, len(rna) - 2, 3):
    codon = rna[i:i + 3]
    peptide.append(codon_dict[codon])
peptide = ''.join(peptide)

print(peptide)  
    
