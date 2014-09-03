#!/usr/bin/env python
#determine how many perfect alignments are in accepted_hits.sam

sam_output_fname = "/Users/cmdb/tophat_out/accepted_hits.sam"

f = open (sam_output_fname)
# opens file

count = 0
#establishes starting point
for i in f:
# for file 'f', addresses 'i' which is assumed to be an individual line
    if "NM:i:0" in i:
    # finds lines with exact matches
        count = count + 1
        # adds each perfect match to the total
print count
#prints answer

#answer 14079052