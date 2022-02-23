#!/usr/bin/python3
################################################################################
# Rosalind: Counting DNA Nucleotides
################################################################################
dna_seq = input("\nEnter DNA sequence: ")


def get_base_counts(dna):

    counts = {'A': 0,
              'C': 0,
              'G': 0,
              'T': 0}
    for base in dna:
        counts[base] += 1
    return counts


print("\nCalculate base counts: ")
print(get_base_counts(dna_seq))
