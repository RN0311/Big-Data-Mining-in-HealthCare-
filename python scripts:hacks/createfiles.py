import random

file = '/home/samiya/Desktop/dataset.arff'
print file

f = open(file,'r+')
g = f.readlines()
f.close()

header = g[:1030]
content = g[1030:]

print len(content)
print content[0]

for i in range(100):
	path = '/home/samiya/Desktop/mridul_weka/datasets/'+str(i)+".arff"
	f = open(path,"w+")
	for i in header:
		f.write(i)
	random.shuffle(content)
	length = int(0.8*len(content))
	for i in range(length):
		f.write(content[i])
	f.close()

