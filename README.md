# heliothine_reseq_paper
Coding for recreating some of the analyses from the heliothine reseq work. The first calculates the proportion of ancestry between two parent taxa, while the second calculates a hybrid index across sliding windows.
________________________________________________________
# 1. Proportion Ancestry

Included is a script for calculating the proportion of homozygous and heterozygous SNPs ancestrally derived from hybridising taxa.

It takes a tsv file consisting of 3 columns (taxa1, taxa2, hybrid), and outputs the proportion of h's (heterozygous genotypes) in the column "hybrid", as well as genotypes shared with taxa1. Taxa1 and Taxa2 are segregating genotypes for each of the two populations and can be stripped from a plink association test output.

The script in get_ap.py runs fine in Python 3, just paste the script into python all in one go.

Simply load a .tsv (without a header) using: snps = open("NAME_OF_FILE.tsv")

And then run the script with: get_apt(snps)

Enjoy!! If you think there can be improvements, drop me a line. :-)
________________________________________________________
# 2. Hybrid Index

- Use bedtools to break up the genome into predetermined window lengths.
bedtools makewindows -b armigera.bed -w 250000 > genome_windows.txt

Use the script hybridindex.py variants.txt genome_windows.txt

The variants.txt file is in the following format:
-bin is the window that the SNP falls in
-chr is chromosome
-bp is position of the SNP on the chromosome
-snp_name is the name of the SNP, it can ber anything, just no repeats
-sample is the sample specific genotype calls, where 1 is homo REF, 0.5 is a het and 0 is homo ALT.

bin	chr	bp	snp_name	sample
2_1	2	26991	2:26991[b37]C,T	1
2_1	2	27401	2:27401[b37]G,T	0
2_1	2	27661	2:27661[b37]C,T	0
2_1	2	30048	2:30048[b37]A,T	1
2_1	2	32230	2:32230[b37]C,T	0
2_1	2	44755	2:44755[b37]G,T	0
2_1	2	44834	2:44834[b37]C,T	0.5
2_1	2	46765	2:46765[b37]G,T	0
2_1	2	47673	2:47673[b37]A,G	0
2_1	2	53660	2:53660[b37]A,G	1

