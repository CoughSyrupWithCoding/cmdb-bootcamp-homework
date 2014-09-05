#!/usr/bin/env python


import sys
from fasta import FASTAReader


reader = FASTAReader(sys.stdin)
#calling fastareader from before
sequence_list = []
for sid, sequence in reader:
    sequence_list.append(sid[:30] + ":" + sequence)
    
#print sequence_list
sorted_list = sorted(sequence_list, key=len, reverse=True)
#key=len writes in length, reverse=True gives highest at top

    #combining the first part of the seq_id with the sequence in order to make them items in a list to be sorted
    
longest_sequences = sorted_list[:100]
#here is the list

#print longest_sequences
test_list = longest_sequences[98:]
basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
reverse_comp_sequeneces = []
for i in test_list:
    rev_seq = "".join[i[::-1]]
    rev_comp = [basecomplement[b] for b in rev_seq]
    rev_comp_str = "".join(rev_comp)
    reverse_comp_sequences.append(rev_comp_str)
#displays top 100 strings
print reverse_comp_sequences