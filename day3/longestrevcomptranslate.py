#!/usr/bin/env python


import sys
from fasta import FASTAReader

basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

dna_codon_dict = { "TTT" : "F", "TCT" : "S", "TAT" : "Y", "TGT" : "C", \
"TTC" : "F", "TCC" : "S", "TAC" : "Y", "TGC" : "C", \
"TTA" : "L", "TCA" : "S", "TAA" : ".", "TGA" : ".", \
"TTG" : "L", "TCG" : "S", "TAG" : ".", "TGG" : "W", \
"CTT" : "L", "CCT" : "P", "CAT" : "H", "CGT" : "R", \
"CTC" : "L", "CCC" : "P", "CAC" : "H", "CGC" : "R", \
"CTA" : "L", "CCA" : "P", "CAA" : "Q", "CGA" : "R", \
"CTG" : "L", "CCG" : "P", "CAG" : "Q", "CGG" : "R", \
"ATT" : "I", "ACT" : "T", "AAT" : "N", "AGT" : "S", \
"ATC" : "I", "ACC" : "T", "AAC" : "N", "AGC" : "S", \
"ATA" : "I", "ACA" : "T", "AAA" : "K", "AGA" : "R", \
"ATG" : "M", "ACG" : "T", "AAG" : "K", "AGG" : "R", \
"GTT" : "V", "GCT" : "A", "GAT" : "D", "GGT" : "G", \
"GTC" : "V", "GCC" : "A", "GAC" : "D", "GGC" : "G", \
"GTA" : "V", "GCA" : "A", "GAA" : "E", "GGA" : "G", \
"GTG" : "V", "GCG" : "A", "GAG" : "E", "GGG" : "G" }



reader = FASTAReader(sys.stdin)
#calling fastareader from before
sequence_list = []
for sid, sequence in reader:
    sequence_list.append(sequence)
#print sequence_list
sorted_list = sorted(sequence_list, key=len, reverse=True)
#key=len writes in length, reverse=True gives highest at top

    #combining the first part of the seq_id with the sequence in order to make them items in a list to be sorted
    
longest_sequences = sorted_list[:100]
#here is the list

#print longest_sequences
test_list = longest_sequences[98:]

reverse_comp_sequeneces = []
for i in longest_sequences:
    rev_seq = "".join[i[::-1]]
    rev_comp = "".join([basecomplement[b] for b in rev_seq])
    rev_comp_str = "".join(rev_comp)
    reverse_comp_sequences.append(rev_comp_str)
#displays top 100 strings
print reverse_comp_sequences

def translate(seq, frame):  #frame either 1, 2 or 3
    proteinSeq = []
    i = frame - 1
    while i+2 < len(seq):
        codon = seq[i:i+3]
        aminoacid = dna_codon_dict[codon]
        proteinSeq.append(aminoacid)
        i += 3
    return "".join(proteinSeq)