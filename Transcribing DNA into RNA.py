#!/usr/bin/python3
################################################################################
# Rosalind: Transcribing DNA into RNA
################################################################################
dna_seq = input("\nEnter DNA sequence to translate: ")


def dna2rna(dna):
    nuc = list(dna)
    for i in range(len(dna)):
        if nuc[i] == 'T':
            nuc[i] == 'U'
        else:
            continue


print("\nRNA sequence: ")
print(dna2rna(dna_seq))
