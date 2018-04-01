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

Use bedtools to break up the genome into predetermined window lengths.<br>
bedtools makewindows -b armigera.bed -w 250000 > genome_windows.txt

The variants.txt file (example below) is in the following format:<br>
-chr is chromosome<br>
-bp is position of the SNP on the chromosome<br>
-snp_name is the name of the SNP, it can ber anything, just no repeats<br>
-sample is the sample specific genotype calls, where 1 is homo REF, 0.5 is a het and 0 is homo ALT. This can easily be stripped from a vcf, with the sample column being derived from a conversion of allele calls using sed<br>

chr	bp	snp_name	sample<br>
2	26991	2:26991[b37]C,T	1<br>
2	27401	2:27401[b37]G,T	0<br>
2	27661	2:27661[b37]C,T	0<br>
2	30048	2:30048[b37]A,T	1<br>
2	32230	2:32230[b37]C,T	0<br>
2	44755	2:44755[b37]G,T	0<br>
2	44834	2:44834[b37]C,T	0.5<br>
2	46765	2:46765[b37]G,T	0<br>
2	47673	2:47673[b37]A,G	0<br>
2	53660	2:53660[b37]A,G	1<br>

Use the script: <br>
hybridindex.py -v variants.txt -g genome_windows.txt -o out_window_averages


The output is a column of the bins (chr_bp) and another reporting the mean hybrid index for each bin.
