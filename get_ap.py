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
