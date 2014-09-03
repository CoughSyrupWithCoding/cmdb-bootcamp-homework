#!/usr/bin/env python
#determine how many alignments are in accepted_hits.sam

sam_output_fname = "/Users/cmdb/tophat_out/accepted_hits.sam"

f = open (sam_output_fname)
# opens file

count = 0
#establishes starting point
for i in f:
# for file 'f', addresses 'i' which is assumed to be an individual line
    count = count + 1
    # adds each new line to preceding count
print count
#prints answer

#answer 18417195