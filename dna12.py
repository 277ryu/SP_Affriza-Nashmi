# Checkpoint 1.2

from collections import Counter

dna = input("Enter a DNA sequence (A, T, C, G): ")
k_len = int(input("Enter k (substring): "))

kmers = [dna[i:i+k_len] for i in range(len(dna) - k_len + 1)]

hitung_kmers = Counter(kmers)
print("K-mer count: ")
for kmer, count in hitung_kmers.items():
    print("%s:%d" % (kmer, count))
    
def complement(dna):
    comp = {'A':'T','T':'A','G':'C','C':'G'} # pasangan nukleotida
    comp_dna = ''
    for b in dna:
        comp_dna += comp[b]
    return comp_dna

def reverse(dna):
    return dna[::-1] # urutan dimulai dari paling belakang

def reverse_complement(dna):
    comp_dna = complement(dna)
    revcomp_dna= reverse(comp_dna)
    return revcomp_dna

comp_dna = complement(dna)
print("DNA complement: '%s'" % (comp_dna))
revcomp_dna = reverse_complement(dna)
print("Reverse DNA complement: '%s'" % (revcomp_dna))
print("\nCheck reverse complement: ")
for kmer, count in hitung_kmers.items():
    revcomp = reverse_complement(kmer)
    print(f"{kmer} <-> {revcomp}")

# References:
# Professor Hendrix & Bioinformatics with Ease on Youtube