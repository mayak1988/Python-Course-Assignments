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


codon_to_aa = {}
for aa in codon_table:
    for codon in codon_table[aa]:
        codon_to_aa[codon] = aa


def read_sequence(filename):
    sequence = ""
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(">"):
                continue  
            sequence += line.strip().upper()
    return sequence


def count_amino_acids(seq):
    counts = {}
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        if codon in codon_to_aa:
            aa = codon_to_aa[codon]
            if aa == 'STOP':
                continue
            if aa not in counts:
                counts[aa] = 0
            counts[aa] += 1
    return counts

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids.py sequence_file.fasta")
        exit(1)

    filename = sys.argv[1]
    dna = read_sequence(filename)
    aa_counts = count_amino_acids(dna)

    print("Amino acid counts:")
    for aa in sorted(aa_counts.keys()):
        print(f"{aa}: {aa_counts[aa]}")