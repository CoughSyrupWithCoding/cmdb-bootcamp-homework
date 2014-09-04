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
print len(longest_sequences)

#displays top 100 strings
