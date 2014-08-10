import re

def build_codon_dict():
    # modified the file to map STOP codon to symbol '-'
    f = open('RNA_codon_table_1.txt', 'r')
    codon_dict = {}
    for line in f:
        codon, amino_acid = line.split()
        codon_dict[codon] = amino_acid
    return codon_dict

def transcribe_dna(dna):
    return dna.replace('T', 'U')

def translate_rna(rna):
    peptide = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        amino_acid = '-'
        if codon in codon_dict:
            amino_acid = codon_dict[codon]
        peptide.append(amino_acid)
    return ''.join(peptide)

def complement(pattern, s = {'A':'T', 'T':'A', 'G':'C', 'C':'G' }):    
    complement = pattern[::-1]  # create a copy & reverse it
    complement = [s[c] for c in complement]
    return ''.join(complement)

def scan_frames(dna, peptide):
    rna = transcribe_dna(dna)
    # scan through the 3 frames
    for i in range(3):        
        amino_acid_seq = translate_rna(rna[i:])     # amino acid sequence
        for m in re.finditer(peptide, amino_acid_seq):
            yield (i + 3*m.start(), i + 3*m.end())

dna = input()
peptide = input()

codon_dict = build_codon_dict()
for seq in scan_frames(dna, peptide):
    print(dna[seq[0] : seq[1]])     # the dna pattern that produced the peptide
for seq in scan_frames(complement(dna), peptide):
    print(dna[-seq[1] : -seq[0]])   # the dna pattern whose
                                    # "complement" produced the peptide

