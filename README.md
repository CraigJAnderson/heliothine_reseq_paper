# heliothine_reseq_paper
Coding for recreating some of the analyses from the heliothine reseq work

Included is a script for calculating the proportion of homozygous and heterozygous SNPs ancestrally derived from hybridising taxa.

It takes data in the format listed below, and outputs the proportion of h's (heterozygous genotypes) in the column "hybrid", as well as genotypes shared with taxa1
Taxa1 and Taxa2 are segregating genotypes for each of the two populations and can be stripped from a plink association test output.

taxa1	taxa2	hybrid

1	0	0

1	0	0

1	0	0

1	0	0

1	0	1

1	0	1

1	0	1

1	0	1

1	0	h

1	0	h

1	0	h

1	0	h

The script below runs fine in Python 3, just paste the script into python all in one go...

def get_pa(snps):
	per =[]
	for snp in snps:
		columns = snp.rstrip().split()
		arm = columns[1]
		zea = columns[0]
		hyb = columns[2]
		if hyb == arm:
			per.append('a')
		elif hyb == zea:
			per.append('b')
		elif hyb == ('h'):
			per.append('h')
	cou_a = per.count('a')
	cou_b = per.count('b')
	cou_h = per.count('h')
	print(cou_h)
	print(cou_b)
	print((cou_b+cou_h)/(cou_a+cou_b+cou_h))

_______________________________________________________________________
and load a .tsv (without a header) using:

snps = open("NAME_OF_FILE.tsv")

And then run the script with:

get_apt(snps)

Enjoy!!




