f = open("uh.txt",'r+')
g = f.readlines()
f.close()

genes= []

for i in g:
	x = i.strip().split()
	if len(x)==3:
		# print x[1]
		genes.append(x[1])

print genes