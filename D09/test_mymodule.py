import random
import pytest
from MyModule import count_amino_acids, generate_random_dna_sequence

def test_count_amino_acids_simple():
    codon_map = {'ATG': 'Met', 'GTT': 'Val', 'TAA': 'STOP'}
    seq = "ATGGTTTAA"
    result = count_amino_acids(seq, codon_map)
    assert result == {'Met': 1, 'Val': 1}

def test_generate_random_dna_sequence_length_and_content():
    random.seed(42)  # ensure deterministic output
    seq, codon_map = generate_random_dna_sequence(5)
    assert len(seq) == 15
    assert all(c in "ATGC" for c in seq)
    assert isinstance(codon_map, dict)

def test_count_amino_acids_with_generated_seq():
    random.seed(1)
    seq, codon_map = generate_random_dna_sequence(10)
    result = count_amino_acids(seq, codon_map)
    total = sum(result.values())
    assert total == 10  # total amino acids = 10
def test_dummy_in_mymodule():
    assert True