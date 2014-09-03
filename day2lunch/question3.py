#!/usr/bin/env python
#determine how many reads align to just 1 location in genome in accepted_hits.sam

sam_output_fname = "/Users/cmdb/tophat_out/accepted_hits.sam"

f = open (sam_output_fname)
# opens file

count = 0
#establishes starting point
for i in f:
# for file 'f', addresses 'i' which is assumed to be an individual line
    if "NH:i:1" in i:
    # finds lines with just 1 match
        count = count + 1
        # adds each good match to the total
print count
#prints answer

#answer 17444398