# Create a file called dna_sequencing.py
# A, C, T, G are called bases or nucleotides
# Accept a sequence on the command line like this: python dna_sequencing.py ACCGXXCXXGTTACTGGGCXTTGTXX
# Given a sequence such as the one above (some nucleotides mixed up with other elements represented by an X)
# First return the sequences containing only ACTG. The above string can will be changed to ['ACCG', 'C', 'GTTACTGGGC', 'TTGT'].
# Then sort them by lenght. Expected result: ['GTTACTGGGC', 'ACCG', 'TTGT', 'C']

seq = input()
