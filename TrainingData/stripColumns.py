
import sys
import os
import csv
import pathlib
import click
import csv
import pandas as pd

try:
    trainingFileName = sys.argv[1]
except IndexError:
    print("No csv file specified run with:")
    print("pyhton csvTagger.py FILENAME.csv")
    exit()

# with open(trainingFileName+".csv","rb") as source:
#     rdr= csv.reader( source )
#     with open("stripped.csv","wb") as result:
#         wtr= csv.writer( result )
#         for r in rdr:
#             wtr.writerow(str(r[0]), str(r[3]))

colnames=['comment', 'upvote', 'id', 'label'] 

f=pd.read_csv(trainingFileName, names=colnames, header=None)
keep_col = ['comment','label']
new_f = f[keep_col]
new_f.to_csv("stripped.csv", index=False)