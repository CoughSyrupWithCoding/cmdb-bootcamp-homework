#!/usr/bin/env python
#determine how many reads align to just 1 location in genome in accepted_hits.sam

sam_output_fname = "/Users/cmdb/tophat_out/accepted_hits.sam"

f = open (sam_output_fname)
# opens file

chrom_loc = []
for i in f:
    fields = i.rstrip("\r\n").split("\t")
    chrom_loc.append(fields[2])
print chrom_loc
