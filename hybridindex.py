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
      opts, args = getopt.getopt(argv,"v:g:o:",["variants=","genomewindows","out_window_averages="])
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
df1 = pd.read_table((sys.argv[4]),sep='\t',names=['chr','bp','snp_name','sample'])
df2 = pd.read_table((sys.argv[2]),sep='\t',names=['bin','chr','bp'])
length = len(df2.index)
#the next two lines create a table of new rs values the length of your SNP list. This list is purely numerical and sequential, but should differ from a downloaded dataset to avoid duplicate names.
t=np.arange(1,length+1,1)
dfa = pd.DataFrame({'rs': t})
#adds SNP idents to your linkage map data
dfb = pd.concat([dfa, df2], axis=1)
#merges the old .map data with your indexed linkage map data
df3 = pd.merge(df1, dfb, how="outer")
print ('Adding numerical SNP idents, ensure these are unique!')
df4 = df3.sort_values(by=['chr', 'bp'], ascending=[True, True])
## if interpolation of distance required, unhash ## df5 = df4.interpolate()
#the following line fills empty values
df6 = df4.fillna(method='pad')
df7 = df6.drop_duplicates(keep='last')
#Turn the folowing columns into integers and turn off the pandas warning
cols = ['chr', 'bp']
pd.set_option('chained_assignment',None)
df7[cols] = df7[cols].applymap(np.int64)
df7.to_csv((sys.argv[6]), sep='\t',index=False,header=False)
print ('Success!')
