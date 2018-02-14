# heliothine_reseq_paper
Coding for recreating some of the analyses from the heliothine reseq work. The first calculates the proportion of ancestry between two parent taxa, while the second calculates a hybrid index across sliding windows.
________________________________________________________
1. Proportion Ancestry

Included is a script for calculating the proportion of homozygous and heterozygous SNPs ancestrally derived from hybridising taxa.

It takes a tsv file consisting of 3 columns (taxa1, taxa2, hybrid), and outputs the proportion of h's (heterozygous genotypes) in the column "hybrid", as well as genotypes shared with taxa1. Taxa1 and Taxa2 are segregating genotypes for each of the two populations and can be stripped from a plink association test output.

The script in get_ap.py runs fine in Python 3, just paste the script into python all in one go.

Simply load a .tsv (without a header) using: snps = open("NAME_OF_FILE.tsv")

And then run the script with: get_apt(snps)

Enjoy!! If you think there can be improvements, drop me a line. :-)
________________________________________________________
2. Hybrid Index

# Use bedtools to break up the genome into predetermined window lengths.
bedtools makewindows -b armigera.bed -w 250000 > genome_windows.txt

# Example of calculating averages of bins in R.
row1<-aggregate(dat$row~dat$bin, FUN=mean)


