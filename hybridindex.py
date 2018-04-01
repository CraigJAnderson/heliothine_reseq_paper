#!/usr/bin/python
import pandas as pd
import numpy as np
import sys
import getopt

def main(argv):
   variants = ''
   genomewindows = ''
   out_window_averages = ''
   try:
      opts, args = getopt.getopt(argv,"v:g:o:",["variants=","genomewindows=","out_window_averages="])
   except getopt.GetoptError:
      print ('hybridindex.py -v <variants> -g <genomewindows> -o <out_window_averages>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('hybridindex.py -v <variants> -g <genomewindows> -o <out_window_averages>')
         sys.exit()
      elif opt in ("-v", "--variants"):
         snpfile = arg
      elif opt in ("-g", "--genomewindows"):
         oldmapfile = arg
      elif opt in ("-o", "--out_window_averages"):
         newmapfile = arg
if __name__ == "__main__":
   main(sys.argv[1:])

df2 = pd.read_table((sys.argv[4]),sep='\t',names=['bin','chr','bp'])
df1 = pd.read_table((sys.argv[2]),sep='\t',names=['chr','bp','snp_name','sample'])
result = df2.append(df1)
result1 = result.sort_values(['chr', 'bp'], ascending=[True, True])
result1['bin'] = result1['bin'].fillna(method='pad')
result1 = result1.dropna(axis=0)
out = result1.groupby(by=['bin'])['sample'].mean().reset_index()
out.columns = ['bin','HI']
out.to_csv((sys.argv[6]), sep='\t',index=False,header=True)
print ('Success!')
