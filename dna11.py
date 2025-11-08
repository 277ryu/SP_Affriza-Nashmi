# Checkpoint 1.1

from collections import Counter

dna = input("Enter a DNA sequence (A, T, C, G): ")
k_len = int(input("Enter k (substring): "))

kmers = [dna[i:i+k_len] for i in range(len(dna) - k_len + 1)]

hitung_kmers = Counter(kmers)
print("K-mer count: ")
for kmer, count in hitung_kmers.items():
    print("%s:%d" % (kmer, count))

# References:
# https://stackoverflow.com/questions/19920733/python-3-k-mers-count-errors
# https://stackoverflow.com/questions/49188432/counting-maximum-k-mer-repetition-frequency