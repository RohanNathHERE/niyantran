#!/usr/bin/env python

import re
import sys

def extract_species(file_path):
    species_set = set()
    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            if line.startswith('>'):
                matches = re.findall(r'\[(.*?)\]', line)
                for match in matches:
                    species_set.add(match)
    return species_set

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./get_species.py <fasta_file>")
        sys.exit(1)
    
    fasta_file_path = sys.argv[1]
    unique_species = extract_species(fasta_file_path)
    for species in unique_species:
        print(species)