import sys
from MyModule import read_sequence,count_amino_acids,generate_random_dna_sequence
import random
import doctest
import MyModule

doctest.testmod(MyModule)

if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("Usage: python count_amino_acids_with_module.py")
        exit(1)
    #generate a random number of amio acids
    num_aa = random.randint(1, 50)  # Random number between 1 and 50
    seq,codon_to_aa = generate_random_dna_sequence(num_aa)

    # filename = sys.argv[1]
    # dna = read_sequence(filename)
    aa_counts = count_amino_acids(seq,codon_to_aa)

    print("Amino acid counts:")
    for aa in sorted(aa_counts.keys()):
        print(f"{aa}: {aa_counts[aa]}")