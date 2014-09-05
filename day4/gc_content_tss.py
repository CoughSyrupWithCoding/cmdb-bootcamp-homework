#!/usr/bin/env python
import sys



#dfp.read_table=(positive_strands, names = (["0", "1", "2", "3", "4", "5", "6", "7", "8"]))
#dff.read_table=(negative_strands, names = (["0", "1", "2", "3", "4", "5", "6", "7", "8"]))

#print dfp.read_table


from fasta import FASTAReader
#imports the parser that we made

reader = FASTAReader(sys.stdin)


positive_strands = "/Users/cmdb/data/results/SRR072893_clout/transcripts_plus.csv"
negative_strands = "/Users/cmdb/data/results/SRR072893_clout/transcripts_minus.csv"

first_line =[]
for line in open(positive_strands):
    a, b ,c ,d ,e ,f ,g, h ,i =line.split("\t")
    start = int(d) - 250
    end = int(d) + 250
    chrom = str(a)
for line in open(negative_strands):
    a, b ,c ,d ,e ,f ,g, h ,i =line.split("\t")
    start = int(e) - 250
    end = int(e) + 251
    chrom = str(a)

k = 500
#length of 'word'

kmers = {}
#establishes that we are creating dict

for chrom, sequence in reader:
    #looks at lines marked sequence
    for i in range(start, end):
        #iterates for sequence starting a 'start' and ending at 'end' every 500
        kmer = sequence[i:i+k]
        #extracts each word of length 11
        if kmer not in kmers:
            kmers[kmer] = 1
            #if is isn' dict, we say we've seen in once
        else:
            kmers[kmer] += 1
            #if we've already seen it, add to sightings in dict
            
for key in kmers:
    #key = how you look up sequence, the 11mer
    print key, kmers[key]
