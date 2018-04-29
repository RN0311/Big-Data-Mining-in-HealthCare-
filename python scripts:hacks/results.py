import os

a = os.listdir('.')

try:
	a.remove("results.py")
	a.remove("util.py")
	a.remove("tmp.txt")
except Exception as e:
	pass

blep = 0

finalset = frozenset()

for i in a:
	# print i
	f = open(i,"r+")
	g = f.readlines()
	f.close()
	flag = 0
	count = 0
	genes = []
	for line in g:

		if count>=1220:
			break

		if "Ranked attributes" in line:
			flag = 1
			continue

		if flag == 1:
			count +=1
			x = line.strip().split()
			if len(x)==3:
				# print x[2]
				genes.append(x[2])

	if blep==0:
		# print len(frozenset(genes))
		finalset = frozenset(genes)
		blep+=1
	else:
		# print "what"
		finalset = finalset.intersection(frozenset(genes))

	# print "genes for this file",len(genes)

	# print "finalset: ",len(finalset)
	# print


# print len(list(finalset))

# for i in finalset:
# 	print i

print list(finalset)
print len(finalset)


