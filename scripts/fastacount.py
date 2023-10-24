#!/usr/bin/env python

import sys

def count_fasta_headers(file_path):
    with open(file_path, 'r') as fasta_file:
        count = 0
        for line in fasta_file:
            if line.startswith('>'):
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fastacount.py <fasta_file>")
        sys.exit(1)
    
    fasta_file_path = sys.argv[1]
    header_count = count_fasta_headers(fasta_file_path)
    print(f"Number of fasta sequence in {fasta_file_path}: {header_count}")
