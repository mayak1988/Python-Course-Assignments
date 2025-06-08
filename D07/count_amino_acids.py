# Each sequence consists of many repetition of the 4 bases represented by the ACTG characters.
# There are 64 codons (sets of 3 bases following each other)
# There are 20 Amino Acids each of them are represented by 3 bases (by one codon).
# Some of the Amino Acids can be represented in multiple ways, represented in the Codon Table. For example Histidine can be encoded by both CAU, CAC
# Create a file called count_amino_acids.py that given a file witha DNA sequence in it, will count the Amino acids from the sequence.
# Read the sequence saved in a txt file.
# You can generate a sequence with a random number generator and save it to that file, but it would be much better if you used a real sequence.
# An even better way would be to read the sequence from a FASTA file. You can download one from NCBI.
# Skeleton:

# examples/dictionary/count_amino_acids_skeleton.py
# codon_table = {
#     'Phe' : ['TTT', 'TTC'],
#     'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
#     'Ile' : ['ATT', 'ATC', 'ATA'],
#     'Met' : ['ATG'],
#     'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
#     'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
#     'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
#     'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
#     'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
#     'Tyr' : ['TAT', 'TAC'],
#     'His' : ['CAT', 'CAC'],
#     'Gln' : ['CAA', 'CAG'],
#     'Asn' : ['AAT', 'AAC'],
#     'Lys' : ['AAA', 'AAG'],
#     'Asp' : ['GAT', 'GAC'],
#     'Glu' : ['GAA', 'GAG'],
#     'Cys' : ['TGT', 'TGC'],
#     'Trp' : ['TGG'],
#     'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
#     'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
#     'STOP' : ['TAA', 'TAG', 'TGA']
# }

import sys


codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Turn codons into a flat dictionary for easy lookup
codon_to_aa = {}
for aa in codon_table:
    for codon in codon_table[aa]:
        codon_to_aa[codon] = aa
  
if len(sys.argv) != 2:
    print("Usage: python count_amino_acids.py sequence_file.fasta")
    exit(1)

else:
    filename = sys.argv[1]
    sequence = ""
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(">"):
                continue  # skip FASTA headers
            sequence += line.strip().upper()
        
    counts = {}
    for i in range(0, len(sequence)-2, 3):
        codon = sequence[i:i+3]
        if codon in codon_to_aa:
            aa = codon_to_aa[codon]
            if aa == 'STOP':
                continue
            if aa not in counts:
                counts[aa] = 0
            counts[aa] += 1
    


    print("Amino acid counts:")
    for aa in sorted(counts.keys()):
        print(f"{aa}: {counts[aa]}")