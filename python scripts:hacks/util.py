features = ['FOXP3', 'TLCD1', 'EMCN', 'FKBP11', 'PARP12', 'ZNF132', 'ENAM', 'AFG3L1', 'FABP4', 'SLC16A12', 'IL20RB', 'PAEP', 'PITX1', 'MNX1', 'CXCL13', 'UFSP2', 'STAT2', 'UGT1A10', 'PRAME', 'IL18BP', 'GSDMB', 'RYR2', 'ITPKA', 'KCNG1', 'INHBE', 'VIPR1', 'DLX4', 'SRP19', 'SLC27A2', 'CYP39A1', 'NR3C2', 'COL25A1', 'MFI2', 'GBP2', 'XPA', 'DNASE1L3', 'RNF43', 'OASL', 'RFPL3S', 'ZNF583', 'C7orf41', 'TSPAN7', 'GYPA', 'IGF2BP3', 'AGTR1', 'GPR68', 'APOBEC3H', 'TCL6', 'COL7A1', 'SEMA3G', 'PPPDE2', 'NTN4', 'TMEM25', 'DONSON', 'MSTO1', 'HSD3B7', 'ZNF542', 'GPD1L', 'GFPT2', 'SYN3']
test_set = ['SGK223','SLC22A16','FABP7','RXRA','GHSR', 'STK38', 'NKX2-3', 'SELS', 'SOX9', 'ZNF830', 'BEST1','PGLYRP2', 'ADM','CXCL5','TGFB3','FGFR3','SCG2', 'CLDN7','IL10RB','FUT10','MAP3K13', 'DSC2','CTSG','RPL39','POLD3','HUS1B','NEIL1','PIP5K1B','UBE2D3','TNFSF4','NODAL','COX7B','GPR77', 'SEMA3G','MNX1','TLR9', 'EMX2','SPOCK1']

boop = ['SPOCK1', 'EMX2', 'TLR9', 'MNX1', 'SEMA3G', 'GPR77', 'COX7B', 'NODAL', 'TNFSF4', 'UBE2D3', 'PIP5K1B', 'NEIL1', 'HUS1B', 'POLD3', 'RPL39', 'CTSG', 'DSC2', 'MAP3K13', 'FUT10', 'IL10RB', 'CLDN7', 'SCG2', 'FGFR3', 'TGFB3', 'CXCL5', 'ADM', 'PGLYRP2', 'BEST1', 'ZNF830', 'SOX9', 'SELS', 'NKX2-3', 'STK38', 'GHSR', 'RXRA', 'FABP7', 'SLC22A16', 'SGK223']

label = ["LABEL"]

print len(features)

# found = 0
# nf = 0

# print

# for i in test_set:
# 	if i in features:
# 		found+=1
# 		print i+" found"
# 	else:
# 		print i+" not found"
# 		nf+=1

# print
# print "SUMMARY"
# print "found",found
# print "not found",nf

f = open("/Users/mridul/Downloads/blep/mridul_weka/final.csv","r+")
g = f.readlines()
f.close()

indices = []

header = g[0].strip().split(",")

boop = frozenset(boop).union(frozenset(features))
boop = list(boop.union(label))
print(len(boop))

for b in boop:
	indices.append(header.index(b))

indices = sorted(indices)
# print header[indices[-1]]

f = open("98fdataset.csv","w+")
for line in g:
	x = []
	tmp = line.strip().split(",")
	for i in indices:
		x.append(tmp[i])
	# print x
	f.write(','.join(x) + "\n")
f.close()



