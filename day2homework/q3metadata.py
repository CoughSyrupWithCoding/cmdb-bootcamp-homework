#!/usr/bin/env python

import pandas as pd
import csv
female10 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
female11 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
female12 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
female13 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
female14a = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
female14b = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
female14c = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
female14d = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
#naming all data files

file_list = []
file_list.append(female10)
file_list.append(female11)
file_list.append(female12)
file_list.append(female13)
file_list.append(female14a)
file_list.append(female14b)
file_list.append(female14c)
file_list.append(female14d)
#compiling list of all data files

sxl_list = []

for i in file_list:
    with open(i) as df:
        for row in df:
            if "Sxl" in row:
                sxl_list.append(row)
print sxl_list

#csv requires list of lists
list_of_lists = []
for i in sxl_list:
    list_of_fields = []
    fields = i.rstrip("\r\n").split("\t")
    #splits all text at \t
    #fields holds all columns
    for field in fields:
        list_of_fields.append(field)
        #each column now becomes an item in a list
    list_of_lists.append(list_of_fields)
    #new lists are combined to be list of lists

print list_of_lists


with open('sxl_values.csv', 'wb') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(list_of_lists)

#works!
#we want column 10

#looks in gene short name column and finds matches for tRNA, comes back as true or false
#tRNAs = df["gene_short_name"].str.contains("tRNA")
#makes group for tRNA genes
#print df[pd.isnull(df)["gene_short_name"]]
#prints row of nan gene that's gumming up the works