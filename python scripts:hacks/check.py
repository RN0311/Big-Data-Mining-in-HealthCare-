mainfile = '/home/samiya/Desktop/dataset.arff'

f = open(mainfile,"r+")
lines = len(f.readlines())
f.close()

for i in range(100):
	path = '/home/samiya/Desktop/mridul_weka/datasets/'+str(i)+".arff"
	f = open(mainfile,"r+")
	x = len(f.readlines())
	f.close()
	if x !=lines:
		print "what"