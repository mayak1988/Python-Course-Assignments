import random 
def read_sequence(filename):
    sequence = ""
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(">"):
                continue  
            sequence += line.strip().upper()
    return sequence


def count_amino_acids(seq,codon_to_aa):
    """
    Count amino acids from a DNA sequence using a codon-to-amino-acid mapping.

    Splits the DNA sequence into codons (triplets) and translates it to an amino acid, while ignoring stop codons,
    and returns the frequency of each amino acid.

    Args:
        seq (str): DNA sequence (e.g., "ATGGTTTAA").
        codon_to_aa (dict): Dictionary mapping codons to amino acids (For example: "ATG" to "Met").

    Returns:
        dict: Dictionary with amino acid names as keys and their counts as values.

    Example:
        >>> codon_map = {'ATG': 'Met', 'GTT': 'Val', 'TAA': 'STOP'}
        >>> count_amino_acids("ATGGTTTAA", codon_map)
        {'Met': 1, 'Val': 1}
    """
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

def generate_random_dna_sequence(num_amino_acids):
    """
    Generate a random DNA sequence encoding a given number of amino acids (excluding STOP).
    Args:
        num_amino_acids (int): Number of amino acids in the sequence.
    Returns:
        str: A DNA sequence composed of randomly selected codons.

    Example:
        >>> seq, codon_map = generate_random_dna_sequence(5)
        >>> len(seq) % 3 == 0
        True
        >>> all(base in 'ATGC' for base in seq)
        True
        >>> len(seq) == 15
        True
    """
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
    
    aa_list = [aa for aa in codon_table if aa != "STOP"]
    sequence = ""

    for _ in range(num_amino_acids):
        aa = random.choice(aa_list)
        codon = random.choice(codon_table[aa])
        sequence += codon

    return sequence,codon_to_aa



    
