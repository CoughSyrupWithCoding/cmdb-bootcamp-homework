#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt


sxl_FPKM = pd.read_table("/Users/cmdb/cmdb-bootcamp-homework/day2homework/sxl_values.csv", header=None)

plt.figure()

sxl_FPKM.plot(x=None, y=9)
plt.savefig("sxl_FKPM.png")


#FKPM_values = "/Users/cmdb/cmdb-bootcamp-homework/day2homework/sxl_values.csv"
#f = open (FKPM_values)



#FKPM_values = []
#for i, line in enumerate(f):
#    fields = line.rstrip("\r\n").split("\t")
#    if i > 0:
#        FKPM_values.append(fields[9])
#print sorted(FKPM_values)