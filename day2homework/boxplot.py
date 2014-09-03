#!/usr/bin/env python

import pandas as pd
#opened panda


male10_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df = pd.read_table(male10_output)
#opens male10 data
female14d_output = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 =pd.read_table(female14d_output)
#opens female14 data
#columns_of_interest = ["FPKM", "gene_short_name"]
#creates column subset
#df.sort("FPKM", ascending=False)
#df2.sort("FPKM", ascending=False)

male10_1 = df.sort("FPKM", ascending=False)[0:5200]
male10_2 = df.sort("FPKM", ascending=False)[5200:10400]
male10_3 = df.sort("FPKM", ascending=False)[10400:]
#male
female14d_1 = df2.sort("FPKM", ascending=False)[:5200]
female14d_2 = df2.sort("FPKM", ascending=False)[5200:10400]
female14d_3 = df2.sort("FPKM", ascending=False)[10400:]
#female

a_list = []
for i in male10_1["FPKM"], male10_2["FPKM"], male10_3["FPKM"], female14d_1["FPKM"], female14d_2["FPKM"], female14d_3["FPKM"],: 
    a_list.append(i)




import matplotlib.pyplot as plt
#opened matplotlib
#first_male10_female14d = pd.DataFrame({"male": male10_1["FPKM"], "female": female14d_1["FPKM"]})
#establishes dataframe for comparitive plot df vs df2
#second_male10_female14d = pd.DataFrame({"male": male10_2["FPKM"], "female": female14d_2["FPKM"]})
#third_male10_female14d = pd.DataFrame({"male": male10_3["FPKM"], "female": female14d_3["FPKM"]})
plt.figure()
#opens portrait
plt.title("male cycle 10 vs female cycle 14D")
#title
plt.axis([0,100, 0, 100])
plt.boxplot(a_list)
#first_male10_female14d.plot(kind="boxplot")
plt.savefig("boxplotmalefemale.png")