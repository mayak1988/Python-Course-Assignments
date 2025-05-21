# Create a file called extended_dna_sequencing.py
# In this case the original string contains more than on type of foreign elements: e.g. 'ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX'.
# Expected output: ['TGGGC', 'ACCG', 'TTGT', 'GTT', 'AC', 'T']
# Ask for a sequence on the Standard Input (STDIN) like this:

# python extended_dna_sequencing.py
# Please type in a sequence:

import re

seq = input('Please type in a sequence: ')
# print(seq)
cleaned = re.sub(r'[^ACGT]', ' ', seq.upper())
list =cleaned.split(' ')
cleaned_list = [item for item in list if item]
sorted_list = sorted(cleaned_list, key=len, reverse=True)
print(sorted_list)
